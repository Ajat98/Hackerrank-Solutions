#!/bin/python3

import math
import os
import random
import re
import sys

"""
In binary form:
    k   = 11
    k-1 = 10
    k-1 == (k-1) & k

That is , ((k-1) | k) is always k. And ((k-1) | k) <= n is always TRUE.
When k is EVEN , k-1 is ODD , k-1 can only be reached if and only if ((k-1) | k) <= n is TRUE

Because of binary form:
    k = 10110
    k-1 = 10101
    pos = 10111
    k-1 == (k-1) & pos

get k-1 if pos <= n TRUE 
can get pos by ((k-1)| (k-1+1))
otherwise follow above process when k is odd then get answer of k-2
So ( (k-1) | k) <=n will determine answer
"""


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)
