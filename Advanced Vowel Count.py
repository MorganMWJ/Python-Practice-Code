#Advanced Counting Vowels
#########################
def sumVowels(vowelPairs):
     total = 0
     for x in vowelPairs:
          total += x[1]
     return total
#########################
vowels = ['a','e','i','o','u']
vowelCount = [['a',0],['e',0],['i',0],['o',0],['u',0]]

string = input("PLease enter some text: ").lower()
for letter in string:
     if letter in vowels:
          for vowel in vowelCount:
               if vowel[0]==letter:
                    vowel[1]+=1#increase that vowels quantity
                    
print("\nThere are " + str(sumVowels(vowelCount)) + " vowels in the text.\n")

for x in vowelCount:
     print("There is " + str(x[1]) + " " + x[0] + "(s) in the text.") 
