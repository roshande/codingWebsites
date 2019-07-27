ESP = 1E9 + 7
def power(n,k):
    if k == 1:
        return n
    elif k == 0:
        return 1
    half = power(n,k//2)%ESP
    if k%2 == 0:
        return (half*half)%ESP
    return (half*half*n)%ESP

# Write your code here
for _ in range(int(input())):
    n, k = map(int,input().split())
    
    ways = (k*power(k-1,n-1))%ESP
    print(int(ways))
