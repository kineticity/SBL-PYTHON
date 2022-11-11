import sqlite3
conn=sqlite3.connect('TED.db')
print("Opened Database successfully")

conn.execute('''CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,'Dan',32,'California',20000.00);")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'Joe',32,'Idaho',10000.00);")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,'Simon',32,'Oregon',30000.00);")
conn.commit()
print("Records entered successfully")

cursor=conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM COMPANY;")

for row in cursor:
    #print(row)
    print("ID: ",row[0])
    print("NAME: ", row[1])
    print("AGE: ", row[2])
    print("ADDRESS: ", row[3])
    print("SALARY: ", row[4],"\n")
print("Values displayed successfully")
conn.close()

conn=sqlite3.connect('TED.db')
print("Reopened Database successfully")

conn.execute("UPDATE COMPANY SET SALARY=30000 WHERE ID=1")
conn.commit()
print("Total no. of rows updated: ",conn.total_changes)
print("Now the table has values: \n")
cursor=conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM COMPANY;")
for row in cursor:
    print("ID: ",row[0])
    print("NAME: ", row[1])
    print("AGE: ", row[2])
    print("ADDRESS: ", row[3])
    print("SALARY: ", row[4],"\n")

conn.close()

