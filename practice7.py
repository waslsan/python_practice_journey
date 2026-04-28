def is_positive (x):
    if x%2==0 or x==0:
        return True
    else:
        return False
    
def my_input():
    return int(input("enter a number: "))   

print(is_positive(my_input())) 