def gcd(b,a=0):
    if a == 0:
        return b
    return gcd(a, b%a)

def get_connection_fee(weight, mc, i):
    fees = [-1]*len(weight)

def get_fee(gcds):
    S = 0
    for i in range(len(gcds)):
        for j in range(i+1, len(gcds)):
            S += gcd(gcds[i], gcds[j])
    return S

for _ in range(int(input())):
    n = int(input())
    gcds = [0 for _ in range(n)]
    s = []
    for _ in range(n-1):
        x,y,z = list(map(int,input().split()))
        x,y = min(x,y),max(x,y)
        if x == 1:
            gcds[y-1]=z
        else:
            if gcds[x-1] == 0:
                if gcds[y-1] != 0:
                    gcds[x-1] = gcd(gcds[y-1], z)
                s.append((x,y,z))
            else:#if gcds[y-1] == 0:
                gcds[y-1] = gcd(gcds[x-1], z)
    for x,y,z in s:
        if gcds[x-1] == 0:
            if gcds[y-1] != 0:
                gcds[x-1] = gcd(gcds[y-1], z)
        else:#if gcds[y-1] == 0:
            gcds[y-1] = gcd(gcds[x-1], z)
    result = get_fee(gcds)
    #print(gcds)
    print(result)





#    degree[x-1]+=1
#    degree[y-1]+=1
#    weight[x-1][y-1] = z
#    weight[y-1][x-1] = z
#    most_conn = degree.index(max(degree))
#    gcds = [1]*n
#    for i in range(n):
#        if i == most_conn:
#            continue
#        if weight[most_conn][i] != 0:
#            gcds[i] = weight[most_conn][i]
#        else:
#            gcds[i] = get_connection_fee(weight, most_conn, i)
#    for i in range(n):
#        for j in range(i+1,n):
#            S += gcd()
