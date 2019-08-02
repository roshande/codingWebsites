for _ in range(int(input())):
    n = int(input())
    goals = list(map(int, input().split()))
    fouls = list(map(int, input().split()))
    points = [max(0, g*20-f*10) for (f,g) in zip(fouls, goals)]
    print(max(points))
