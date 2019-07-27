for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(1,n):
        arr[i] += arr[i-1]

    """
    print(arr)
    for i in range(n):
        if i+1+arr[i] >= n:
            print(i+1)
            break
        """
    done = [False]*n
    done[0] = True
    last = 0
    day = 0
    #while not all(done):#last < n:
    while last < n-1:
        day += 1
        #done[[last + i for i in range(1,arr[last]+1) if last + i < n]] = True
        #for i in range(1,arr[last]+1):
        #    if last + i < n:
        #        done[last+i] = True
        last += arr[last]
    print(day)
