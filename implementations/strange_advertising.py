#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    share = 5
    likes = 2
    cumul = 2
    
    for i in range(1, n):
        share = (share // 2) * 3
        likes = share// 2 
        cumul += likes
        
    return cumul

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
