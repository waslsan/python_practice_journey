from random import randint
win=False

while win == False:
    result=randint(1,6)
    user=int(input("guess the number: "))
    if result!= user:
        print(f"sorry it was {result}")
        continue
    else:
        print("you guessed it right!")
        win=True    
    