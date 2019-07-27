#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_right
from itertools import accumulate
import operator

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    less = []#[(0,0)]*len(b)
    l_a, l_c = 0,0
    for num in b:
        l_a = bisect_right(a, num, l_a)
        l_c = bisect_right(c, num, l_c)
        less.append((l_a,l_c))
    print(less)
    S = sum(map(lambda x:x[0]*x[1], less))
    return S

if __name__ == '__main__':
    lena, lenb, lenc = list(map(int, input().split()))
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    print(ans)
