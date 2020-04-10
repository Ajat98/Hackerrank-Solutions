#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    #Starting conditions
    e = 100
    i = k
    pos = 0


    while True:
        pos = (i) % n
        e -= 1
        
        if c[pos] == 1:
            e -=2
        if pos == 0:
            return e
            break
        i += k
       
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
