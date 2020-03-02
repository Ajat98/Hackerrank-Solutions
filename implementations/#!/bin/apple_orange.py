#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    on_house_apples = 0
    pos=0
    for i in apples:
        pos = i+a
        if pos >=s and pos <=t:
            on_house_apples += 1

    on_house_oranges = 0
    pos = 0
    for k in oranges:
        pos = k + b
        if pos >=s and pos <= t:
            on_house_oranges += 1

    print(on_house_apples)
    print(on_house_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
