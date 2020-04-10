#!/bin/python3

import sys

S = input().strip()

try:
    print(int(S))
except(SyntaxError, ValueError):
    (print('Bad String'))
