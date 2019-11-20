# file: migrations/0001.create-foo.py
from yoyo import step

step("CREATE TABLE foo (id INT, bar STRING, INDEX(id))", "DROP TABLE foo")
