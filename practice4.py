number=int(input("enter a number: "))
if number%3==0 and number%5==0:
    print("legendery")
elif number%3==0:
    print("magical")
elif number%5==0:
    print("cursed")
else:
    print("normal")            