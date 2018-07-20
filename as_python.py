
value = int(input("Enter integer (0-99): "))
operation = input("Calculate additive or multiplicative persistence (a or m)?")
count = 0
while(value > 9):
    if operation == 'a':
        value = (value/10) + (value%10)
    else:
        value = (value/10) * (value%10)
    count += 1
print("The persistnece is: " + str(count))
