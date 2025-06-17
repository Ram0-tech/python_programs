# mysql
import mysql.connector

#connects to mysql db server using mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")

#creating a database file inside mysql db server
# sql_command='create database company'
con = mysql.connector.connect(user="root", password="root", host="localhost", database="company")
c = con.cursor()
# c.execute(sql_command)
# c.execute('create table employee(empid int primary key,name varchar(30),age int,gender varchar(10),salary int)')
# c.execute('insert into employee values(100,"Ram",24,"male",100000)')
# c.execute('insert into employee values(101,"Brinnet",20,"male",50000)')
# c.execute('insert into employee values(102,"Alphin",23,"male",60000)')
# c.execute('insert into employee values(103,"Anu",25,"female",40000)')
# con.commit()
# c.execute('select *from employee')
# k=c.fetchall()
# print(k)

