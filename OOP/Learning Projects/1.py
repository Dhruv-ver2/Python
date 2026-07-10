from random import randint as r

class BankAccount:
    bank_name="SBI"

    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance

    def deposit(self,amount):
        print(f"{self.name},\nRs. {amount} Deposited\nNow, total balance is {self.balance} + ",end='')
        self.balance+=amount
        print(f"{amount} = {self.balance}\n")

    def withdraw(self,amount):
        if (self.balance-amount)<0:
            print("Insufficient Balance")
        else:
            print(f"{self.name},\nRs. {amount} has been Deducted\nNow, total balance is {self.balance} - ",end='')
            self.balance-=amount
            print(f"{amount} = {self.balance}\n")

    def show_details(self):
        print(f"USER DETAILS\nAccount Holder: {self.name}\nAccount Number: {self.number}\nBalance: {self.balance}\nBank Name: {self.bank_name}\n")

    @classmethod
    def change_bank(cls,new_name):
        cls.bank_name=new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount>0


user_accounts=list()
n=int(input("Enter the number of users:"))
for i in range(n):
    print(f"User {i+1}")
    name=input("Enter the user name:")
    number=r(10**6,10**7)
    balance=int(input("Enter the balance:"))
    print("\n")

    user_accounts.append(BankAccount(name,number,balance))


for accounts in user_accounts:
    accounts.show_details()
    print("\n")


user_accounts[0].deposit(60000)
user_accounts[1].withdraw(10000)
user_accounts[1].change_bank("HDFC")

user_accounts[1].show_details()
