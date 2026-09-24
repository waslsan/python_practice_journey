class vehicle ():
    def __init__(self,brand,model):
        self.brand = brand
        self.model =model

    def start (self):
        return("vehicle is starting")   

class car(vehicle):
    def __init__(self, brand, model,doors):
        super().__init__(brand, model)  
        self.door = doors

x = car("toyota", "corolla", 4)
print(f"the vehicle is a {x.brand} {x.model} and has {x.door} doors")
print(x.start())           
        