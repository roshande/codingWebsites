arr = []
for t in range(int(input())):
    n = int(input())
    arr.append(n)
for num in reversed(sorted(arr)):
    print(num)
