import datetime
import sqlite3

def convert_to_sql(dict_):
  conn = sqlite3.connect("test.db")
  conn.execute('CREATE TABLE bitcoin(time TEXT, price NUM)')
  for ele in dict_:
    row = []
    row.append(ele.strftime("%Y-%m-%d %H:%M:%S"))
    row.append(dict_[ele])
    conn.execute('INSERT INTO bitcoin VALUES (?, ?);', row)
    
  
  conn.commit()
  conn.close()