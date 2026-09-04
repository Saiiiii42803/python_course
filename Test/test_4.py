class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrow = False
    def borrow(self):
        self.is_borrow = True
        print(f"{self.title} has beeen borrowed")
    def return_book(self):
        print(f"{self.title} has been returned")
        self.is_borrow = False

b1 = Book("Diary","tim")
b2 = Book("while","tom")

print(b1.title)
print(b1.author)
b1.borrow()
b1.return_book()

print(b2.title)
print(b2.author)
b2.borrow()
b2.return_book()