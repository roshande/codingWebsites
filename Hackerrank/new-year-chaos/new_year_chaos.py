#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    minbribe = 0
    for i in range(len(q)):
        bribe = q[i] - (i+1)
        if bribe > 2:
            print("Too chaotic")
            return
        minbribe += max(bribe,0)
    print(minbribe)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

