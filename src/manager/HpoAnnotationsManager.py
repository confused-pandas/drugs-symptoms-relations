import sqlite3
from sqlite3 import Error


try:
    conn = sqlite3.connect("./res/database/hpo/hpo_annotations.sqlite")
except Error as e:
    print(e)

 
cur = conn.cursor()
cur.execute('SELECT disease_db, disease_id, sign_id FROM phenotype_annotation;')
rows = cur.fetchall()

for row in rows:
    print(row)
