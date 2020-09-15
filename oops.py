class number:
    count = 0
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        number.count += 1
    def Sum(self):
        print("{}+{}={}".format(self.num1, self.num2, self.num1 + self.num2))
    @classmethod
    def Countfun(cls):
        print("objects Counted are {}".format(cls.count))

add1 = number(10, 12)
add2 = number(20,30)
add3 = number(100, 200)
add4 = number(10000,20000)
number.Countfun()

