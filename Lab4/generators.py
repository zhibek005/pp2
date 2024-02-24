#1
n = input().split()
lst = [int(num) for num in n]

def sqr_gen(nums):
    for num in nums:
        yield(num * num)

squared_list = list(sqr_gen(lst))
print(*squared_list)

#2
x = int(input())

def even_gen(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i

for num in even_gen(x):
    print(num)

#3
n = input().split()
lst = [int(num) for num in n]

def divisible_gen(nums):
    for i in range(0, max(nums)):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_gen(lst):
    print(num)

#4
a = int(input())
b = int(input())

def sq_gen(n, m):
    for i in range(n, m):
        yield(i * i)

for num in sq_gen(a, b):
    print(num)

# Exercise 5
x = int(input())

def down_gen(n):
    i = n
    while i != 0:
        i -= 1
        yield i

for num in down_gen(x):
    print(num)
