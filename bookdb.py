# create two tables Books and Author
#
# Books  --bookno,title,author id(foreign),price,pages,published year
#
# Author ---author_id,name,nationality,birthyear

import sqlite3
con=sqlite3.connect('book.db')
# con.execute('drop table books')
# con.execute('create table author(author_id int primary key,name varchar(50),nationality varchar(50),birthyear int) ')
# con.execute('create table books(book_no int primary key,title varchar(50),author_id int,price int,pages int  , published_year int,foreign key(author_id) references author(author_id))')
# con.execute('insert into author values(10,"George RR Martin","America",1948)')
# con.execute('insert into author values(11,"A.P.J Abdul kalam" ,"India",1931)')
# con.execute('insert into author values(12,"Paulo Coelho" ,"Brazil",1947)')
# con.execute('insert into author values(13,"J k Rowling","British",1965)')
# con.execute('insert into books values(100,"A song of ice and fire",10,500,450,1996)')
# con.execute('insert into books values(101,"Wings of fire",11,410,500,1999)')
# con.execute('insert into books values(102,"The Alchemist",12,350,400,1988)')
# con.execute('insert into books values(103,"Harry potter",13,600,700,1997)')
# con.commit()

# 1,Find all books of specific author
# s=con.execute('select title,author.name from books join author  on books.author_id=author.author_id where author.name="Paulo Coelho"')
# print(s.fetchall())

# 2.Find the publication year of a particular book
# s=con.execute('select title,published_year from books where title="Wings of fire"')
# print(s.fetchall())

# 3.Find the youngest author
# s=con.execute('select name,max(birthyear) from author')
# print(s.fetchall())
#    OR
# s=con.execute('select name, from author where order by birthyear desc limit 1')
# print(s.fetchall())

# 4.List books with their corresponding author where booktitle contains a specific keyword
# s=con.execute('select title,author.name  from books join author on books.author_id=author.author_id where title  like "%l%"  ')
# print(s.fetchall())

# 5.list all authors who have written books published after a particular year.
# s=con.execute('select title,author.name,published_year from books join author on books.author_id=author.author_id where published_year>1996')
# print(s.fetchall())