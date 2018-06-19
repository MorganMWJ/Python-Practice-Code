#Counting the till program

#each denomination name,weight and value in a list
denoms = [("1p coins",3.56,0.01), ("2p coins",7.12,0.02), ("5p coins",3.25,0.05),
          ("10p coins",6.5,0.10), ("20p coins",5.0,0.20), ("50p coins",8.0,0.50),
          ("£1 coins",9.5,1.00), ("£2 coins",12.0,2.00), ("5.00 notes", 0.812, 5.00)]

total = 0.00
print ("Count the till program.\n")
for denom in denoms:
     correctInput=False
     while(False==correctInput):
          try:
               totalWeight = float (input("Enter the weight of the " + denom[0] + ": "))
               correctInput=True
          except:
               print("*Enter a DECIMAL NUMBER for the weight*")
     quantity = round(totalWeight/denom[1],0)
     amount = int(quantity)*denom[2] 
     total += amount
     total = round(total,2)
     print (denom[0] + " = " + str(int(quantity)) +
            "  value = " + str(round(amount,2)) +
            "\n(Current total: £" + str(total) + ")\n")
     if denom ==denoms[8]:
          print("There is £" + str(total) + "in the till.\nThanks for using the program!")



