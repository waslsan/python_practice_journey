class animal():
    zoo_name = "hayat vahsh"
    def __init__(self,name,species,age,sound):
        self.n = name
        self.s = species
        self.a = age
        self.sound = sound

    def make_sound(self):
        return self.sound  

    def info(self):
        return(f"the animal is a {self.s} its name is {self.n}, it is {self.a} years old and it says {self.sound}") 
    
    def __str__(self):
        return f"{self.n} is a {self.s}"
    
class bird(animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, "bird", age, "coco") 
        self.wing = wing_span  

    def make_sound(self):
        return("coco")


 

x = animal("leo", "lion", 8, "idfkhf")
print(x)
print(x.info())
y = bird("nana", 1, 3)
print(y.info())
       