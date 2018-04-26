import sqlite3
from sqlite3 import Error


try:
    conn = sqlite3.connect("/home/najib/Downloads/chinook.db")
except Error as e:
    print(e)

 
cur = conn.cursor()
cur.execute('SELECT * FROM albums')
rows = cur.fetchall()

for row in rows:
    print(row)
