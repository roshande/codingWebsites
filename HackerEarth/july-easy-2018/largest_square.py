'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())
points = list()
for _ in range(N):
    num1,num2 = map(int,input().split(' '))
    points.append([num1,num2])

points.sort()
print(points)
#print(sorted(points))

for i in range(N):
    for j in range(i+1,N):
        if points[i][0] == points[j][0]:
            side = abs(points[i][1] - points[j][1])
        elif points[i][1] == points[j][1]:
            side = abs(points[i][0] - points[j][0])
        else:
            continue
        for k in range(j+1,N):
            if 
