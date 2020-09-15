def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    return a/b
def module(a,b):
    return a%b
def default():
    print("Enter correct values")

switcher = {
    1.addition(),
    2.subtraction(),
    3.mul(),
    4.division(),
    5.module()
}
def switch(a,b,option):
    return switcher.get(option, default)(a,b)

a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
choice = int(input("Enter your choice...."))
print(switch(a,b,choice))