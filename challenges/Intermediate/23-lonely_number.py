# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

# [1,2,3,4,3,2,1]

# The unique element is 4.

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the element that occurs only once
# Input Format

# The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a.

def lonelyinteger(a):
    count = {n:a.count(n) for n in a}
    return [k for k,v in count.items() if v==1][0]

print(lonelyinteger([1,2,3,4,3,2,1]))    
