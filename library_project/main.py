from my_library import library
from emoji import emojize

print(emojize("hello \n"
    "welcome to the program of this library \n"
    "here's the menu of what you can do on this program :red_heart: \n"
    "1- Add book \n"
    "2- remove book \n"
    "3-search book \n"
    "4-show all books \n"
    "5-exit \n"
    " \n"
    "chose what you want"))


closed = 0 
my_library = library.library()
while closed == 0:
    print(emojize(
    "here's the menu of what you can do on this program :red_heart: \n"
    "1- Add book \n"
    "2- remove book \n"
    "3-search book \n"
    "4-show all books \n"
    "5-exit \n"
    " \n"
    "chose what you want"))
    num = int(input("enter the number of the task: ")) 
    
    if num == 5:
     print("Goodbye!")
     closed=1

    elif num == 1:
     title = str(input("enter the book's title: "))
     author = str(input("enter the book's author: "))
     my_library.add_book(title,author)
     print (emojize("book added successfully :thumbs_up:"))

    elif num == 2:
      title = str(input("enter the title of the book you want to remove: "))
      my_library.remove_book(title)

    elif num == 3:
      title = str(input("enter the title of the book you want to search"))
      my_library.search_book(title)

    elif num == 4:
      my_library.show_books()   
    else:
     print("you chose a wrong number")
