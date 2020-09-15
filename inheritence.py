class triangle():
    def __init__(self,a,b,c):
        self.side1 = a
        self.side2 = b
        self.side3 = c
    def perimeter(self):
        p = self.side1+self.side2+self.side3
        print("perimeter of triangle is {}".format(p))
        return

#===============================================================
class RightAngledTriangle(triangle):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        self.side1 = a
        self.side2 = b
        self.side3 = c

t= triangle(10,20,30)
t.perimeter()

rat = RightAngledTriangle(10,80, 50)
rat.perimeter()