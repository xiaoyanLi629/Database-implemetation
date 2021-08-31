import sqlite3

def crud(conn):
  row = ("Cam", 95, "")
  conn.execute('INSERT INTO students VALUES (?, ?, ?);', row)
  conn.execute('UPDATE students SET grade = 100 WHERE name is "Dennis";')
  conn.execute('UPDATE students SET grade = grade-15 WHERE name LIKE "%z%";')
  conn.execute('UPDATE students SET notes = "SUCKER" WHERE name LIKE "%z%";')
  conn.execute('DELETE FROM students WHERE grade <= 65')