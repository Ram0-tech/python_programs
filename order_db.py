import mysql.connector
# con=mysql.connector.connect(user='root',password='root',host='localhost')
sql_command='create database order_db'
con=mysql.connector.connect(user='root',password='root',host='localhost',database='order_db')
c=con.cursor()
# c.execute('drop table orders')
# c.execute('drop table customers')
# c.execute(sql_command)
# c.execute('create table customers(id int primary key,name varchar(30),email varchar(50),phone bigint)')
# c.execute('create table orders(id int primary key,customer_id int,order_date date,amount int,foreign key(customer_id) references customers(id))')
# c.execute('insert into customers values(1,"Amjad","amjad@gmail.com",9045786432)')
# c.execute('insert into customers values(2,"Sherooq","sherooq@gmail.com",8095472310)')
# c.execute('insert into customers values(3,"Anuranj","anuranj@gmail.com",7035261729)')
# c.execute('insert into customers values(4,"Anandu","anandu@gmail.com",6267839211)')
# c.execute('insert into orders values(100,1,"2025-02-05",5000)')
# c.execute('insert into orders values(101,2,"2025-01-10",1000)')
# c.execute('insert into orders values(102,3,"2025-03-01",2000)')
# c.execute('insert into orders values(103,4,"2025-01-20",3000)')
# con.commit()

#retrieve and display all orders with customer name
# c.execute('select orders.id,customer_id,name,order_date,amount from orders join customers on customers.id=orders.customer_id ')
# k=c.fetchall()
# print(k)

# update the phn and emaildetails of customer id=1
# c.execute('update customers set phone=8045786432,email="amjad1@gmail.com" where id=1')
# con.commit()

# find the total amount spend by each customer
# c.execute('select name,sum(amount) from orders join customers on  customers.id=orders.customer_id group by name')
# k=c.fetchall()
# print(k)

#count the number of orders per customer
# c.execute('select name,count(orders.id) from orders join customers on  customers.id=orders.customer_id group by name')
# k=c.fetchall()
# print(k)

# add an additional field place to customer table
c.execute('alter table customers add column place varchar(50)')

