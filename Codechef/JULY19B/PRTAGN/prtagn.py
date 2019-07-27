bin_cnt = lambda n:n>0 and bin_cnt(n&(n-1)) + 1 or 0

def even_odd(S, X):
    global even
    to_add = set([X])
    if X not in S and bin_cnt(X)&1 == 0:
        even += 1
    for y in S:
        if y != X:
            new_num = y^X
            if new_num not in S and new_num not in to_add and bin_cnt(new_num)&1 == 0:
                even += 1
            to_add.add(new_num)
    S.update(to_add)

def even_odd1(S, X):
    global even
    if X in S:
        return
    to_add = set([X])
    if bin_cnt(X)&1 == 0:
        even += 1
    for y in S:
        new_num = y^X
        if new_num not in S and bin_cnt(new_num)&1 == 0:
            even += 1
        to_add.add(new_num)
    S.update(to_add)

for _ in range(int(input())):
    S = set()
    even = 0
    for _ in range(int(input())):
        X = int(input())
        even_odd1(S, X)
        print(list(map(bin, S)))
        print(even, len(S)-even)
