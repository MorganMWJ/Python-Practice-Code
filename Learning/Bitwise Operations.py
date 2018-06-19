#Bitwise Operations

#bit shift <<
x = 2# x = 0b10
print(bin(x))

x = x << 3 #move all the (1)bits 3 bits to the left

#x = 0b10000 therefore x now equals 16
print(bin(x))
print(str(x) + "\n")

#bitwise
# OR = |
#AND = &
#XOR = ^


#OR inpputs only one must be true
#0110 | 1100 = 1110 
#6| 14 = 14
b = 6|14
print(bin(b))
#b = 0b1110
#b = 14

#XOR inputs must differ
#0101|1010 = 1111

#AND inputs must be the all true
# 1011 | 1011 | 1111 = 1011
