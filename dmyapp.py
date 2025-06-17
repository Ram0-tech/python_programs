import sqlite3

con = sqlite3.connect('dCompany.db')
# sql_command='create table tablename(property1 type1,property2 type2,....)
# con.execute('drop table employee1')
con.execute('drop table Employee')
sql_command='create table Employee(eid int primary key,name varchar(50),age int,gender varchar(10),salary int,place varchar(40))'
con.execute(sql_command)
# print('Table created')
sql_command = 'insert into Employee(eid,name,age,gender,salary,place)values(100,"Ram",24,"male",50000,"Thrissur")'
con.execute(sql_command)
con.execute('insert into Employee(eid,name,age,gender,salary,place)values(101,"Brinnet",20,"male",45000,"Idukki")')
con.execute('insert into Employee(eid,name,age,gender,salary,place)values(102,"Alphin",22,"male",30000,"Ernakulam")')
con.execute('insert into Employee values(103,"Anu",25,"female",15000,"Kannur")')
con.commit()
# print('Data inserted successfully')

# Read/Retrieval
# sql_command='select attributes from tablename where condition'
s=con.execute('select *from Employee')
print(s.fetchall())
# s=con.execute('select name from Employee1 where place="Ernakulam"')
# for i in s:
#     print(i)
# s=con.execute('select *from Employee1 where salary between 15000 and 30000')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where salary in(15000,50000)')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "a%"')  # % --> 0 or more character
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "r__"')  #_ -->exactly one character
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "__m"')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "%t"')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "%p%"')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "%p%" and age>20')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where name like "%a%" or age=22')
# print(s.fetchall())
# s=con.execute('select *from Employee1 where salary!=15000 and salary!=25000')
# print(s.fetchall())
# #      OR
# s=con.execute('select *from Employee1 where salary not in(15000,25000)')
# print(s.fetchall())
#
# s=con.execute('select *from Employee1 order by salary')
# print(s.fetchall())
#
# s=con.execute('select *from Employee1 order by salary desc')
# print(s.fetchall())
#
# s=con.execute('select distinct(place) from Employee1')
# print(s.fetchall())

# update
# print('Before update')
# s=con.execute('select *from Employee1')
# print(s.fetchall())
# con.execute('update Employee1 set name="Ramprakash",salary=100000 where eid=100')
# con.commit()
# print('After update')
# s=con.execute('select *from Employee1')
# print(s.fetchall())

# Delete
# print('Before Delete')
# s=con.execute('select *from Employee1')
# print(s.fetchall())
# con.execute('delete from Employee1 where eid=101')
# con.commit()
# print('After Delete')
# s=con.execute('select *from Employee1')
# print(s.fetchall())

# limit clause
# s=con.execute('select *from Employee1 limit 1')
# print(s.fetchall())

# s=con.execute('select *from  Employee1 limit 2')
# print(s.fetchall())


# offset
# s=con.execute('select *from Employee1 limit 1 offset 2')#skip 2 rows
# print(s.fetchall())

#alter command(to change structure of a table)
#add column --> alter table tablename add column coulmnname type
# print("before Alter")
# s=con.execute('select *from Employee1')
# print(s.fetchall())
# con.execute('alter table Employee1 add column email varchar(30)')
# con.execute('insert into Employee1 values(104,"Xavier",26,"male",40000,"Ernakulam","xavi123@gmail.com")')
# con.commit()
# print('Afer alter')
# s=con.execute('select *from Employee1')
# print(s.fetchall())

# delete column -->alter table tablename drop column coulmnname
# print("before Alter")
# s=con.execute('select *from Employee1')
# print(s.fetchall())
# con.execute('alter table Employee1 drop column email')
# print('Afer alter')
# s=con.execute('select *from Employee1')
# print(s.fetchall())

#rename table name -->alter table tablename rename  to new tablename

# con.execute('alter table Employee1 rename to  employeee1')
# con.commit()

# rename column name --> alter table tablename rename column     coulmnname to column name
# print("before Alter")
# s=con.execute('select *from Employee1')
# print(s.fetchall())
# con.execute('alter table Employee1 rename column eid to empid ')
# print('Afer alter')
# s=con.execute('select *from Employee1')
# print(s.fetchall())

# aggregate fns
# k=con.execute('select count(*),max(salary),min(age),sum(salary),avg(age) from Employee1' )
# print(k.fetchall())


# group by
# s=con.execute('select gender,sum(salary) from Employee group by gender')
# print(s.fetchall())
# s=con.execute('select place,count(*)from Employee group by place')
# print(s.fetchall())

# group  by having
# s=con.execute('select gender,sum(salary) from Employee group by gender having sum(salary)>50000')
# print(s.fetchall())