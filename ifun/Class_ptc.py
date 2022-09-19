class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Initial name testing...{self.name}")
    def talk(self):
        print(f"Talk testing...{self.name}")


person1 = Person("Leo Lee")
person1.talk()
print(person1.name)
person2 = Person("Stima")
person2.talk()
print(person2.name)
oeso = Person("oeso corp")
print(oeso.name)
oeso.talk()