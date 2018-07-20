#Odds On Game
import random

def getInteger(message):
    while(True):
        inputText = input(message)
        try:
            inputInt = int(inputText)
            if inputInt < 1:
                raise ValueError
            return inputInt
        except ValueError:
            print("PLEASE ENTER A POSITIVE INTEGER")

def getOddsChoice(message, odds):
    while(True):
        inputInt = getInteger(message)
        if inputInt <= odds:
            return inputInt
        else:
            print("MUST BE NO GREATER THAN MAX OF ODDS RANGE")

odds = getInteger("Enter max value of your odds range: ")

computerChoice = random.randint(0,odds)
userChoice = getOddsChoice("Enter your choice of odds: ", odds)

if computerChoice==userChoice:
    print("MATCH")
else:
    print("MISMATCH")
    
print("Computer's choice = " + str(computerChoice))
print("Your choice = " + str(userChoice))    
    
