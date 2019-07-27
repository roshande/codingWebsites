def cirmerge_brute_force(A):
    if len(A) == 1:
        return 0
    penalty = 1e9
    n = len(A)
    for i in range(n):
        low = (i-1+n)%n
        penalty = min(penalty, A[i]+A[low]+ cirmerge_brute_force(A[:low]+A[i:]))
def cirmerge(A):
    penalty = 0
    while len(A) > 1:
        print(A)
        min_pen, min_i = A[0]+A[-1],-1
        for i in range(len(A)-1):
            if min_pen > A[i]+A[i+1]:
                min_pen = A[i]+A[i+1]
                min_i = i
        penalty += min_pen
        A[min_i+1] = min_pen
        del A[min_i]
    return penalty+ A[0]

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    print(cirmerge(A))
