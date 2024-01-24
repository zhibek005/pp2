# tp 1 - syntax

if 5 > 2:
  print("Five is greater than two!")

# tp 3 - variables

x = str(3)    # x -> '3'
y = int(3)    # y -> 3
z = float(3)  # z -> 3.0

# Illegal variable:

2myvar = "John"
my-var = "John"
my var = "John"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# tp 4 - data types

x = 1    -> int
y = 2.8  -> float
z = 1j   -> complex

x = str("s1")     x -> 's1'
y = int(2.8)      y -> 2
z = float("3")    z -> 3.0

# tp 6 - string

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip()) -> "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) -> ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))