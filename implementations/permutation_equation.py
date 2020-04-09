#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):

    res = []
    first_index = 0
    second_index = 0
    for i in range(n):
        x = i +1
        first_index = p.index(x)
        second_index = p.index(first_index+1)

        res.append(second_index +1)
    return res




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
