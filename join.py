import sqlite3
con=sqlite3.connect('shop.db')
# con.execute('drop table product')
# con.execute('drop table order_details')
# con.execute('create table product(product_id int primary key,pname varchar(50),price int)')
# con.execute('create table order_details(order_id int primary key,p_id int,product_quantity int,foreign key(p_id) references product(product_id))')
# con.execute('insert into product values(100,"prodA",1000)')
# con.execute('insert into product values(101,"prodB",50)')
# con.execute('insert into product values(102,"prodB",250)')
# con.execute('insert into product values(103,"prodC",100)')
# con.commit()
# con.execute('insert into order_details values(1,101,1)')
# con.execute('insert into order_details values(2,102,2)')
# con.commit()

# inner join
# syntax:
# 'select attributes from table1 inner join table2 on condition '
# k=con.execute('select * from product join order_details on product.product_id=order_details.p_id')
# print(k.fetchall())
# k=con.execute('select product_id,pname,price from product join order_details on product.product_id=order_details.p_id')
# print(k.fetchall())

# outer join(left outer join)
# syntax:
# 'select attributes from table1 left join table2 on condition '
# k=con.execute('select *from product left join order_details on product.product_id=order_details.p_id')
# print(k.fetchall())

# cross join
# syntax:
# 'select attributes from table1 cross join table2  '
# k=con.execute('select *from product cross join order_details ')
# print(k.fetchall())
