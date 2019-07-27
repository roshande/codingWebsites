def countSquare(n,m):
    result=0
    for i in range(1,min(n,m)):
        result+=(m-i)*(n-i)
    result%=(7E9)
    i=2
    while i < min(n,m):
        result+=(n-i)*(m-i)
        i*=2
   result %=(7E9)

n =int(input())
for i in xrange(1,n+1):
    n,m = map(int,input().strip().split(' '))
    result = countSquare(n,m)
    print("Case #%s: %d"%(i,result))
