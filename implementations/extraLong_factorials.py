#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    total =1
    for i in range(1, n+1):
        total *= i
    print(total)
    

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
