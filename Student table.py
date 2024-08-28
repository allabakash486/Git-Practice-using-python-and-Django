import sqlite3
conn = sqlite3.connect('Student table.db')
c = conn.cursor()

c.execute('''
             create table Student_detais(
             S_id number(4) primary key,
             s_name varchar(20) unique,
             s_age number(2) not null,
             gender varchar(10) not null)
             ''')
c.execute('''INSERT INTO STUDENT_DETAIS VALUES (1,'SHAIK',20,'MALE')''')
c.execute('''INSERT INTO STUDENT_DETAIS VALUES (2,'SHAIK',20,'MALE')''')
c.execute('''INSERT INTO STUDENT_DETAIS VALUES (3,'SHAIK',20,'MALE')''')
conn.commit()
print(c.execute('Select * from Student_detais'))
c.close()
