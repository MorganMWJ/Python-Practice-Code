#Counting Vowels
vowels = ['a','e','i','o','u']
vowelCount = 0

string = input("Please enter some text: ").lower()
for letter in string:
     if letter in vowels:
            vowelCount+=1
                  
print("There are " + str(vowelCount) + " vowels in the text.\n")
