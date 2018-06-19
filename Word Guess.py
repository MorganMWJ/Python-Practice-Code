#Fallout hacking program

#import the functionality to choose random numbers
from random import *

###################################################
#function to get a guess from the user that is the same length as the word
def getGuess(message, length):
     validGuess = False
     while(not validGuess):         
          guess = input(message).lower()
          if len(guess) == length:
               validGuess = True
          message = "ERROR guess must be "+ str(length) + " characters long!\n" + message
     return guess
####################################################

#list of possible words the program can choose from come from file
wordFile = open("Resources/wordBank.txt", "r")
wordBank = wordFile.readlines()
wordFile.close()

#pick a random word from the wordBank,
#make it lowercase and then remove its last character (the newline)
chosenWord = wordBank[randint(0,len(wordBank)-1)].lower()[:-1]
chosenWordLength = len(chosenWord)

correctGuess = False
guessCount = 0

while not correctGuess:
     print("The word is " + str(chosenWordLength) + " letters in length.")
     guess = getGuess("Guess a word: ",chosenWordLength)
     if guess==chosenWord:
          correctGuess = True
     else:
          correctPositions = 0
          for pos in range(0,chosenWordLength):
               if guess[pos]==chosenWord[pos]:
                    correctPositions += 1
          print("Incorrect guess. " + str(correctPositions) + " letters are in the correct position.")
          
print("All " + str(len(chosenWord)) + " letters match, You won yey!!!")
     
