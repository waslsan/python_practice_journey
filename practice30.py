main_number = int(input("enter a number"))

def check_number (f):
    if main_number % 2 == 0 :
        f()
    else:
        print("this number is odd")

@check_number
def show_number ():
    print (main_number)           
