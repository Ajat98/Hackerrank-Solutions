#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    p = 0
    n = 0
    neut = 0
    l = len(arr)

    for i in range(l):
        if arr[i] == 0:
            neut +=1
        if arr[i] < 0:
            n += 1
        if arr[i] > 0:
            p += 1
    
    print(p / l)
    print(n / l)
    print(neut / l)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
