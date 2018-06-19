import os, sys

location = "C:/Users/Morgan/Documents/Programming/Python Code/"


def chooseProgram(prompt, programNumber):
     x = 0
     while True:
          x = input(prompt)
          if int(x) in range(1,programNumber):
               return int(x)
          
while True:
     #Make sure we are in the correct directory
     if os.getcwd()!=location:
          os.chdir(location)
     
     #Get a the names of all programs in the directory
     programList = os.listdir(location)

     #remove anything other than python programs

     for item in programList:
          if not item.endswith('.py'):
               programList.remove(item)
          
     #Display the list, (first number the items in it)
     programDisplayList = zip(range(1,len(programList)+1),programList)
	 
     print(('*'*80) + "\nHere are all the currently available python programs:\n")

     for program in programDisplayList:
          print (str(program[0]) + ": " + program[1] + "\n")

     choice = chooseProgram("Please choose which number program to start: ", len(programList)+1)
     print("Launching program [" + str(choice) + "]:")
     print(('*'*80))
     #print(location + programList[choice-1] + "\n")
     os.system('\"' + programList[choice-1] + '\"')
     #^ windows cmd needs quotes around names with whitespace



###Notes on OS######
#os.startfile(programOfUserChoice)
#os.mkdir()
#os.rmdir()

##for wndows
#'start "programName"' will open the file/folder/program in a new window
