'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,m = map(int, input().split())
text = []
for _ in range(n):
    text.append(input())
saba_count = 0
mat = (((0,0,0,0),(0,1,2,3)),
        ((0,1,2,3),(0,0,0,0)),
        ((0,1,2,3),(0,1,2,3)),
        ((3,2,1,0),(0,1,2,3)))
for row in range(n-3):
    for col in range(m-3):
        for mr,mc in mat:
            print(text[row+mr[0]][col+mc[0]], text[row+mr[1]][col+mc[1]],text[row+mr[2]][col+mc[2]],text[row+mr[3]][col+mc[3]])
            if text[row+mr[0]][col+mc[0]] == 's'and text[row+mr[1]][col+mc[1]] == 'a' and text[row+mr[2]][col+mc[2]] == 'b' and text[row+mr[3]][col+mc[3]] == 'a':
                saba_count += 1
print(saba_count)
