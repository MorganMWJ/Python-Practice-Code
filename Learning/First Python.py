#Morgan Jones
#First Python Program
#13/08/2015

def square(x):
     return x*x

print("Hello World!")
x = int(input("Number for me to square: "))
print (square(x))

#input - cast as the numeric type you want to read in when expecting a number

print('\n\n')
text = input("Enter some text for me to play with: ")
print("\nThis is the length of your text: ")
print(len(text))
print("\nThis is the first char of your text: ")
print(text[0])
print("\nThis is the last char of your text: ")
print(text[len(text)-1])
print("\nThese are all the letters inbetween: ")
print(text[1:len(text)-1])
print("\nThis is your text in uppercase: ")
print(text.upper())
print("\nThis is your text in lowercase: ")
print(text.lower())
print('\n')

if "love" in text:
     print("'love' was found in " + text)
else:
     print("There was no \'love\' found in " + text)

###########################################################

dragons = ["Fire","Ice","Lightening","Earth"]

dragons.append("Darkness")
print(dragons)
dragons.append("stupid")
print(dragons)
dragons.remove("stupid")
print(dragons)

dragons.sort() #sorts them alphabetically
print(dragons)

#notes on tuples
#dont need brackets around them to be inistialised
tup = 5*2,'hello',6**3
print(tup)
