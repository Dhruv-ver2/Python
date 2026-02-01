from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance

    @abstractmethod
    def withdraw(self,value):
        pass

    @abstractmethod
    def type(self):
        pass
    
    def deposit(self,value):
        if not value<=100 or value>=5e5:
            self._balance+=value




class SavingsAccount(Account):
    def type(self):
        return "Savings Account"
    
    def withdraw(self,value):
        if value>self._balance:
            raise ValueError(f"Insufficient Balance")
        else:
            self._balance-=value

class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self._overdraft_limit=5000

    def type(self):
        return "Current Account"

    def withdraw(self,value):
        self._balance-=value
        if self._balance<0:
                if self._overdraft_limit+self._balance<0:
                    raise ValueError("Overdraft limit Exceeded")
                else:
                    self._overdraft_limit=self._overdraft_limit+self._balance

class FixedDeposit(Account):
    def type(self):
        return "Fixed Deposit Account"
    
    def withdraw(self,value):
        raise Exception("Withdrawl is forbidden at Fixed Deposit account")



class Bank:
    def __init__(self,name):
        self.bank_name=name
        self.ac_list=[]

    def create_account(self,name,balance,ac_type):
        accounts={"Savings":SavingsAccount,"Current":CurrentAccount,"Fixed Deposit":FixedDeposit}
        ac=accounts[ac_type.title()](name,balance)
        print(f"Mr.{ac._name} is initially depositing Rs.{balance}\n{ac.type()} has been created for Mr.{name} at {self.bank_name}")
        print(f"\nInitial Balance: Rs.{balance} \nDeposit Limit: MINIMUM==> Rs.100\t MAXIMUM==> Rs.500000")
        if ac.type()=="Current Account":
            print(f"Overdraft limit: Rs.10000")
        self.ac_list.append(ac)
        return ac
        
    def withdraw(self,ac:Account,value):
        if not ac in self.ac_list:
            raise Exception(f"{ac._name} don't have account at {self.bank_name}")
        ac.withdraw(value)
        print(f"Rs {value} has been debited from Mr.{ac._name}'s account at {self.bank_name}") 

    def deposit(self,ac:Account,value):
        if not ac in self.ac_list:
            raise Exception(f"{ac._name} don't have account at {self.bank_name}")
        ac.deposit(value)
        print(f"Rs.{value} has been credited to Mr.{ac._name}'s account at {self.bank_name}")
        



class User:
    def __init__(self,name):
        self.name=name

    def create_user_account(self,bank:Bank,account_type,balance):
        print(f"{self.name} is requesting to open a {account_type} account at {bank.bank_name}")
        return bank.create_account(self.name,balance,account_type)
        
    def withdraw(self,bank:Bank,acc:Account,amount):
        print(f"\n{self.name} is requesting a withdrawl of {amount} at {bank.bank_name}")
        bank.withdraw(acc,amount)

    def deposit(self,bank:Bank,acc:Account,amount):
        print(f"\n{self.name} is requesting a deposite of {amount} at {bank.bank_name}")
        bank.deposit(acc,amount)




b1=Bank("SBI")

u1=User("Harry")
u1_acc=u1.create_user_account(b1,"Current",22000)
u1.withdraw(b1, u1_acc,4000)
u1.deposit(b1,u1_acc,12000)

