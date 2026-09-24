class student():
    def __init__(self, names, ages):
        self.name = names
        self.age = ages

x = student("asal", 20)
appelle = x.name
age = x.age

print(f"the student's name is {appelle} and the student is {age} years old")