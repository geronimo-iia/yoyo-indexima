# file: migrations/0001.create-foo.py
from yoyo import step

__depends__ = {'0001.create-foo'}

step(
    "CREATE TABLE bar (id INT, foo STRING, INDEX(id))", "DROP TABLE bar"
)
