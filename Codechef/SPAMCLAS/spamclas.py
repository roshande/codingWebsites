# cook your dish here
test = int(input())
while test > 0:
    N,minX,maxX = list(map(int,input().split()))
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    odd = 1
    even = 2
    for w,b in arr:
        odd,even = (w*odd + b)%2,(w*even+b)%2
    odd = odd%2
    even = even%2
    total_num = maxX - minX + 1
    odd_num = int(total_num/2)
    if total_num%2 == 1 and minX%2 == 1:
        odd_num+=1

    if odd == 0 and even == 0:
        print(total_num,0)
    elif odd == 1 and even == 1:
        print(0,total_num)
    elif odd == 1 and even == 0:
        print(total_num - odd_num,odd_num)
    else:
        print(odd_num,total_num - odd_num)
    test -=1
