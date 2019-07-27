#!/bin/python

import sys


s = raw_input().strip()
count=0
if int(s)%6==0:
    count=1
#print s
for i in range(len(s)):
    if s[i]!='0':
        for j in range(i+1,len(s)+1):
            if int(s[i:j])%6==0:
                count=count+1
            print s[i:j]

'''for i in range(len(s)):
    if s[i]!='0':
        j=i+1
        #print i,j
        while j<len(s):
            #print i,j
            if int(s[i:j])%6==0:
                #print s[i:j]
                count=count+1
            j=j+1
            '''
print count
# your code goes here

