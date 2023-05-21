#create a class Book
class Book:
    def __init__(self, title, author, num_pages, genre):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.genre = genre
#printing the book information with print_info() method
    def print_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Number of Pages:", self.num_pages)
        print("Book Type:", self.genre)
        print()
#create class library
class Library:
    def __init__(self):
        self.books = []
#add_book() method
    def add_book(self, book):
        self.books.append(book)
#printing the information of all books in the library with print_book() method   
    def print_books(self):
        print("All books in the library:")
        for book in self.books:
            book.print_info()
 #borrowing book from  the Library with method borrow_book() 
    def borrow_book(self, title):
        for book in self.books:
          #if title in lower case matches any title in lower case
            if book.title.lower() == title.lower():
             #remove the book from books list 
                self.books.remove(book)
                print(f"Book {book.title} by {book.author} borrowed from the library.")
                return book
        return None
#instance of class Lbrary()
library = Library()

#open book.txt file and Assuming the "books.txt" file contains book information separated by commas (title, author, num_pages, genre) on each line
with open("books.txt", "r") as file:
    for line in file:
     #use strip() to remove trailing or leading white space in the string on each line and split(",") to split the string on each line that is separated by "," in to sub strings
        title, author, no_of_pages, genre = line.strip().split(",")
        #instance of class Book 
        book = Book(title, author, no_of_pages, genre)
       #adding the book to the library
        library.add_book(book)
#printing the books in the library
library.print_books()

#assuming no book is borrowed 
borrowed_book = None
while borrowed_book is None:
#ask the user for the title of the book they want to borrow
    title = input("Enter the title of the book you want to borrow: ")
    borrowed_book = library.borrow_book(title)
   #if title does not match any book title in the library
    if borrowed_book is None:
        print("Book not found.")

print("Books in the library after borrowing:")
#printing list of books after borrowin
library.print_books()