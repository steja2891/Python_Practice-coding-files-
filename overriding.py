class College():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.sal = salary

    def Biodata(self):
        print("name of {} of age {} having {}".format(self.name, self.age, self.sal))
        return

class Student(College):
    def __init__(self,name,age,exp,sal=None):
        super().__init__(name,age,sal)
        self.exp = exp
    def Biodata(self):
        print("name of {} of age {} having {} experience".format(self.name, self.age, self.exp))
        return

class Faculty(College):
    def __init__(self,name,age,exp,sal):
        super().__init__(name,age,sal)
        self.exp  =exp

    def Biodata(self):
        print("name of {} of aged {} having {} experience. His salary is {}".format(self.name, self.age, self.exp,self.sal))
        return

c = College("Ashok",40,12000)
c.Biodata()

s = Student("Saiteja",20, 2)
s.Biodata()

f = Faculty("Sunil", 35, 10, 1000000)
f.Biodata()