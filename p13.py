#  Part : 1 Use of Built-in Function in Python

import random

# import the random module to generate random number later.

print("<==== Built-in Function on List  ====>")

numbers = [4 , 2 , 7 , 9 , 5 , 6]

print("List : " , numbers)

#  len()

# a list named number is defined with 5 integers

#  len() return the number of items in the list

print("Length of List : " , len(numbers))

# max() and min( are ) used to find the largest and smallest numbers respectively.

print("Max  Number : " , max(numbers))

print("Min Number : " , min(numbers))

# sum() adds all values in the list

print("Sum of List : " , sum(numbers))

# part:2 Nagative float number operation

print("<==== Part:2  Operation in Nagative value ====>")

num = float(input("Enter a Negative float Number : "))

# abs() return the positive version from the user

print("Positive Version From The user : " , abs(num))

# pow() raises the positive value of the power

print("power of value : " , pow(num , 10))

#  round() round of the number to 2 digit after the decimal point

print("Roundof Value : " , round(num))

# part:3 rand List and Its Values / Analysis

print("<=== Random List and Its Values / Analysis ===>")

random_num = random.sample(range(1 , 100) , 5)

print(random_num)

# using max() , and min() , sum() in random value

print("Random List: " , random_num)

print ("Random Number max count: " , max(random_num))
print ("Random Number min count: " , min(random_num))
print ("Random Number sum count: " , sum(random_num))

# Part:4 Sort and Reverse a List

print("<=== Sort and Reverse a List ==>")

user_list = list(map(int , input("Enter Number seperated by space : ").split()))

print(user_list)

# sorted() the original user inputs

# reverse() return a reverse iterator , and list convert in back to a list

print("Sorted List Ascending" , sorted(user_list))

# print("Sorted List Descending" , sorted(user_list , reverse=True))

print("Reverse value of List : " , list(reversed(user_list)) )