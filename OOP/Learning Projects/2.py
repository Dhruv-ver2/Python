class Book:
    library_name="Central Library"

    def __init__(self,title, author,issued=False):
        self.title=title
        self.author=author
        self.issued=issued

    def show_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nLibrary: {self.library_name}\nStatus: {self.issued}\n")

    @classmethod
    def change_library_name(cls,name):
        cls.library_name=name

    @staticmethod
    def is_valid_title(title):
        return title.isspace()


class Member:

    def __init__(self,name,_id):
        self.name=name
        self._id=_id

    def borrow_book(self,book):
        if book.issued:
            print(f"{book.title} is already issued")
        else:
            book.issued=True
            print(f"{self.name} borrowed {book.title}")

    def return_book(self,book):
        if book.issued:
            book.issued=False
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{book.title} is not issued yet")

    def show_details(self):
        print(f"Name: {self.name}\nId: {self._id}\n")



b1=Book("Harry Potter","JK Rowling")
b2=Book("Demon Slayer","Koyoharu Gotouge")
b3=Book("Clean Code","Robert Hook")

m1=Member("Haabu",101)
m2=Member("Alex",202)

b1.show_details()
b2.show_details()
b3.show_details()

m1.show_details()
m2.show_details()

       
m1.borrow_book(b1)
m1.borrow_book(b2)
m1.borrow_book(b3)

m2.borrow_book(b1)
m1.return_book(b1)
m2.borrow_book(b1)

Book.change_library_name("State Library")
b1.show_details()
b2.show_details()
b3.show_details()