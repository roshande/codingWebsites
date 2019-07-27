for t in range(int(input())):
    n,k = map(int,input().split())
    heights = list(map(int,input().split()))
    steps = heights[0]//k
    if heights[0]%k == 0:
        steps-=1
    for i in range(1,n):
        steps += (heights[i]-heights[i-1])//k
        if (heights[i]-heights[i-1])%k == 0:
            steps-=1
    print(steps)
