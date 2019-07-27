def present(A, n, k):
    A = sorted(A)
    if 2*A[0] > k or 2*A[-1] < k or k == 1:
        return False
    for i in range(n):
        if binary_search(A, k - A[i], i):
            return True
    return False

def binary_search(A, x, i):
    l, r = 0, len(A)-1
    while l < r:
        print(l,r)
        mid = (l+r)//2
        if A[mid] < x:
            l = mid +1
        elif A[mid] > x:
            r = mid -1
        elif mid == i:
            if A[mid-1]==x or A[mid+1]==x:
                return True
            else:
                l = i-1
        else:
            return True
    return False

for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    if present(A, n, k):
        print("Yes")
    else:
        print("No")
