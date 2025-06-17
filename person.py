# values insert dynamically
import sqlite3
con=sqlite3.connect('person.db')
# con.execute('create table Person(name varchar(30)primary key,age int)')
while(True):
 n=input('Enter the name:')
 a=int(input('Enter the age:'))
 con.execute('insert into Person values(?,?)',(n,a))
 con.commit()
# print('Data inserted')
# s=con.execute('select *from Person where name=?',(n,))
# print(s.fetchall())