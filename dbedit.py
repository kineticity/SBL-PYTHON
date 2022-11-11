import sqlite3
conn=sqlite3.connect('TED.db')
print("Opened Database successfully")

conn.execute('DROP TABLE COMPANY;')