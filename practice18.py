class circle():
    p = 3.14
    def __init__(self,r):
        self.r = r

    def masahat(self):
        m = self.r * self.r * circle.p
        return m

x = circle(3)
print (f"your circle's area with {x.r} radius is {x.masahat()}")        
        