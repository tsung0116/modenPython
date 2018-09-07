import sqlite3
conn = sqlite3.connect('2017-11.db')
curs = conn.cursor()
curs.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(curs.fetchall())
curs.execute("select sql from sqlite_master where type = 'table' and name = 'mail';")
print(curs.fetchall())