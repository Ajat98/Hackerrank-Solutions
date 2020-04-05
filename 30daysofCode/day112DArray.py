#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    rows = len(arr)
    cols = len(arr[0])
    #Hour glass shape: 3 consecutive nums, 1 row down: 1 non zero num:, 1 row down, 3 consecutive ums
    
    max_sum = 0
    temp_sum = 0
    for i in range(4):
        for j in range(4):
            temp_sum = 0
            #For top Row
            temp_sum += sum(arr[i][j:j+3])
            #Middle Row
            temp_sum += arr[i+1][j+1]
            #Bottom row
            temp_sum += sum(arr[i+2][j:j+3])

            #Need to set first temp_sum to max_sum in case of negative sums
            if temp_sum > max_sum or i == 0 and j == 0:
                max_sum = temp_sum
    print(max_sum) 
    
