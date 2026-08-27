#1
names = ["asal", "saman", "ali", "sara"]
print(f"the list is {names}")
names[0]="Ava"
print(f"after the change the list is {names}")

#2
numbers = [5,2,8,1,9,3]
numbers.append(10)
numbers.sort()
numbers.pop()
print(numbers)
print(f"there is {numbers.count(2)} 2 in the list")

#3
my_dict={"name":"asal", "age":20, "scores":{"math":18, "physics":15, "programming":20}}
print(f"student's name is {my_dict['name']}")
print(f"the student's score in physics is {my_dict['scores']['physics']}")
my_dict["scores"]["programming"]=19
my_dict["city"]= "shiraz"
print(my_dict)

#4
numbers = [12, 7, 3, 18, 21, 4, 10, 15]
zoj = []
fard = []
for i in numbers :
    if i%2 == 0 :
        zoj.append(i)
    else:
        fard.append(i)

zoj.sort()
fard.sort()

print(f"zoj numbers: {zoj}")
print(f"fard numbers: {fard}")    

#5
scores = [12, 18, 9, 20, 15, 7, 19]
passed = []
failed = []
for i in scores :
    if i >= 10 :
        passed.append(i)
    else:
        failed.append(i)

print(f"you have passed {len(passed)} courses")   

#6
text = "i love python"
print(f"length of the text is {len(text)}")
print(f"the first letter of the text is {text[0]}")
print(f"the last letter of the text is {text[-1]}")
print(f"backwards of the text is: {text[::-1]}")
text = text + " and i want to learn python"
print(text)

#7
text2 = "python is a very interesting language"
print(text2[0:6])
print(text2[-8:])
print(f"there is {text2.count("i")} i in the text")
if "python" in text2:
    print("there is python in the text")
else:
    print("there is not python in the text")    
text2 = "Java" + text2[6:]
print(text2)
print(text2.upper())
print(text2.lower())

#8
students = [("Asal",19),("saman",20),("sara",17),("ali",14),("zahra",8)]
for name,score in students:
    if score >= 18 :
        print(f"{name}: Excellent")
    elif 10<=score<=17 :
        print(f"{name}:Passed")
    else :
        print(f"{name}:Failed")        



       


