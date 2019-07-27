for _ in range(int(input())):
    inp = [input(), input(), input()]
    #print(inp)
    good = "no"
    for r in range(2):
        for c in range(2):
            if inp[r][c] == 'l' and inp[r+1][c] == 'l' and inp[r+1][c+1] == 'l':
                good = "yes"
                break
        if good == "yes":
            break
    print(good)
