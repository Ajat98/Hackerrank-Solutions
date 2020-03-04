#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    if (min(keyboards) + min(drives)) > b:
        return -1
    elif (min(keyboards) + min(drives)) == b:
        return b
    
    max_list = []
    m = 0
    for i in range(len(keyboards)):
        for c in range(len(drives)):
            cost = keyboards[i] + drives[c]
            if cost > m and cost <= b:
                max_list.append(cost) 
    return max(max_list)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
