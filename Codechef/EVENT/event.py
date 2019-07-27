week_map={
        "sunday":1,
        "monday":2,
        "tuesday":3,
        "wednesday":4,
        "thursday":5,
        "friday":6,
        "saturday":7
        }
for _ in range(int(input())):
    s,e,l,r = input().split()
    l,r = int(l),int(r)
    diff1 = week_map[e] - week_map[s] + 1
    diff2 = r-l+1
    if diff1 < 2:
        diff1 += 7
    if diff1 >= l and diff1 <= r:
        if diff1 + 7 > l and diff1 + 7 <= r:
            print("many")
        else:
            print(diff1)
    else:
        print("impossible")
