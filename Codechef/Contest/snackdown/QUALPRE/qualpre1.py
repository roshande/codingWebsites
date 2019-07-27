for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = k
    for i in range(k):
        index_max_score = i
        for j in range(i+1,n):
            if arr[j] >= arr[index_max_score]:
                index_max_score = j
        arr[index_max_score],arr[i] = arr[i],arr[index_max_score]
    for i in range(k,n):
        if arr[i] == arr[k-1]:
            cnt += 1
    print(cnt)


