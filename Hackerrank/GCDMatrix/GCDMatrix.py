#!/bin/python

import sys

def gcd(a,b):
    if a%b==0:
        return b
    elif a%2==0 and b%2==0:
        return 2*gcd(a/2,b/2)
    elif a%2==0:
        return gcd(a/2,b)
    elif b%2==0:
        return gcd(a,b/2)
    elif a>b:
        return gcd((a-b)/2,b)
    return gcd((b-a)/2,a)

n,m,q = raw_input().strip().split(' ')
n,m,q = [int(n),int(m),int(q)]
a = list(map(int, raw_input().strip().split(' ')))
b = list(map(int, raw_input().strip().split(' ')))

#gcd_matrix=[]
gcd_matrix=[[0]*len(b)]*len(a)
print gcd_matrix
for a_i in range(len(a)):
    for b_i in range(len(b)):
        gcd_matrix[a_i][b_i]=gcd(a[a_i],b[b_i])
'''for index_a,elem_a in enumerate(a):
    #gcd_temp=[]
    for index_b,elem_b in enumerate(b):
        gcd_matrix[index_a][index_b]=gcd(elem_a,elem_b)
        #gcd_temp.append(gcd(elem_a,elem_b))
    #gcd_matrix.append(gcd_temp)
'''
print gcd_matrix
for a0 in xrange(q):
    r1,c1,r2,c2 = raw_input().strip().split(' ')
    r1,c1,r2,c2 = [int(r1),int(c1),int(r2),int(c2)]
    unique_set=set()
    for gm_i in range(r1,r2+1):
        for gm_j in range(c1,c2+1):
            if gcd_matrix[gm_i][gm_j] not in unique_set:
                unique_set.add(gcd_matrix[gm_i][gm_j])
    print len(unique_set)
    # your code goes here

