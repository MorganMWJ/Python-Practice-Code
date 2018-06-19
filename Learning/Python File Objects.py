#Python File Object

outputFile = open('filename','w')
#first parameter of open is the filename
#second is the processing mode
#
#    'w' - write
#    'a' - append
#    'r' - read
#
# 'r' is the defualt processing mode if none is given
readFile = open('filename')

readFile.read() #puts all file into one string
readFile.read(N) #Reads up to next N characters into one string
readFile.readLine() #reads next line including the \n
readFIle.readlines() #reads all lines into a list each member being a line from the file

outputFile.write(astring) #writes chars or bytes to the file
output.writeLines(alist) #writes all strings in a list to the file

#file iterators to read line by line
for line in open('filename'):
   #do something to each line  

