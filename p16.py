Python Function Theory
# 1. Utilizing built-in functions
# Python provides many built-in functions like len(), max(), min(), sum(), type(), range(), etc.


# numbers = [3, 5, 7]
# print(len(numbers)) 
# print(sum(numbers))

# 2. Creating user-defined functions (UDF)
# Defined using def keyword.

# def greet(name):
#   print(f"I am, Alexa!")
#   print(f"Hi, {name}")
#   print(20 + 20)

# greet("Zeel")
# greet("Alice")


# def sum(x , y):
#   print(x + y)

# sum(10 , 20)

# def expontiationss(x , y):
#   print(x ** y)

# expontiationss(2 , 5)

# z = sum(100 , 200)

# print("Sum :" , z)

# 3. Using *args, kwargs, and doc

# *args allows variable number of positional arguments.

# **kwargs allows variable number of keyword arguments.

# __doc__ stores function documentation.

def example_func(a, b, c , *args, **kwargs):
    """This is an example function"""
    print(a, b , c)
    print(args)
    print(kwargs)

example_func(1, 2, 3, x = 4, y = 5, z = 6)
print(example_func.__doc__)

# 4. Implementing function recursion

# A function calling itself is recursion.

# Used in factorial, fibonacci, tree traversal, etc.

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print("factorial :" , factorial(6)) 

# 5. Applying lambda (anonymous) functions

# lambda creates small, anonymous functions.

# Syntax: lambda arguments : expression

# square = lambda x: x**3
# print(square(10))  

# 6. Using the global keyword

# Used to modify global variables inside a function.


# x = 10
# y = 20

# def change():
#     global x
#     x = 20
#     y = 10

# change()
# print(x)  
# print(y)  

# 7. Returning multiple values

# Functions can return multiple values as tuples.

def operations(a, b):
    return [a+b, a-b, a*b, a/b , a ** b]

add, sub, mul, div , exp = operations(10, 2)

print(add, sub, mul, div , exp)

# 8. Sorting and transforming list-based data collections

# sorted() returns a new sorted list.

# list.sort() sorts in place.

# map() applies a function to all items.

nums = [5, 2, 9, 1]
# print(sorted(nums))  # [1, 2, 5, 9]

# nums.sort()
# print(nums)  # [1, 2, 5, 9]

# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 25, 81]