class A:
    def __init__(self):
        print("I am A")
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B:
    def __init__(self):
        print("I am B")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("I am C")

    def feature5(self):
        print("Feature 1 is working")

    def feature6(self):
        print("Feature 1 is working")


ob = C()
