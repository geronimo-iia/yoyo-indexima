"""Connections utility.

Change:

- get_backend use migration table name from Backend class
- register indexima backend on first call
- add typing

"""
from yoyo import get_backend as yoyo_get_backend
from yoyo.backends import DatabaseBackend
from yoyo.connections import BACKENDS

from .backend import IndeximaBackend


__all__ = ['get_backend', 'register_backend', 'INDEXIMA_BACKEND_KEY']

INDEXIMA_BACKEND_KEY = 'indexima'


def register_backend(name: str, backend: DatabaseBackend):
    """Register specified backend."""
    BACKENDS[name] = backend


def get_backend(uri: str, backend=IndeximaBackend) -> DatabaseBackend:
    """Return associated backend."""
    register_backend(name=INDEXIMA_BACKEND_KEY, backend=backend)
    return yoyo_get_backend(uri=uri, migration_table=IndeximaBackend.migration_table)
