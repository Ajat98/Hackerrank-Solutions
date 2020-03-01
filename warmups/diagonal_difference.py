#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    m = len(arr)
    n = len(arr[0])

    #right diagonal
    r = 0
    k = 0
    for i in range(m):
        if k <= n:
            r += arr[i][k]
            k += 1
    
    #left diag
    x = 0
    l = 1
    for i in range(m):
        if l <= n:
            x += arr[i][-l]
            l += 1
    return abs(x - r)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
