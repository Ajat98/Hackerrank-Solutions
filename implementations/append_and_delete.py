#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
     if k >= len(s) + len(t) :
        return "Yes"

     i = 0 
     m = min( len(s), len(t) )
     while i < m and s[i] == t[i] :
         i += 1    
     d = len(s)-i + len(t)-i
        
     if k < d or (k-d)%2: 
        return "No"
     if k == d or not (k-d)%2:
         return "Yes"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
