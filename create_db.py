import sqlite3
from sys import argv

db_path = argv[1]

connection = sqlite3.connect(db_path)

with open("schema.sql", "r") as schema_file:
    sql_schema = schema_file.read()
    cursor = connection.cursor()
    cursor.executescript(sql_schema)

connection.close()

