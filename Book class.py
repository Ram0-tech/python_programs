class Book:
    def __init__(self):
        self.title=input('Enter the title: ')
        self.author=input('Enter the author name: ')
        self.price=float(input('Enter the price: '))
        self.language=input('Enter the language: ')
        self.pages=int(input('Enter pages: '))
    def gettitle(self):
        print(self.title)
    def getauthor(self):
        print(self.author)
    def getprice(self):
        print(self.price)
    def language(self):
        print(self.language)
    def getpages(self):
        print(self.pages)
    def settitle(self):
        self.title=input('Enter the title: ')
        print('new title value:',self.title)
        # self.gettitle()
    def setauthor(self):
        self.author=input('Enter the author name: ')
    def setprice(self):
        self.price=float(input('Enter the price: '))
b1=Book()
b1.gettitle()
b1.getauthor()
b1.getprice()
b2=Book()
b2.gettitle()
b2.settitle()
