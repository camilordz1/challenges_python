# You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and 
# return the result as an unsigned integer.

# Example

# 9 base 10 is iqual
# 1001 base 2. We're working with 32 bits, so:
# 00000000000000000000000000001001 base 2 = 9 base 10
# 11111111111111111111111111110110 base 2 = 4294967286 base 10

# Return 4294967286.

# Function Description

# Complete the flippingBits function in the editor below.

# flippingBits has the following parameter(s):

# int n: an integer

# Returns

# int: the unsigned decimal integer result

def flippingBits(n):
    binary = toBinary(n,32)
    flip = lambda x:0 if x==1 else 1
    return toDecimal([flip(num) for num in binary])

def toBinary(n,bits):
    bin = []
    while n > 0:
        bin.insert(0,n%2)
        n = n//2
    return [0]*(bits-len(bin)) + bin

def toDecimal(n):
    n.reverse()
    return sum([num*2**pos for pos, num in enumerate(n)])

print(flippingBits(9))








    

