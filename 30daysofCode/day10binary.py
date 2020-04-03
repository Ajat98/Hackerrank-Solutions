#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = str(bin(n)[2:]) #Erase the 0b at start
    
    streak = 0
    current_best = 0
    for i in binary:
        if int(i) ==0:
            streak = 0
        if int(i) ==1:
            streak+=1
            if streak > current_best:
                current_best = streak
        
    print(current_best)
