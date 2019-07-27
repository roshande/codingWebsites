#!/bin/python3

import math
import os
import random
import re
import sys

def checkanagrams(str1,str2):
    str1_hash = [0]*26
    for i in range(len(str2)):
        str1_hash[ord(str1[i])-ord('a')]+=1
        str1_hash[ord(str2[i])-ord('a')]-=1
    for num in str1_hash:
        if num != 0:
            return False
    return True

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    cnt = 0
    for length in range(1,len(s)):
        for j in range(len(s)-length):
            for k in range(j+1,len(s)-length+1):
                if checkanagrams(s[j:j+length],s[k:k+length]):
                    cnt+=1
    return cnt

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    print(checkanagrams("abdc","bdca"))
    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
