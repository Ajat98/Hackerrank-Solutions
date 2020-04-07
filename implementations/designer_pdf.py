#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    for c in range(len(alphabet)):
        if c not in d:
            d[alphabet[c]] = h[c]
    
    height = len(word) #+1 ?
    highest = 0
    for i in word:
        if d[i] >highest:
            highest = d[i]

    return (highest * height)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
