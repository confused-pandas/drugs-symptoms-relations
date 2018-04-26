import sqlite3
from sqlite3 import Error


try:
    conn = sqlite3.connect("/home/depot/2A/gmd/projet_2017-18/hpo/hpo_annotations.sqlite")
except Error as e:
    print(e)

 
cur = conn.cursor()
cur.execute('SELECT disease_db, disease_id, sign_id FROM %s', tablename)
 
