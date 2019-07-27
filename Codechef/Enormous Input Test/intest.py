input1 = raw_input().split(' ')
n = int(input1[0])
k = int(input1[1])
count =0
for i in xrange(n):
    num = int(raw_input())
    if num %k == 0 :
        count = count+1
print(count)
