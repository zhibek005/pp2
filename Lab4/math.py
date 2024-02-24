import math

#1
a = int(input("Enter an angle in degrees: "))

def d_to_r(deg):
    rad = math.radians(deg)
    print("Angle in radians:", rad)

d_to_r(a)

#2
h = int(input("Height: "))
b1 = int(input("Base1: "))
b2 = int(input("Base2: "))

def trap_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    print("Area of the trapezoid:", area)

trap_area(h, b1, b2)

#3
n = int(input("Number of sides: "))
l = int(input("Length of a side: "))

def poly_area(sides, length):
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
    print("Area of the polygon:", area)

poly_area(n, l)

#4
b = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))

def para_area(base, height):
    area = base * height
    print("Area of the parallelogram:", area)

para_area(b, h)
