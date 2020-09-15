class car:
    def __init__(self, a=1000):
        self._speed = a
    def get_speed(self):
        return self._speed

    def set_speed(self, a):
        if a not in range(500,1001):
            print("it should be in between 500 and 1001")
        else:
            self._speed = a

    speed = property(get_speed, set_speed)

m = car()
print(m.speed)

# print(m.speed)
