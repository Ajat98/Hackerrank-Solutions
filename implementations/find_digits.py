#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    digits = str(n)
    count = 0
    counted = []
    for i in digits:
        if int(i)!= 0 and n % int(i) ==0 and int(i) not in counted:
            count += 1
            counted.append(i)
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
