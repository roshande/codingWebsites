#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(string):
    freq = {}
    freq_freq = {}
    for s in string:
        freq[s] = freq.get(s,0)+1
        if freq_freq.get(freq[s]-1,0) != 0:
            freq_freq[freq[s]-1] -= 1
            if freq_freq[freq[s]-1] == 0:
                del freq_freq[freq[s]-1]
        freq_freq[freq[s]] = freq_freq.get(freq[s],0)+1
    print(freq, freq_freq)
    if len(freq_freq) == 1:
        return "YES"
    elif len(freq_freq) > 2:
        return "NO"
    m,n = freq_freq.keys()
    m,n=max(m,n),min(m,n)
    if n==1 and freq_freq[n]==1 or m-n==1 and freq_freq[m] == 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

