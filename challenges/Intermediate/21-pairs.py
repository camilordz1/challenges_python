import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # pairs
    pairs = []
    for pos,i in enumerate(ar):
        pair = [[i,j] for pos2, j in enumerate(ar[pos::]) if pos2>0]
        pairs = pairs + pair

    return len([pair for pair in pairs if (pair[0]+pair[1])%k == 0])
   

if __name__ == '__main__':
    n = 6 
    k = 4
    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(n, k, ar)
    print(result)
