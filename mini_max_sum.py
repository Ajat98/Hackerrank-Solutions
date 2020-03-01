#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mi = sum(arr) - max(arr)
    ma = sum(arr) - min(arr)
    print(str(mi) + " " + str(ma))
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
