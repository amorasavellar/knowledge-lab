from book import Book 
from library import Library

def main():
    
    library = Library()
    
    #defined book details
    book1 = Book("The Da Vinci Code", "Dan Brown", 2003)
    book2 = Book("Inferno", "Dan Brown", 2011)
    book3 = Book("Angels & Demons", "Dan Brown", 2000)
    
    #adding books on the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    #list books from the library
    library.list_books()
    
    #search a book from the library
    library.search_book("Angels & Demons")
    
    #removing a book from the library
    library.remove_book("The Da Vinci Code")


if __name__ == "__main__":
        main()