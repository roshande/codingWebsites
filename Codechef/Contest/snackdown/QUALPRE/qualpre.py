import heapq

for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    heapq._heapify_max(arr)
    c = 0
    cnt = 0
    prev = 0
    while c != k:
        prev = heapq._heappop_max(arr)
        cnt += 1
        c += 1
    while prev == arr[0]:
        heapq._heappop_max(arr)
        cnt += 1
    print(cnt)

