#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest = scores[0]
    highest = scores[0]
    records = [0,0]
    for i in scores[1:]:
        if i > highest:
            records[0] += 1
            highest = i
        elif i < lowest:
            records[1] +=1
            lowest = i
    return records


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
