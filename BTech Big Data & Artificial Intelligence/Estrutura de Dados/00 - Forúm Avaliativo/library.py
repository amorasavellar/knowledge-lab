from book import Book

class Library:
    def __init__(self:list) -> None:
        self.book_list = []
        
    def add_book(self, book:Book):
        self.book_list.append(book)
        print(f"The book {book.title} has been added to the library!")
        
    def remove_book(self, title:str):
        if len(self.book_list) >0:
            for item in range(0,len(self.book_list)-1):
                if title in self.book_list[item].title:
                    self.book_list.pop(item)
                    print(f"The book {title} has been removed from the library!")
                    break
                else:
                    print(f"The book {title} has not find.")
                    break
        else:
            print(f"No has been any book registrer on the library!")
    
    def search_book(self, title:str):
        if len(self.book_list) >0:
            for item in range(0,len(self.book_list)-1):
                if title in self.book_list[item].title:
                    print(f"Book Number: {item+1} Title: {self.book_list[item].title} Author: {self.book_list[item].author} Year_of_Publication: {self.book_list[item].year_of_publication}\n")
                    break
                else:
                    print(f"The book {title} has not find.")
                    break
        else:
            print(f"No has been any book registrer on the library!")
        
    
    def list_books(self):
        try:
            if len(self.book_list) >0:
                print("\n>>>>>>>>>>>>>>>>List of All Books in the Library<<<<<<<<<<<<<<<<\n")
                for item in range(0,len(self.book_list)):
                    print(f"Book Number: {item+1} Title: {self.book_list[item].title} Author: {self.book_list[item].author} Year_of_Publication: {self.book_list[item].year_of_publication}")
            else:
                print(f"No has been any book registrer on the library!")
        
        except Exception as e:
            print(e)