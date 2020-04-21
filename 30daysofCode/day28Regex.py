#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())

    d = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x, i in enumerate(alphabet):
        d[i] = x

    names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if '@gmail.com' in emailID:
            names.append(firstName)
    #Use '*' to unpack iterable into arguments of the function call
    print(*sorted(names), sep='\n')
