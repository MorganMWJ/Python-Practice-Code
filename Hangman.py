#Hangman Program
from random import*

wordBank = ["diplomacy", "hairdressing", "inspirer", "electrically", "physics", "art", "career", "freedom", "hello", "elephant", "fearless", "colorado", "computer", "grandfather", "decadent", "command", "moisturiser"]
#############################################
def checkSure(prompt):
     choice = input(prompt).lower()
     while choice not in ['y','yes',"n",'no']:
          choice = input(prompt + "(yes/no)").lower()
     if choice in ['n','no']:
          return False
     else:
          return True
############################################
def getGuess(prompt):
     while True:
          letter = input(prompt)
          if len(letter)==1:
               return letter.lower()
          else:
               print("Incorrect Input")
##############################################
def wholeGuess(wordToMatch):
     guess = input("Enter the whole word guess: ").lower()
     if guess==wordToMatch:
          print("Exact word match!\n***You won hangman, Congradulations!***\n")
          return True
     else:
          return False
##############################################
def updateGuessStatus(letterToDisplay, currentDisplay, fullWord):
     display = list(currentDisplay)
     indexes = []
     positionOfCurrentLetter = 0
     for currentLetter in fullWord:#get all the positions of a particular letter in a word
          if letterToDisplay==currentLetter:
               indexes.append(positionOfCurrentLetter)
          positionOfCurrentLetter += 1

     for letterPosition in indexes:#display the letter at all the posistions found
          display[letterPosition] = letterToDisplay
     return ''.join(display)
##############################################
#Main code
def hangmanCode():
     
     chosenWord = wordBank[randint(0,len(wordBank)-1)]
     guessList = []#to keep all the guesses stored for reference
     guessStatus = ""#to display all correct guesses
     for item in chosenWord:
          guessStatus = guessStatus + "-"
     guessesLeft = 12
     notWarned = True

     print('\n' + guessStatus)
     while guessesLeft > 0 and guessStatus!=chosenWord:
          
          #if guessStatus.count("-") > guessesLeft and notWarned:
           #    notWarned = False
            #   if checkSure("WARNING\nYou have less guesses left than spaces do you want to start a new game?"):
             #       return
               
          print("You have " + str(guessesLeft) + " guesses left.")
          newLetter = getGuess("Enter a single letter: ")

          if newLetter=='!':#option for a whole guess
               if wholeGuess(chosenWord):
                    return
          
          if newLetter in guessList:
               print("You have already guessed: " + str(newLetter))
               #do not peanalies for repeat guesses of the same letter
          else:
               guessList.append(newLetter)
               guessesLeft -= 1
               if newLetter in chosenWord:
                    guessStatus = updateGuessStatus(newLetter, guessStatus, chosenWord)
                    print("Correct Guess!")
               else:
                    print("Incorrect Guess!")

          print(guessStatus + '\n')     
          
          
          
     if guessStatus==chosenWord:
          print("***You won hangman, Congradulations!***\n")
     else:
          print("---You lost hangman---\n")

#############################################
print("Welcome to the Hangman Program\n[Type '!' to guess the whole word]")
while checkSure("Do you want to play a game of Hangman?"):
     hangmanCode()
print("Exiting Hangman Program")
