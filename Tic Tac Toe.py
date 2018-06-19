#Tic Tack Toe

from random import *

#8 possible lines to be made upon winning tic tac toe
winCombinations = [ (6,7,8), (3,4,5), (0,1,2), (6,3,0), (7,4,1), (8,5,2), (0,4,8), (6,4,2) ]
#AI prioity move  encoded game states
#Prioity 1 (if win in one move)
p1Moves = [ (8,[(7,6),(5,2),(4,0)]),
            (7, [(4,1),(6,8)]),
            (6, [(7,8),(3,0),(4,2)]),
            (5, [(8,2),(3,4)]),
            (4, [(8,0),(6,2),(1,7),(3,5)]),
            (3, [(6,0),(4,5)]),
            (2, [(5,8),(1,0),(4,6)]),
            (1, [(0,2),(4,7)]),
            (0, [(4,8),(1,2),(3,6)])]
#######################################################
def playOs(prompt):
     choice = input(prompt + "\n>>>").upper()
     while choice not in ['X','O','OS','XS']:
          choice = input(prompt + "(X/O)\n>>>").upper()
     if choice[0] == 'X':
          return False
     else:
          return True
#######################################################
def yesOrNo(prompt):
     choice = input(prompt + "\n>>>").lower()
     while choice not in['y','yes',"n",'no']:
          choice = input(prompt + "(yes/no)\n>>>").lower()
     if choice in ['n','no']:
          return False
     else:
          return True
#######################################################
def noWinner(board):
     for winCombination in winCombinations:
          if (board[winCombination[0]] == board[winCombination[1]] == board[winCombination[2]]) and (board[winCombination[0]] != ' '):
               return False
     return True
#######################################################
def notStuck(board):
     if ' ' in board:#not stuck
          return True
     else:
          return False     
#######################################################

#NOTE: The computer AI is currently random unless the first move,
     # which is always in the center.

def AIMove(board, sign, enemySign):
     if board.count(' ') == 9:#if empty board
          board[4] = sign#mark the center            
     else:
          #get a list of all empty squares
          tempIndexList = []
          for square in board:
               if square==' ':
                    tempIndexList.append(board.index(square))
          #pick one of the empty squares from the list at random
          board[tempIndexList[randint(0,len(tempIndexList)-1)]] = sign
                    
     return board
#######################################################
def playerMove(prompt, board, sign):
     while True:
          square = getOneToNine(prompt) - 1
          if board[square]==' ':
               board[square] = sign
               return board
          else:
               print("That space is already taken!")
####################################################### 
def getOneToNine(prompt):
     tempInput = ''
     while tempInput not in ['1','2','3','4','5','6','7','8','9']:
          tempInput = input(prompt)
     return int(tempInput)     
#######################################################
def displayBoard(board):
     print('  ' + board[6] + '  |  ' + board[7] + '  |  ' + board[8] + '  ')
     print("-----------------")
     print('  ' + board[3] + '  |  ' + board[4] + '  |  ' + board[5] + '  ')
     print("-----------------")
     print('  ' + board[0] + '  |  ' + board[1] + '  |  ' + board[2] + '  ')
     print("\n")
####################################################### 
def choseWhoStarts():
     x = randint(-1,0)
     if x==-1:
          print("The computer will start.\n")
          return x
     print("The player will start.\n")
     return x
####################################################### 
print("Welcome to the Tic Tac Toe Program\n")

while yesOrNo("Would you like to play a game of Tic Tac Toe?"):
     
     if playOs("Would you like to play O's or X's?"):
          playerSign = 'O'
          computerSign = 'X'
          print("\nYou are playig as O's.")
     else:
          playerSign = 'X'
          computerSign = 'O'
          print("\nYou are playing as X's.")
          
     #main code
     board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     moveCounter = choseWhoStarts()
     while noWinner(board) and notStuck(board):
          moveCounter+=1
          if moveCounter%2==0:
               print("The computer will make a move.")
               board = AIMove(board, computerSign, playerSign)
          else:
               board = playerMove("Please pick an empty square(1-9): ", board, playerSign) 
          displayBoard(board)     
     if notStuck(board) == False:
          print("The game is a draw.\n")
     else:
          if moveCounter%2==0:
               print("The computer wins the game.\n")
          else:
               print("Congradulations, You won Tic Tac Toe.\n")
     
print("Exiting Tic Tac Toe Program")
