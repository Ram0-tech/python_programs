from urllib.request import install_opener


class Account:
    def __init__(self):
        print('Acoount Details')
        self.acnumber = int(input('Enter the account number:'))
        self.acname = input('Enter the name:')
        self.acbalance = float(input('Enter the balance:'))

    def deposit(self):
        deposit = float(input('Enter the deposite Amount'))
        self.acbalance = self.acbalance + deposit

    def withdraw(self):
        withdraw = float(input('Enter the withdrawal Amount'))
        self.acbalance = self.acbalance - withdraw

    def show_balance(self):
        print('Balance:', self.acbalance)


l = []
while True:
    print('Bank Operations \n', '1.Create Account\n', '2.Deposit \n' '3.Withdraw\n', '4.Showbalance\n')
    ch = int(input('Enter the choice:'))
    if ch == 1:
        a = Account()
        l.append(a)
    elif ch == 2:
        n = int(input('Enter the Account number:'))
        for i in l:
            if i.acnumber == n:
                i.deposit()
                break
        else:
            print('Account does not exist')
    elif ch == 3:
        n = int(input('Enter the Account number:'))
        for i in l:
            if i.acnumber == n:
                i.withdraw()
                break
        else:
            print('Account does not exist')
    elif ch == 4:
        n = int(input('Enter the Account number:'))
        for i in l:
            if i.acnumber == n:
                i.show_balance()
                break
        else:
            print('Account does not exist')
    else:
        print('Invalid choice')
        exit()
