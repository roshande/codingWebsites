def population(n):
    times = n//26
    rem = n - (26*times)
    bit,nibble,byte = 0,0,0
    if rem < 0:
        byte = 1 << (times-1)
    elif rem < 2:
        bit = 1<<times
    elif rem < 10:
        nibble = 1<<times
    else:
        byte = 1<<times
    return bit,nibble,byte

for t in range(int(input())):
    n = int(input())
    for num in population(n):
        print(num,end=" ")
    print()
    #print(*population(n))
