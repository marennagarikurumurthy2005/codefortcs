#  what is python
#  python is a dynamically typed , interpreted , easy oops suported etc 
# variable :- var are the containers used to store the values Naming rules etc
# data types : which type of data is stored in the variable 
# a=10
# b="10"
# Operators aithmetic , logical , assignment , membership (in not in) bitwise operator
# ?conditional statemsnts
# switch case using match key word
#  loops
# functions


# ============================================================
# PYTHON FUNDAMENTALS TO DSA - COMPLETE REVISION SHEET
# ============================================================

# ============================================================
# 1. ABOUT PYTHON
# ============================================================

"""
Python is a:
1. High-level language
2. Interpreted language
3. Object-Oriented language
4. Dynamically Typed language
5. Platform Independent language

Features:
- Easy syntax
- Huge libraries
- Automatic memory management
- Cross-platform
- Open source
"""

print("Hello World")

# Output:
# Hello World


# ============================================================
# 2. VARIABLES
# ============================================================

"""
Variable:
A named memory location used to store data.
"""

name = "MK"
age = 21
salary = 50000

print(name)
print(age)
print(salary)

# Output:
# MK
# 21
# 50000


# Multiple Assignment

a,b,c = 10,20,30
print(a,b,c)

# Output:
# 10 20 30


# Dynamic Typing

x = 10
print(type(x))

x = "Python"
print(type(x))

# Output:
# <class 'int'>
# <class 'str'>


# ============================================================
# 3. DATA TYPES
# ============================================================

"""
Primitive:
int
float
complex
bool
str

Non Primitive:
list
tuple
set
dict
"""

# Integer

a = 10
print(type(a))

# Float

b = 10.5
print(type(b))

# Complex

c = 3 + 4j
print(type(c))

# Boolean

d = True
print(type(d))

# String

e = "Python"
print(type(e))


# ============================================================
# 4. OPERATORS
# ============================================================

# Arithmetic

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Output:
# 13
# 7
# 30
# 3.333
# 3
# 1
# 1000


# Comparison

print(a>b)
print(a<b)
print(a==b)

# Output:
# True
# False
# False


# Logical

print(True and False)
print(True or False)
print(not True)

# Output:
# False
# True
# False


# Membership

name = "Python"

print("P" in name)

# Output:
# True


# Identity

x = [1,2]
y = x

print(x is y)

# Output:
# True


# ============================================================
# 5. CONDITIONAL STATEMENTS
# ============================================================

age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Output:
# Eligible


marks = 80

if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("C")

# Output:
# B


# ============================================================
# 6. MATCH CASE (SWITCH)
# ============================================================

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")

# Output:
# Tuesday


# ============================================================
# 7. LOOPS
# ============================================================

# For Loop

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# While Loop

i = 1

while i <= 5:
    print(i)
    i += 1


# Break

for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0 1 2 3 4


# Continue

for i in range(5):
    if i == 2:
        continue
    print(i)

# Output:
# 0 1 3 4


# Pass

for i in range(5):
    pass


# ============================================================
# 8. FUNCTIONS
# ============================================================

def greet():
    print("Hello")

greet()

# Output:
# Hello


# Parameters

def add(a,b):
    return a+b

print(add(10,20))

# Output:
# 30


# Default Arguments

def show(name="MK"):
    print(name)

show()

# Output:
# MK


# *args

def total(*nums):
    print(sum(nums))

total(10,20,30)

# Output:
# 60


# **kwargs

def details(**data):
    print(data)

details(name="MK", age=21)

# Output:
# {'name': 'MK', 'age': 21}


# ============================================================
# 9. VARIABLE SCOPE
# ============================================================

x = 100

def demo():
    x = 50
    print(x)

demo()
print(x)

# Output:
# 50
# 100


# Global Keyword

x = 10

def change():
    global x
    x = 20

change()

print(x)

# Output:
# 20


# ============================================================
# 10. STRINGS
# ============================================================

s = "Python"

print(s[0])
print(s[-1])

# Output:
# P
# n


print(s[0:4])

# Output:
# Pyth


print(s.upper())
print(s.lower())
print(s.replace("Python","Java"))

# Output:
# PYTHON
# python
# Java


print(len(s))

# Output:
# 6


# ============================================================
# 11. LIST
# ============================================================

nums = [10,20,30]

nums.append(40)
nums.insert(1,15)

print(nums)

# Output:
# [10,15,20,30,40]


nums.remove(20)

print(nums)

# Output:
# [10,15,30,40]


nums.pop()

print(nums)

# Output:
# [10,15,30]


nums.reverse()
print(nums)

# Output:
# [30,15,10]


# ============================================================
# 12. TUPLE
# ============================================================

t = (10,20,30,20)

print(t.count(20))
print(t.index(30))

# Output:
# 2
# 2


# ============================================================
# 13. SET
# ============================================================

s = {1,2,3}

s.add(4)

print(s)

# remove()

s.remove(2)

print(s)

# union

a = {1,2}
b = {2,3}

print(a.union(b))

# Output:
# {1,2,3}


# intersection

print(a.intersection(b))

# Output:
# {2}


# ============================================================
# 14. DICTIONARY
# ============================================================

student = {
    "name":"MK",
    "age":21
}

print(student["name"])

# Output:
# MK


student["city"] = "Hyderabad"

print(student)

# keys

print(student.keys())

# values

print(student.values())

# items

print(student.items())


# ============================================================
# 15. LIST COMPREHENSION
# ============================================================

nums = [i for i in range(1,6)]

print(nums)

# Output:
# [1,2,3,4,5]


squares = [i*i for i in range(1,6)]

print(squares)

# Output:
# [1,4,9,16,25]


# ============================================================
# 16. ENUMERATE
# ============================================================

names = ["MK","RK","VK"]

for index,value in enumerate(names):
    print(index,value)

# Output:
# 0 MK
# 1 RK
# 2 VK


# ============================================================
# 17. ZIP
# ============================================================

names = ["MK","RK"]
ages = [21,22]

for n,a in zip(names,ages):
    print(n,a)

# Output:
# MK 21
# RK 22


# ============================================================
# 18. SORTING
# ============================================================

nums = [4,2,1,5,3]

nums.sort()

print(nums)

# Output:
# [1,2,3,4,5]


nums.sort(reverse=True)

print(nums)

# Output:
# [5,4,3,2,1]


# ============================================================
# 19. RECURSION
# ============================================================

def fact(n):

    if n == 1:
        return 1

    return n * fact(n-1)

print(fact(5))

# Output:
# 120


# ============================================================
# 20. FACTORIAL
# ============================================================

n = 5

fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)

# Output:
# 120


# ============================================================
# 21. PRIME NUMBER
# ============================================================

n = 7

flag = True

for i in range(2,n):
    if n % i == 0:
        flag = False

print(flag)

# Output:
# True


# ============================================================
# 22. PALINDROME
# ============================================================

s = "madam"

print(s == s[::-1])

# Output:
# True


# ============================================================
# 23. FIBONACCI
# ============================================================

a,b = 0,1

for i in range(10):
    print(a,end=" ")
    a,b = b,a+b

# Output:
# 0 1 1 2 3 5 8 13 21 34


# ============================================================
# 24. OOPS
# ============================================================

class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

s1 = Student("MK")
s1.display()

# Output:
# MK


# ============================================================
# 25. INHERITANCE
# ============================================================

class Parent:

    def show(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.show()

# Output:
# Parent


# ============================================================
# 26. EXCEPTION HANDLING
# ============================================================

try:
    print(10/0)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Completed")

# Output:
# Cannot divide by zero
# Completed


# ============================================================
# END OF PYTHON REVISION SHEET
# ============================================================

# inp="abc"
# arr=[]

# print("Problem")

# arr=[]
# def sol(inp,ans):
#     if len(inp)==0:
#         return arr.append(ans)
#     for i in range(len(inp)):
#         ch=inp[i]
#         left=inp[:i]
#         right=inp[i+1:]
#         remaining=left+right
#         # print(ch,"-",left,"-",right,"-",remaining)
#         # print(ans+ch)
#         sol(remaining,ans+ch)
# sol("abc","")
# print(arr)
# 
# 
# 
# 
# 
