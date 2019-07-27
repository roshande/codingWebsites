for _ in range(int(input())):
    n = int(input())
    jars = list(map(int, input().split()))
    print(sum(jars) - n + 1)
    #jars.sort()
    #count_n = n*(jars[0]-1) +1
    #rem = jars[0]
    #n-=1
    #for j in jars[1:]:
    #    if n*(j-rem-1)+1 > rem:
    #        count_n += n*(j-rem-1) + 1 - rem
    #        rem = j
    #        n-=1
    #print(count_n)

