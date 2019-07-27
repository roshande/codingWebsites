"""def abbreviation(a,b):
	
for _ in range(int(input())):
	a = input()
	b = input()
	n,m = len(a),len(b)
	d = [[0]*(n+1)]*(m+1)
	d[0][0] = 1
	for i in range(1,n+1):
		for j in range(m+1):
			if a[i] == b[j]:
				d[i][j] = d[i-1][j-1]
			elif toupper(a[i]) == b[j]:
				d[i][j] = d[i-1][j-1] | d[i-1][j]
			elif isupper(a[i]):
"""				
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
"""def abbreviation(a, b):
    a_i, b_i = 0, 0
    while a_i < len(a) and b_i < len(b):
        if (ord(a[a_i]) - ord(b[b_i]) in (0,32)):
            b_i += 1
        elif a[a_i].isupper():
            return "NO"
        #reject
        a_i += 1
    if a_i == len(a):
        if b_i != len(b):
            return "NO"
        return "YES"
    elif b_i == len(b):
        if a[a_i:].islower():
            return "YES"
        return "NO"
"""

def abbreviation(a, b, i=0, j=0):
    if j == len(b):
        if i == len(a) or (i+1 < len(a) and a[i+1:].islower()):
            return True
        else:
            return False
    elif i == len(a):
        return False
    print(a[i],b[j])
    if ord(a[i]) == ord(b[j]):
        return abbreviation(a,b,i+1,j+1)
    elif ord(a[i]) - ord(b[j]) == 32:
        return abbreviation(a,b,i+1,j+1) or abbreviation(a,b,i+1,j)
    elif a[i].islower():
        return abbreviation(a,b,i+1,j)
    else:
        return False

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        if result:
            print("YES")
        else:
            print("NO")
