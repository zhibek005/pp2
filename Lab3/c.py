import math

# 1
class MyClass:

    def getString(self):
        str = input("enter some str")
        return str

    def printString(self, str):
        print(str)


x = MyClass()
string = x.getString()
x.printString(string)


# 2
class Shape():

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


shape = Shape()
print(shape.area())

square = Square(4)
print(square.area())


# 3
class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


rectangle = Rectangle(3, 5)
print(rectangle.area())


# 4
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"coordinates: {self.x}, {self.y}")

    def move(self, newX, newY):
        self.x = newX
        self.y = newY
        print(f"new coordinates: {self.x}, {self.y}")

    def dist(self, secondPoint):
        distanceX = secondPoint.x - self.x
        distanceY = secondPoint.y - self.y
        distance = round(math.sqrt(distanceX**2 + distanceY**2))
        print(f"distance: {distance}")


point1 = Point(2, 6)
point2 = Point(4, 7)

point1.show()
point1.move(3, 5)
point1.dist(point2)


# 5
class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(
                f"Withdrawals may not exceed the available balance. Your balance: {self.balance}"
            )
        else:
            self.balance -= amount
            print(f"Your balance: {self.balance}")


account1 = Account("Zhibek", 5000)

account1.deposit(200)
account1.withdraw(1500)

account2 = Account("Tima")

account2.deposit(800)
account2.withdraw(1500)

# 6
nums = list(range(2, 100))

for i in range(2, 10):
    nums = list(filter(lambda x: x == i or x % i != 0, nums))

print(nums)