#Dice Rolling Program

from random import *

def diceRoll():
     return randint(1,6)
#######################################################
def rollAgain(prompt):
     choice = input(prompt).lower()
     while choice not in ['y','yes',"n",'no']:
          choice = input(prompt + "(yes/no)").lower()
     if choice in ['n','no']:
          return False
     else:
          return True
#######################################################     
wantsToRoll = True
while wantsToRoll:
     if rollAgain("Would you like to roll the dice?"):
          print("You rolled a: " + str(diceRoll()))
     else:
          wantsToRoll = False
          
print("Exiting Dice Rolling Program")
