"""Define internale migration V1."""
from yoyo.backends import DatabaseBackend


def upgrade(backend: DatabaseBackend):
    """Apply V1 migration."""
    backend.execute(f"drop table if exists {backend.migration_table_quoted}")
    backend.execute(
        f"CREATE TABLE {backend.migration_table_quoted} (" "id STRING," "ctime TIMESTAMP(SECOND), INDEX(id))"
    )
