#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    time = s[:-2]
    hour = int(time[:2])
    
    if s[-2:] == "PM":
        if hour == 12:
            time = "12" + time[2:]
            
        else:
            hrs = int(time[:2]) + 12
            time = str(hrs) + time[2:]
        
    if s[-2:] == "AM":
        if hour == 12:
            time = "00" + time[2:]
            
    return time
        
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
