def digitsum(n):
    s = 0
    times = 0
    while n>0:
        times += 1
        s += n%10
        n = n//10
    return s,times

d = {}
for i in range(1,10):
    for j in range(1,10):
        _min = i
        _ind = 0
        for k in range(10):
            if _min > digitsum(i+j*k)[0]:
                _min,_ind = digitsum(i+j*k)
        d[(i,j)] = (_min,_ind)

for key in sorted(d.iterkeys()):
    print("%s :%s"%(key,d[key]))
print(sorted(d))
