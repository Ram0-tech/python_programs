class Company:
    def __init__(self):
        self.cname=input('Enter name of the company:')
    def display(self):
        print(self.cname)
class Development(Company):
    def __init__(self):
        super().__init__()
        self.developer_id=int(input('Enter developer id:'))
        self.developer_name = input('Enter developer name:')
    def display(self):
        super().display()
        print(self.developer_id)
        print(self.developer_name)
class Testing(Company):
    def __init__(self):
        super().__init__()
        self.tester_id=int(input('Enter tester id:'))
        self.tester_name=input('Enter tester name:')
    def display(self):
        super().display()
        print(self.tester_id)
        print(self.tester_name)
class Project(Development,Testing):
    def __init__(self):
        super().__init__() #method resolution order
        self.project_id=int(input('Enter the project id:'))
        self.project_name=input('Enter the project name:')
    def display(self):
        super().display()
        print(self.project_id)
        print(self.project_name)
p=Project()
p.display()
