#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    ### Readable version
    lates = sum(x <= 0 for x in a)
    
    if k <= lates:
        return 'NO'
    else: return 'YES'
    
    #One liner (same as above)    
    #return("NO" if k<= (sum(x <= 0 for x in a)) else 'YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
