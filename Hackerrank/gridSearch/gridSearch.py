#!/bin/python3

import sys

def gridSearch(G,P):
    if len(G) < len(P):
        return False
    for i in range(len(G)-len(P)):
        prev_pos=G[i].find(P[0])
        while prev_pos != -1:
            j=1
            temp_i=i+1
            while j<len(P):
                new_pos=G[temp_i].find(P[j],prev_pos)
                if new_pos != prev_pos :
                    break
                j=j+1
                temp_i=temp_i+1
            if j == len(P):
                return True
            prev_pos=G[i].find(P[0],prev_pos+1)
    return False        

#t = int(input().strip())
t = int(input())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    if gridSearch(G,P):
        print("YES")
    else:
        print("NO")

