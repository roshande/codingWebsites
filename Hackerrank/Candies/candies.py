#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candy = [1]*len(arr)
    candy_rev = [1]*len(arr)
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            candy[i] = candy[i-1]+1
        if arr[-i] < arr[-i-1]:
            candy_rev[-i-1] = candy_rev[-i]+1
    print(candy)
    print(candy_rev)
    return sum([max(candy[i],candy_rev[i]) for i in range(len(arr))])

if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = candies(n, arr)
    print(result)

