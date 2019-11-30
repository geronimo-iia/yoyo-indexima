from yoyo import step

step("CREATE TABLE foobar (id INT, foobar STRING, INDEX(id))", "DROP TABLE foobar")
