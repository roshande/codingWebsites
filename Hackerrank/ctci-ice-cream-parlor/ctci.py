#!/bin/python3

import math
import os
import random
import re
import sys

def binary_search(costs, c, i):
    low, high = 0, len(costs)-1
    while low < high:# and low > -1 and high < len(costs):
        mid = high - (high-low)//2
        #print(low, mid, high)
        if costs[mid][1] < c:
            low = mid+1
        elif costs[mid][1] > c:
            high = mid-1
        elif costs[mid][0] == i:
            if costs[mid-1][1] == c:
            #if mid > 0 and costs[mid-1][1] == c:
                return costs[mid-1][0]
            elif costs[mid+1][1] == c:
            #elif mid < len(costs)-1 and costs[mid+1][1] == c:
                return costs[mid+1][0]
            else:
                return -1
        else:#costs[mid][0] != i
            return costs[mid][0]
    return -1

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    costs_dict = {}
    for i,c in enumerate(cost):
        if c not in costs_dict.keys():
            costs_dict[c] = [i]
        else:
            costs_dict[c].append(i)
    #print(costs_dict.items())
    for key,val in costs_dict.items():
        k = costs_dict.get(money-key, None)
        if k is None:
            continue
        if len(k) == 1:
            if val != k:
                return min(k[0],val[0])+1, max(k[0],val[0])+1
        else:
            other = sum(k)- val[0]
            return min(other,val[0])+1, max(other,val[0])+1

def whatFlavors1(cost, money):
    sorted_costs = sorted(enumerate(cost), key=lambda k:(k[1],k[0]))
    for i,c in sorted_costs:
        r = binary_search(sorted_costs, money - c, i)
        if r != -1:
            return min(r,i)+1, max(r,i)+1
    return 1,2

if __name__ == '__main__':
    for t_itr in range(int(input())):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        l,r = whatFlavors(cost, money)
        print(l,r)
