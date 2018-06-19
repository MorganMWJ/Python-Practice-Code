import re
'''
Integer Representations

     -Signed Value Representation
     -1's Complement Representation
     -2's Complement Representation
     -Excess Representation
'''
def chopLiteral(binary):
     if binary[0] == '0' and binary[1] == 'b':
          return binary[2:]#excluding '0b'
     elif binary[0] == '-':
          return binary[3:]#excluding '-0b'
     else:
          return binary
#############################################################################################################     
#All the 'B-D' functions take in a string of a binary number. Starting with '0b....'

def signValueBD(binary):
     binary = chopLiteral(binary)
     if binary[0]=='0':
          return int(binary,2)
     else:
          return -1*int(binary[1:],2)#[1:] to discount the sign bit

def excessBD(binary):
     binary = chopLiteral(binary)
     length = len(binary)
     bias = (2**(length-1)) - 1
     return int(binary,2) - bias

#e.g: 1101 = -((1-1)*(2**0) + (1-0)*(2**1) + (1-1)*(2**2)) = -2
def onesCompBD(binary):
     binary = chopLiteral(binary)
     if binary[0]=='0':
          return int(binary,2)
     else:
          inverseBits = ""
          for bit in binary[1:]:
               inverseBits = inverseBits + (str((1 - int(bit))))#take away each bit from one to invert it
          return -1 * int(inverseBits, 2)

def twosCompBD(binary):
     binary = chopLiteral(binary)
     if binary[0]=='0':
          return int(binary,2)
     else:
          inverseBits = [str(1-int(bit)) for bit in binary[1:]]#makes a list of chars using list comprehension
          inverseBits = ''.join(inverseBits)#turns list of chars into a string
          print(inverseBits)
          return -1 * (int(inverseBits,2) + 1)
#############################################################################################################
def signValueDB(decimal):
     if decimal > -1:
          usedBits = len(bin(decimal)) - len("0b")
          filler0s = byteSize - usedBits
          return ('0'*filler0s) + bin(decimal)[2:]
     else:
          usedBits = len(bin(decimal)) - len("-0b") + len("b")
          filler0s = byteSize - usedBits          
          return "1" + ('0'*filler0s) + bin(decimal)[3:]

def excessDB(decimal):
     bias = (2**byteSize)-1
     result = decimal + bias
     return bin(result)[2:] #remove the '0b' at the start of srting

def onesCompDB(decimal):
     if decimal>-1:
          usedBits = len(bin(decimal)) - len('0b')
          filler0s = byteSize - usedBits
          return ('0'*filler0s) + bin(decimal)[2:]
     else:
          bits = bin(decimal)[3:]
          inverseBits = [str(1-int(bit)) for bit in bits]#makes a list of chars using list comprehension
          inverseBits = ''.join(inverseBits)#turns list of chars into a string
          filler1s = byteSize - len(inverseBits)
          return ('1'*filler1s) + inverseBits
          
def twosCompDB(decimal):
     if decimal>-1:
          usedBits = len(bin(decimal)) - len('0b')
          filler0s = byteSize - usedBits
          return ('0'*filler0s) + bin(decimal)[2:]
     else:
          bits = bin(decimal)[3:]#excluding the '-0b'
          inverseBits = [str(1-int(bit)) for bit in bits]#makes a list of chars using list comprehension
          inverseBits = ''.join(inverseBits)#turns list of chars into a string
          filler1s = byteSize - len(inverseBits)
          return bin(int(('1'*filler1s) + inverseBits,2) + 1)[2:]#remove the '0b' 
#############################################################################################################
def choice(prompt,inputs):
     text = input(prompt)
     while text not in inputs:
          text = input("please choose from " + str(inputs) + ":\n")
     return text

def chooseBinary():
     goodInputs = ["binary","bin","b","bi","decimal","dec","d"]
     text = input("Convert from Binary OR Decimal?:").lower()
     while text not in goodInputs:
          print("*INPUT ERROR*")
          text = input("Convert from Binary OR Decimal?:").lower()
     if text[0]=='b':
          return True
     else:
          return False
#############################################################################################################
def getBinaryInput():
     while True:
          text = input("Please enter an " + str(byteSize) + " bit binary number: ")
          #reg exp for string to be binary = ^[01]+$
          if len(text)==byteSize and re.match('^[01]+$',text):
               return text

def getIntegerInput():
     while True:
          text = input("Please enter an integer: ")
          if re.match('^\-?[0-9]+$',text):
               return int(text)

def getByteLength():
     while True:
          text = input("Enter the new byte length: ")
          if re.match('^[0-9]+$',text):
               if int(text) in range(4,17):
                    return int(text)
#############################################################################################################
def printBD(stdin,result):
     print("\nBINARY -> DECIMAL\n" + str(stdin) + " -> " + str(result))
     
def printDB(stdin,result):
     print("\nDECIMAL -> BINARY\n" + str(stdin) + " -> " + str(result))
#############################################################################################################
     
runProgram = True             
byteSize = 8
prompt =  ""
prompt += "Program Functions Menu: \n"
prompt += "1. Signed Value Representation\n"
prompt += "2. 1's Complement representation\n"
prompt += "3. 2's Complement Representation\n"
prompt += "4. Excess Representation\n"
prompt += "5. Change Default Byte Length\n"
prompt += "q. Exit Program\n\nChoose from the above options: "
options = ['1','2','3','4','5','q']

while runProgram:
     option = choice(prompt,options)
     print("\n" + ('#'*80) + "\n")
     if option == 'q':
          print("Exiting Program..")
          runProgram = False
     elif option == '1':
          print("\t\t\tSIGNED VALUE REPRESENTATION")
          if chooseBinary():
               stdin = getBinaryInput()
               result = signValueBD(stdin)
               printBD(stdin,result)
          else:
               stdin = getIntegerInput()
               result = signValueDB(stdin)
               printDB(stdin,result)
     elif option == '2':
          print("\t\t\tONES COMPLEMENT REPRESENTATION")
          if chooseBinary():
               stdin = getBinaryInput()
               result = onesCompBD(stdin)
               printBD(stdin,result)
          else:
               stdin = getIntegerInput()
               result = onesCompDB(stdin)
               printDB(stdin,result)
     elif option == '3':
          print("\t\t\tTWOS COMPLEMENT REPRESENTATION")
          if chooseBinary():
               stdin = getBinaryInput()
               result = twosCompBD(stdin)
               printBD(stdin,result)
          else:
               stdin = getIntegerInput()
               result = twosCompDB(stdin)
               printDB(stdin,result)
     elif option == '4':
          print("\t\t\tEXCESS REPRESENTATION")
          if chooseBinary():
               stdin = getBinaryInput()
               result = excessBD(stdin)
               printBD(stdin,result)
          else:
               stdin = getIntegerInput()
               result = excessDB(stdin)
               printDB(stdin,result)
     elif option == '5':
          print("\t\t\tCHANGE DEFAULT BYTE LENGTH [4-16]")
          byteSize = getByteLength()
          print("Byte length has been set to " + str(byteSize) + " bytes.")
     print("\n" + ('#'*80) + "\n")
          
          
                         
                         
               
