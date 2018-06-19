#Practice with dictionaries

record = {'name': {'first': 'bob', 'last': 'smith'},
          "job": ['developer', 'manager'],
          "age": 19,
          'dob': {'day': 25, 'month': 6, 'year': 1996}}

#main dictionary keys are name,job,age,dob
#the values to their right can be as comples as wanted

#dictionary comprehensions
dictionary = {x:x**2 for x in [1,5,2,6]}
#--> {1: 1, 2: 4, 5: 25, 6: 36} keys can be different order
print(dictionary,'\n')

d2 = {c:c*3 for c in ['a','b','c']}
print(d2,'\n')

d2 = {c.upper() + ' x3':c*3 for c in ['a','b','c']}
#both the key and value can me changed by functions
print(d2,'\n')
