import sys

#sys.path = the list of places python looks in order to find imports
#sys.version = curretn version of python
#sys.maxint =maxiumum interger that can be stored
#sys.platform = platform/os python is running on = 'win32'
############################################################################
def reverse(string):
     reversedString=''
     for x in range(1,len(string)+1):
          reversedString = reversedString + string[-1*x]
     return reversedString

def shortScriptName(longName):
     reverseLongName = reverse(longName)
     reverseShortName=''
     for letter in reverseLongName:
          if letter == '/' or letter == '\\': #on cmd it uses backslash '\' but py interpreter uses '/' forwardslash
               break
          reverseShortName = reverseShortName + letter
     return reverse(reverseShortName)
############################################################################
if sys.platform[:3]=='win':
     print("Hello Windows User\n")

total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)

# Pharsing args one by one 
print ("Script name: %s" % shortScriptName(sys.argv[0]))
for x in range(1,total):
     print ("No. " + str(x) + " argument: %s" % str(sys.argv[x]))
     
