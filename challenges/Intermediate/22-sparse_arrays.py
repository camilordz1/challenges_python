#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    results = [] 

    for query in queries:
        results.append([string for string in strings if string == query])

    return [len(res) for res in results]   

if __name__ == '__main__':

    strings = ["def","de","fgh"]
    queries = ["de","lmn","fgh"]

    res = matchingStrings(strings, queries)
    print(res)