import random

computer_guess=random.randint(1,20)
user_guess=0
count=0

def guess():
    o=int(input("what is your guess? "))
    return o

def win (x,y):
    return x==y

def answer(c,u):
    if c>u:
        return("my number is larger")
    elif u>c:
        return("my number is smaller")
    else:
        return("you wonnn")
    
def finish(num):
    return (f"my number was {num} and you found it with {count} try")    

while not win(computer_guess,user_guess):
    user_guess=guess()
    count+=1
    print(answer(computer_guess,user_guess))  
    if win(computer_guess,user_guess):
        print(finish(computer_guess))            
