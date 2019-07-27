def digitsum(n):
    s = 0
    while n>0:
        s += n%10
        n = n//10
    return s

def change(n):
    times = 0
    while n > 9:
        times += 1
        n = digitsum(n)
    return n,times

for t in range(int(input())):
    n,d = map(int,input().split())
    n,times = change(n)
    d,times1 = change(d)
    times += times1
    min_n,min_i = n,0
    for i in range(1,10):
        k,j = change(n+i*d)
        if min_n > k:
            min_n = k
            times += j
            min_i = i
        if min_n == 1:
            break
    print("%s %s"%(min_n,times+min_i))
