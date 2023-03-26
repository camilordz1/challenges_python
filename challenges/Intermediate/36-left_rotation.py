# A left rotation operation on an array of size n shifts each of the array's 
# elements 1 unit to the left. Given an integer,d, rotate the array that 
# many steps left and return the result.

def rotateLeft(d, arr):
    return arr[d:]+arr[:d]

a = [1,2,3,4,5]
print(rotateLeft(4,a))