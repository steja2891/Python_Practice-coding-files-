# To find the simple and compound interest

principal ,rate, year = int(input()),int(input()),int(input())

si = (principal*rate*year)/100
print("{:6f}".format(si))

ci =  principal*(pow((1+rate/100),year)) - principal
print("{:6f}".format(ci))



