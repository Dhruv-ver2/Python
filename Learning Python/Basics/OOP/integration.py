from abc import ABC,abstractmethod

class Paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    @staticmethod
    def is_valid_amount(amount):
        return amount>0


class Card(Paymentmethod):
    def pay(self,amount):
        if not self.is_valid_amount(amount):
            raise ValueError("Invalid Amount")

        print(f"Paid {amount} via card")

class Upi(Paymentmethod):
    def pay(self,amount):
        if not self.is_valid_amount(amount):
            raise ValueError("Invalid Amount")

        print(f"Paid {amount} via upi")

class Cash(Paymentmethod):
    def pay(self,amount):
        if not self.is_valid_amount(amount):
            raise ValueError("Invalid Amount")

        print(f"Paid {amount} via cash")


class Order:
    def __init__(self):
        self.item=[]

    def add_item(self,name,price):
        self.item.append((name,price))

    def get_total(self):
        total=0
        for _,i in self.item:
            total+=i

        return total

    def pay(self, payment_method):
        total = self.get_total()
        payment_method.pay(total)



    
class User:
    def __init__(self,name):
        self.name=name

    def place_order(self):
        return Order()

    def pay_for_order(self,order:Order,payment_method:Paymentmethod):
        print(f"{self.name} is paying for the order...")
        order.pay(payment_method)


# Create user
user = User("Haabu")

# User creates an order
order = user.place_order()

# Add items
order.add_item("Book", 200)
order.add_item("Pen", 50)
order.add_item("Notebook", 150)

# Pay using different payment methods
user.pay_for_order(order, Upi())
