#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    
    
    ranks = sorted(set(scores), reverse=True )
    
    leaderBoard = {}
    r = len(ranks)
    res = []
    for i in alice:
        #If score is >= score at end of leaderboard, subtract 1 from index to check next score up.
        while (r > 0) and (i >= ranks[r-1]):
            r -= 1
        res.append((r+1)) #Once score is less than next score up, index is added to res
        
    return(res)
        
    #Reverse =False in rank needs to be set for this segment. Long runtime and messy
    """
    for i in range(len(ranks)):
        if r in leaderBoard:
            leaderBoard[r].append(ranks[i])
        elif r not in leaderBoard:
            leaderBoard[r] = ranks[i]
        r -=1
    print(leaderBoard)
    #Once checked lower scores do not compare again

    alice_ranks = []
    for i in range(len(alice)):
        place = 0
        if alice[i] in ranks:
            place = ranks.index(alice[i])
        else:
            ranks.append(alice[i])
            ranks = sorted(ranks, reverse=False)
            place = ranks.index(alice[i])
        
        alice_ranks.append(len(ranks) - place)
        
    return(alice_ranks)  
    """


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
