#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    v_count = 0
    current = 0
   
    for i in range(0, n):
        if s[i] == 'D':
            current -= 1
        if s[i] == 'U':
            current += 1
        if current < 0:
            if current +1 == 0 and s[i+1] == 'U':
                v_count +=1
      
    return v_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
