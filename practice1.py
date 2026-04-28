n=int(input("enter repeats:"))
x=int(input("enter your number:"))
for i in range(n):
    print("hi")
    if x %2!=0:
      x=(x*2)-1
    else:
      x=x/2    
print(x)      
