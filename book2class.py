class Book2:
    def __init__(self):
        self.book_no=int(input('Enter book no:'))
        self.btitle=input('Enter the title:')
        self.author=input('Enter authour name:')
        self.language=input('Enter language:')
        self.price=float(input('Enter price:'))
    def showbook(self):
        print(self.book_no,self.btitle,self.author,self.language,self.price)
    def upadate_book(self):
        a=input('enter the attribute you want to uodate(all/title/author/language/price):')
        if a=='title':
          self.btitle = input('Enter new title')
        elif a=='author':
          self.author = input('Enter new authour name:')
        elif a=='language':
          self.language = input('Enter language:')
        elif a=='price':
          self.price = float(input('Enter price:'))
        elif 'all':
            self.btitle = input('Enter the title:')
            self.author = input('Enter authour name:')
            self.language = input('Enter language:')
            self.price = float(input('Enter price:'))
        else:
            pass
    def deletebook(self):
        # del self.btitle
        l.remove(self)
        print('Book',self.btitle,'is deleted')
l=[]
while True:
    print('Library Operations:')
    print('1.Add book details\n','2.Show all details\n','3.Show details of a particular book\n','4.Update a book \n','5.Delete a book\n','6.Exit')
    ch=int(input('Enter the choice:'))
    if ch==1:
        b=Book2()
        l.append(b)
    elif ch==2:
        for i in l:
            i.showbook()
    elif ch==3:
        n=int(input('Enter  the book no:'))
        for i in l:
            if i.book_no==n:
                i.showbook()
                break
        else:
            print('Book not found')
    elif ch==4:
        n = int(input('Enter  the book no:'))
        for i in l:
            if i.book_no == n:
                i.upadate_book()
                break
        else:
            print('Book not found')
    elif ch==5:
        n = int(input('Enter  the book no to be delete:'))
        for i in l:
            if i.btitle == n:
               i.deletebook()
               break
        else:
            print('Book not found')

    else:
        print('Invalid choice!!!')
        exit()






