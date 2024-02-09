# 1

print("How many grams?")
a = float(input())
def converGramsToOunces(d):
    o = 28.3495231 * d
    print(o)

converGramsToOunces(a)

# 2

print("How many Fahrenheit?")
a = float(input())

def convertF(F):
    C = (5 / 9) * (F - 32)
    print(C)

convertF(a)

# 3

h=35
l=94

def solve(nh, nl):
    rabbits = (nl-2*nh)/2
    chickens = nh-rabbits
    print(int(rabbits), int(chickens))
    
solve(h, l)

# 4

stroke = input()
list = list(stroke.split(" "))
primelist = []
def filter_prime(s):
    global primelist
    n=int(s)
    if int(n) > 1:
        for i in range(2,int(n/2)+1):
            if (n%i) == 0:
                break
        else:
            primelist.append(n)
    
for x in list:
    filter_prime(x)
print(primelist)

# 5

s = input("Enter a string: ")
slist = list(s)

def permutations(stroke, index=0):
    if index == len(stroke) - 1:
        print(''.join(stroke))
    else:
        for i in range(index, len(stroke)):
            # Swap 
            stroke[index], stroke[i] = stroke[i],stroke[index]
            # Recursive for checking next index
            permutations(stroke, index + 1)
            # Swap back to check other order
            stroke[index], stroke[i] = stroke[i], stroke[index]

permutations(slist)

# 6

s=input()

def fureverse(fs):
    slist=list(fs.split(" "))
    slist.reverse()
    print(' '.join(slist))

fureverse(s)

# 7

s=input()
nums = [int(num) for num in s.split()]

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            print("True")
            return
        
    print("False")
                    
has_33(nums)

# 8 

def spy_game(nums):
    sequence_position = 0
    for num in nums:
        if sequence_position == 0 and num == 0:
            sequence_position += 1
        elif sequence_position == 1 and num == 0:
            sequence_position += 1
        elif sequence_position == 2 and num == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))

# 9

import math
def volumeSphere(r):
    V=float(4/3*math.pi*pow(r,3))
    print(V)

r=float(input())
volumeSphere(r)

# 10

def unique(nums):
    newl=[]
    for i in nums:
            if i not in newl:
                newl.append(i)         
    return newl
        
nums=[1,2, 3,2,4,4,5]
print(unique(nums))

# 11

def palindrome(st):
    n=len(st)
    for i in range(int((n-1)/2)):
            if st[i]!=st[n-i-1]:
                return False
    return True     
    

        
st="madam"
print(palindrome(st))

# 12

def histogram(nums):
    for x in nums:
        print("*"*x)
        
nums=[4,9,7]
histogram(nums)

# 13

import random
def game():
    
    print("Hello! What is your name?")
    name=input()
    rn=random.randint(1,20)
    cn=0
    ng=0
    print("Well, "+name+ ", I am thinking of a number between 1 and 20. Take a guess.")
    while ng!=rn:
        ng=int(input())
        if ng==rn:
            print("Good job,"+name+"! You guessed my number in ",cn+1," guesses!")
        
        elif ng<rn and ng>0:
            cn+=1
            print("Your guess is too low. Take a guess.")
        elif ng>rn and ng<21:
            cn+=1
            print("Your guess is too high. Take a guess.")
        else:
            print("Some error!!!!!!")

game()