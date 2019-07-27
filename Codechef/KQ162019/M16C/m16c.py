for _ in range(int(input())):
    T, M, S, P = list(map(int, input().split()))
    nt, nm, ns, np = list(map(int, input().split()))
    pt, pm, ps, pp = list(map(int, input().split()))
    R = int(input())
    min_chai = min([nt//T, nm//M, ns//S, np//P])
    nt = nt%min_chai


