class Employee:
    def __init__(self):
        self.empid=int(input('Enter employee id:'))
        self.ename=input('Enter employee name:')
        self.eage=int(input('Enter age:'))
        self.esalary=float(input('enter employee salary:'))
    def showdetails(self):
        print(self.empid,self.ename,self.eage,self.esalary)
e1=Employee()
e1.showdetails()
e2=Employee()
e2.showdetails()