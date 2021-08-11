#!/usr/bin/env python
# coding: utf-8

# # Project 2.0 Rock, Paper, Scissor
# 
# Rock crushes scissor
# Paper wraps rock
# scissor cuts paper

# In[17]:


import random

moveList = ["rock", "paper", "scissor"]
machineChoice = random.choice(moveList)
print(machineChoice)
userChoice = str(input("Choose from rock, paper, scissor: ").lower())
print(userChoice)


# In[18]:


userPoints = 0
machinePoints = 0

if (userChoice == machineChoice):
    print("No one scored. It's a tie")
elif (userChoice == "rock"):
    if (machineChoice == "scissor"):
        userPoints = userPoints + 1
        print("You win as rock crushed the scissor, your scored {score}".format(score = userPoints))
    elif (machineChoice == "paper"):
        machinePoints = machinePoints + 1
        print("You lose, paper wrapped rock, machine scored {score}".format(score = machinePoints))
elif (userChoice == "paper"):
    if (machineChoice == "scissor"):
        machinePoints = machinePoints + 1
        print("You lose as scissor cuts the paper, machine scored {score}".format(score = machinePoints))
    elif (machineChoice == "rock"):
        userPoints = userPoints + 1
        print("You win, paper wrapped rock, you scored {score}".format(score = userPoints))
elif (userChoice == "scissor"):
    if (machineChoice == "paper"):
        userPoints = userPoints + 1
        print("You win, scissor cuts paper, you scored {score}".format(score = userPoints))
    elif (machineChoice == "rock"):
        machinePoints = machinePoints + 1
        print("You lose as rock crushed the scissor, machine scored {score}".format(score = machinePoints))

print(userPoints)
print(machinePoints)


# In[19]:


if (userPoints > machinePoints):
    print("BINGO, You won")
elif (userPoints < machinePoints):
    print("Oh no, Good luck next time!")
else:
    print("It's a tie")


# In[ ]:




