possibilities = {
    "1":True,
    "0":False,
    "10":True,
    "01":True,
    "11":False,
    "00":False,
    "000":False,
    "001":True,
    "010":True,
    "011":False,
    "100":True,
    "110":True,
    "101":False,
    "111":True
}
def is_possible(S):
    #print(S)
    val = possibilities.get(S)
    if val is not None:
        return val
    #val = possibilities.get(reversed(S))
    #if val is not None:
    #    return val
    toggle = lambda x: '0' if x == '1' else '1'
    if S[0] == '1':
        new_s = toggle(S[1])+S[2:]
        fs = is_possible(new_s)
        possibilities[new_s] = fs
        if fs:
            return True
    if S[-1] == '1':
        new_s = S[:-1]+toggle(S[-2])
        fs = is_possible(new_s)
        possibilities[new_s] = fs
        if fs:
            return True
    for i in range(1, len(S)-1):
        if S[i] == '1':
            new_s = S[:i-1]+toggle(S[i-1])
            fs = is_possible(new_s)
            possibilities[new_s] = fs
            new_s = toggle(S[i+1])+S[i+2:]
            ls = is_possible(new_s)
            possibilities[new_s] = ls
            if fs and ls:
                return True
    return False

for _ in range(int(input())):
    S = input()
    if is_possible(S):
        print("WIN")
    else:
        print("LOSE")
#print(possibilities)
