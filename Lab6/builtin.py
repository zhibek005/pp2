#1
from functools import reduce
l = [1, 2, 3, 4]  
r = reduce(lambda x, y: x*y, l)
print(r)

#2
s = "Hello World"
u = sum(1 for c in s if c.isupper())
l = sum(1 for c in s if c.islower())
print("Upper case:", u, "Lower case:", l)

#3
s = "radar"
p = s == s[::-1]
print(p)

#4
from time import sleep
from math import sqrt
n = 25100  
m = 2123 
sleep(m / 1000) 
r = sqrt(n)
print(f"Square root of {n} after {m} milliseconds is {r}")

#5
t = (True, True, True)
r = all(t)
print(r)
