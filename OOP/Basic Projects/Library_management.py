from abc import ABC,abstractmethod

class Book(ABC):
    def __init__(self,title):
        self.__title=title
        self.__is_available=True

    @property
    def title(self):
        return self.__title

    @property
    def is_available(self):
        return self.__is_available

    @abstractmethod
    def get_book_type(self):
        pass

    def borrow(self):
        if not self.__is_available:
            raise Exception("Book is not available")
        else:
            self.__is_available=False

    def return_book(self):
        self.__is_available=True


class PrintedBook(Book):
    def get_book_type(self):
        return "Printed Book"

class EBook(Book):
    def get_book_type(self):
        return "E Book"

class ReferenceBook(Book):
    def get_book_type(self):
        return "Reference Book"


class Library:
    def __init__(self):
        self.book_list=[]

    def add_book(self,book:Book):
        self.book_list.append(book)

    def borrow_book(self,book:Book):
        if book not in self.book_list:
            raise Exception(f"{book.title} {book.get_book_type()} doesn't belongs to this library")
        else:
            book.borrow()
            print(f"Borrowed: {book.title} ({book.get_book_type()})")

    def return_book(self,book:Book):
        if book not in self.book_list:
            raise Exception(f"{book.title} {book.get_book_type()} doesn't belongs to this library")
        else:
            book.return_book()
            print(f"Returned: {book.title()} ({book.get_book_type()})")
        
class User:
    def __init__(self,name):
        self.name=name

    def borrow_book(self,library:Library,book:Book):
        print(f"{self.name} requests to borrow '{book.title}'")
        library.borrow_book(book)

    def return_book(self,library:Library,book:Book):
        print(f"{self.name} is returning '{book.title}")


b1=PrintedBook("Harry Potter")
b2=EBook("Kimetsu no yaiba")
b3=ReferenceBook("Human Psychology")

lib=Library()
def add_books(*books):
    for i in books:
        lib.add_book(i)

add_books(b1,b2,b3)

u1=User("Ron")
u1.borrow_book(lib,b1)


