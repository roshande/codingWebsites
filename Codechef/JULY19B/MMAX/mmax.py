def max_sum(n,k):
    num_min = min(k%n, n - (k%n))
    num_max = n-num_min
    if num_min == num_max:
        return n-1
    return 2*num_min

for _ in range(int(input())):
    n, k = int(input()), int(input())
    print(max_sum(n,k))
