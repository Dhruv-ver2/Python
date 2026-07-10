#_________________________________________________________
class Product:
    store_name="D Mart"

    def __init__(self,name,id,price):
        self.name=name
        self.id=id
        self.price=price

    def show_details(self):
        print(f"Name: {self.name}\nStore: {self.store_name}\nID: {self.id}\nPrice: Rs. {self.price}\n")

    @classmethod
    def change_store_name(cls,name):
        cls.store_name=name

    @staticmethod
    def is_valid_price(price):
        return price>0
#_________________________________________________________


#_________________________________________________________
class ShoppingCart:
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        cart=self.products
        cart.append(product)
        print(f"{product.name} Successfully Added to the Cart")

    def remove_product(self,product):
        self.products.remove(product)
        print(f"{product.name} Successfully Removed from the Cart")

    def show_details(self):
        print(30*"_")
        print("The cart has the following products:-\n")
        sum=0
        c=0
        for product in self.products:
            print(f"{product.name}:\t{product.price}")
            sum+=product.price
            c+=1
           
        print(f"\nTotal number of products: {c}")
        print(f"Grand Total: {sum}")
        print(30*"_")

    def grand_total(self):
        total=0
        for product in self.products:
            total+=product.price

        return total
#_________________________________________________________


#_________________________________________________________        
class Customer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.cart=ShoppingCart()

    def show_customer(self):
        print(f"Name: {self.name}\nID: {self.id}")
#_________________________________________________________


p1=Product("Laptop",11,10**5)
p2=Product("Mouse",12,1000)
p3=Product("Keyboard",13,4000)
p4=Product("Monitor",14,50000)
p5=Product("Headphones",15,30000)
p6=Product("TV",16,3*10**5)

c1=Customer("Haabu",1)
c2=Customer("Alex",2)

c1.cart.add_product(p1)
c1.cart.add_product(p2)
c1.cart.add_product(p3)

c2.cart.add_product(p4)
c2.cart.add_product(p5)

c1.cart.show_details()
c2.cart.show_details()

c2.cart.remove_product(p5)
c2.cart.show_details()

l=[p1,p2,p3,p4,p5,p6]
for products in l:
    products.show_details()
    print(30*"_")

p1.store_name="Dell Enterprises"

for products in l:
    products.show_details()
    print(30*"_")