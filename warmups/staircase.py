#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    c = 1
    btm = "#" * n
    lvl = ""
    for i in range(n):
        lvl = (n-c) * " " + (c *"#")
        print(lvl)
        c += 1
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
