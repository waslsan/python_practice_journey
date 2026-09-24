class rectangle ():
    def __init__(self,width,length):
        self.w = width
        self.l = length

    def area(self):
        a = self.w * self.l
        return a

x = rectangle(3,5)
print(f"your rectangle's area with {x.l} length and {x.w} width is {x.area()}")        