# print your name 

# print("Hello,my name is taxil")

 # aske name and print 

# name = input("What is your name:")
# print("Nice to meet you,",name)

# 3 sum of two numbber 

# a=10
# b=20
# sum = a + b
# print('This sum is:',sum)

# simple calculator

# a =int(input("Enter fist Number :"))
# b =int(input("Enter second Number :"))

# print("addition:", a + b)
# print("substraction:", a - b)
# print("multiplication:", a * b)
# print("division:", a / b)


# 5.sndwich make 

# bread = input("Choose Your bread (white/brown)")

# filling = input("Choose Your filling (cheese / jam /potato / banana)")

# print("Here you silly sandwich:🥪")
# print(" [ " + bread + " bread" + filling + " rainbow silly sandwich 🌈" + " ] ")

# 6. rock ,paper and scissors game

import random

chocies = ["rock" , "paper" , "scissor"]
computer = random.choice(chocies)
player = input("choose rock , paper and scissors:")
 
if (player == computer):
    print("🤣  it's a tie!!!")
elif (player == "rock" and computer == "scissors") or \
(player == "paper" and computer == "rock") or \
(player == "scissors" and computer == "paper"):
    print("🎉 you win......")
else:
    print("🎉 computer win.....")