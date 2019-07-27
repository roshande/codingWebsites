for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    avg = sum(coins)/n
    try:
        print(coins.index(avg)+1)
    except ValueError:
        print("Impossible")

