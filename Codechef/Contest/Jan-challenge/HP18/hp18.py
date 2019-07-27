def count_multiples(seq, a, b):
    ma, mb, mab = 0, 0, 0
    for num in seq:
        if num%a == 0:
            ma += 1
            if num%b == 0:
                mab += 1
        elif num%b == 0:
            mb += 1
    return ma,mb,mab

def winner(seq, a, b):
    if a == 1:
        return "BOB"
    elif b == 1:
        return "ALICE"
    ma, mb, mab = count_multiples(seq, a, b)
    #if ma != 0 and ma == mb and mb == mab:
    if ma != 0 and (ma + mb) == 2*mab:
        return "BOB"
    elif ma == 0:
        return "ALICE"
    elif mb == 0:
        return "BOB"
    elif ma - mab > mb - mab:
        return "ALICE"
    elif ma - mab <= mb - mab:
        return "BOB"

for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    print(winner(seq, a, b))
