class library :
    def __init__(self):
        self.books = []

    def add_book (self,title,author):
            self.books.append({"title":title, "author":author})

    def remove_book (self,title):
         for book in self.books:
              if book["title"] == title:
                   self.books.remove(book)
                   print("book was removed successfully :thumbs_up:")
                   return
         print("this book is not in the library")

    def search_book (self,title):
         for book in self.books:
              if book["title"]== title:
                   print(f"{book} is available")
                   return
         print(f"{title} is not in the library")                 

    def show_books(self):
         if not self.books :
              print("there is no book in the library")
         else:
              number = 0
         for book in self.books:
              number+=1
              print(f"{number}- {book["title"]} by {book["author"]}")
              
if __name__ == "__main__":
    print("you should run me as a package")              
         
                   