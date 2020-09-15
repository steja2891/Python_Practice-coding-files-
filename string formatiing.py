number = 2020
a = 12
b = 12
c = a + b
print("Addition is ", c)
# string formatting


#  a   b   c
print("{0}+{1}={2}".format(a, b, c))
print("{1}+{0}={0}".format(c, a, b))
print("{1} equal to {0} plus {2}".format(a, c, b))
a = int(input())
b = int(input())
print("{}+{}={}".format(a, b, a + b))
print('''
jan = {0}
feb = {2}
mar = {0}
apr = {1}
may = {0}
jun = {1}
jul = {0}
aug = {0}
sep = {1}
oct = {0}
nov = {1}
dec = {0}
'''.format(31, 30, 28))
pi = 22 / 7
print("pi value is : {0}".format(22 / 7))
print(f"pi value is : {pi}")
print(f"pi value is : {22 / 7}")
num1 = 10
num2 = 30
print(f"{num1} / {num2} = {num1 / num2}")
