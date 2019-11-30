from yoyo import step

step("CREATE TABLE foo (id INT, bar STRING, INDEX(id))", "DROP TABLE foo")
