#Numeric notation

#hexadecimal,octal and binary
#below function convert from decimal to other bases as strings
print(hex(50)) #base 16
print(oct(50)) #base 8
print(bin(50)) #base 2

h = 0x40 #64 in hexadecimal [4*(16^1)] + [0*(16^0)]
o = 0o21 #17 in octal [2*(8^1)] + [1*(8^0)]
b = 0b110 #6 in binary [1*(2^2)] + [1*(2^1)] + [0*(2^0)]

print(str(h), str(o), str(b))#will all print as decimal


#python call also convert to decimal from any of these bases
#usng the int() function to cast hex as decimal
#just like int can cast string int as an int
x = int('64')   #turns string decimal into decimal base
y = int('100',8)#turns string octal into decimal base
z = int('40',16)#turns string hex into decimal base

#this aslo works if typeing literally 0x40
a = int('0x40',16)
b = int('0b110',2)

#you can also convert integers to other bases by using string formatting methods
print('%o, %x, %X' % (64, 255, 255))

#EXTRA notes on Math module of the standard libary
#constants
math.pi, math.e

#sine tangent, cosine
math.sin(45)

#absoulute, sum, power & sqrt
math.abs(-7.8)
math.pow(3,2)
math.sqrt(4)

#floor gores to the lower near ineteger
math.floor(2.567) #>>> 2
math.floor(-2.567)#>>> -3

#truncate just removes all after the decimal place
math.truncate(-2.567)#>>>-2

#normal rounding
round(2.4)#rounds down
round(4.6)#rounds up

#formatting (not to do with math)
print('%.1f' % 2.567) #format 1 dp and apply to 2.567




