'''Print out the leap years from now until the year 2500.
 Leap years are those that are divisible by 4,
  except that years that are divisible by 100 are not leap years,
  unless they're also divisible by 400.'''


#get leap years
for year in range(2017,2501):
	if year % 4 == 0:
		if year % 100 == 0 and year % 400 == 0:
			print(str(year)) 
		elif year % 100 == 0:
			continue
		else:
			print(str(year))
x = input("Press enter to end:")
