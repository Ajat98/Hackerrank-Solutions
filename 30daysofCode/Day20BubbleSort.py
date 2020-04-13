#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble(n):
    numSwaps = 0
    for i in range(n):
        
        for j in range(n-1):
            if a[j] > a[j+1]:
                numSwaps += 1
                b = a[j]
                c = a[j+1]
                a[j] = c
                a[j+1] = b
                
        if numSwaps == 0:
            break

    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    
bubble(n)
