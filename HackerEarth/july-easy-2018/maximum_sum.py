'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = input()
numArray = map(int,input().split(' '))

count=0
max_sum=0
for i in numArray:
    if i > 0:
        count +=1
        max_sum += i

print(max_sum,count)
