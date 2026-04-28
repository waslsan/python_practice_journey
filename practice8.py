def square (x,y):
    sum=(x**2)+(y**2)
    return sum

def my_input():
    first=int(input("enter the first number: "))
   
    return first

def inputtwo ():
 second=int(input("enter the second number: "))
 return second

print(f"sum of your numbrs is {square(my_input(),inputtwo())}")