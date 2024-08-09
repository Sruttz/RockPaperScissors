rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#rock = 0
#paper = 1
#scissor = 2
import random

user_input= int(input("enter 0 for rock, 1 for paper and 2 for scissors : "))
comp_input = random.randint(0,2)

if comp_input==0:
    if user_input==0:
        print("your have chosen rock\n", rock)
        print("computer choice is\n", rock)
        print("DRAW")
    if user_input==1:
        print("your have chosen paper\n", paper)
        print("computer choice is\n", rock)
        print("YOU WIN")
    if user_input==2:
        print("your have chosen scissors\n", scissors)
        print("computer choice is\n", rock)
        print("YOU LOSE")

if comp_input==1:
    if user_input==0:
        print("your have chosen rock\n", rock)
        print("computer choice is\n", paper)
        print("YOU LOSE")
    if user_input==1:
        print("your have chosen paper\n", paper)
        print("computer choice is\n", paper)
        print("DRAW")
    if user_input==2:
        print("your have chosen scissors\n", scissors)
        print("computer choice is\n", paper)
        print("YOU WIN")

if comp_input==2:
    if user_input==0:
        print("your have chosen rock\n", rock)
        print("computer choice is\n", scissors)
        print("YOU WIN")
    if user_input==1:
        print("your have chosen paper\n", paper)
        print("computer choice is\n", scissors)
        print("YOU LOSE")
    if user_input==2:
        print("your have chosen scissors\n", scissors)
        print("computer choice is\n", scissors)
        print("DRAW")
