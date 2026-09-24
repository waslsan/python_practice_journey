class animal():
    def __init__(self,name):
        self.name = name

class dog (animal):
    def bark (self):
        return("woof")

x = dog("max")
print(f"my pet's name is {x.name} and says {x.bark()}")            