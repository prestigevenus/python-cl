import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfully")
conn.execute("INSERT INTO EMPLOYEE VALUES (11,'FAITH KARIMI',34,34000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (12,'JOE KIM',32,120000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (13,'DERRIC KAREEM',27,85000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (14,'JOY PEACE',41,560000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (15,'DOREA CARDISTA',23,345000.00)")

conn.commit()
print("Employee inserted successfully")
conn.close()