import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import (
    MetaData, create_engine, func, select, text,
    DateTime, Date, Integer, String, Text, Float, Numeric, Boolean
)

load_dotenv()

SQLITE_PATH = Path(os.getenv("SQLITE_DB_PATH", "school.db")).resolve()
POSTGRES_URL = (os.getenv("DATABASE_URL") or "").strip()


def normalize_postgres_url(url: str) -> str:
    if url.startswith("postgres://"):
        return "postgresql+psycopg2://" + url[len("postgres://"):]
    if url.startswith("postgresql://") and "+psycopg2" not in url:
        return "postgresql+psycopg2://" + url[len("postgresql://"):]
    return url


def die(message: str):
    print(f"\n❌ {message}")
    sys.exit(1)


def make_postgres_compatible(metadata: MetaData):
    for table in metadata.tables.values():
        for column in table.columns:
            type_name = column.type.__class__.__name__.upper()

            if type_name in {"DATETIME", "TIMESTAMP"}:
                column.type = DateTime()
            elif type_name == "DATE":
                column.type = Date()
            elif type_name in {"INTEGER", "BIGINT", "SMALLINT"}:
                column.type = Integer()
            elif type_name in {"TEXT", "CLOB"}:
                column.type = Text()
            elif type_name in {"REAL", "FLOAT", "DOUBLE"}:
                column.type = Float()
            elif type_name in {"NUMERIC", "DECIMAL"}:
                column.type = Numeric()
            elif type_name in {"BOOLEAN", "BOOL"}:
                column.type = Boolean()
            elif type_name in {"VARCHAR", "NVARCHAR", "CHAR", "NCHAR"}:
                length = getattr(column.type, "length", None)
                column.type = String(length) if length else String()


if not SQLITE_PATH.exists():
    die(f"SQLite file not found: {SQLITE_PATH}")

if not POSTGRES_URL:
    die("DATABASE_URL is missing in .env")

POSTGRES_URL = normalize_postgres_url(POSTGRES_URL)

if not POSTGRES_URL.startswith("postgresql"):
    die("DATABASE_URL must be a PostgreSQL URL")

sqlite_engine = create_engine(f"sqlite:///{SQLITE_PATH.as_posix()}")
postgres_engine = create_engine(
    POSTGRES_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)

print(f"SQLite source : {SQLITE_PATH}")
print("PostgreSQL    : connection configured from DATABASE_URL")
print()

source_meta = MetaData()
source_meta.reflect(bind=sqlite_engine)

if not source_meta.tables:
    die("No tables were found in the SQLite database.")

print("Tables found:")
for name in source_meta.tables:
    print(f"  - {name}")

make_postgres_compatible(source_meta)
print("\n✅ SQLite column types converted to PostgreSQL-compatible types.")

try:
    source_meta.create_all(bind=postgres_engine, checkfirst=True)
except Exception as exc:
    die(f"Could not create PostgreSQL tables: {exc}")

target_meta = MetaData()
target_meta.reflect(bind=postgres_engine)

non_empty = []
with postgres_engine.connect() as conn:
    for table_name in source_meta.tables:
        target_table = target_meta.tables.get(table_name)
        if target_table is None:
            die(f"Target table was not created: {table_name}")

        count = conn.execute(
            select(func.count()).select_from(target_table)
        ).scalar_one()

        if count:
            non_empty.append((table_name, count))

if non_empty:
    print("\nTarget contains data:")
    for name, count in non_empty:
        print(f"  - {name}: {count} row(s)")
    die(
        "Migration stopped to prevent duplicate data. "
        "Use an empty PostgreSQL database or clear the partial target tables first."
    )

total_rows = 0

for source_table in source_meta.sorted_tables:
    table_name = source_table.name
    target_table = target_meta.tables[table_name]

    with sqlite_engine.connect() as src:
        rows = src.execute(select(source_table)).mappings().all()

    if not rows:
        print(f"⏭️  {table_name}: 0 rows")
        continue

    payload = [dict(row) for row in rows]

    try:
        with postgres_engine.begin() as dst:
            batch_size = 1000
            for start in range(0, len(payload), batch_size):
                dst.execute(
                    target_table.insert(),
                    payload[start:start + batch_size],
                )
    except Exception as exc:
        die(f"Failed while copying table '{table_name}': {exc}")

    total_rows += len(payload)
    print(f"✅ {table_name}: {len(payload)} row(s)")

prep = postgres_engine.dialect.identifier_preparer

with postgres_engine.begin() as conn:
    for table_name, table in target_meta.tables.items():
        pk_cols = list(table.primary_key.columns)

        if len(pk_cols) != 1:
            continue

        pk = pk_cols[0]

        try:
            if not issubclass(pk.type.python_type, int):
                continue
        except Exception:
            continue

        q_table = prep.quote(table_name)
        q_col = prep.quote(pk.name)

        try:
            seq_name = conn.execute(
                text("SELECT pg_get_serial_sequence(:table_name, :column_name)"),
                {"table_name": table_name, "column_name": pk.name},
            ).scalar()

            if not seq_name:
                continue

            max_id = conn.execute(
                text(f"SELECT MAX({q_col}) FROM {q_table}")
            ).scalar()

            if max_id is not None:
                conn.execute(
                    text("SELECT setval(:seq_name, :max_id, true)"),
                    {"seq_name": seq_name, "max_id": int(max_id)},
                )
        except Exception as exc:
            print(f"⚠️  Sequence reset skipped for {table_name}: {exc}")

print("\n" + "=" * 60)
print(f"✅ Migration complete. Total copied rows: {total_rows}")
print("✅ Original SQLite database was NOT changed.")
print("=" * 60)
