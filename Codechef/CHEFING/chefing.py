for _ in range(int(input())):
    n = int(input())
    ingredients = [[0]*26 for _ in range(n)]
    ingredients.append([1]*26)
    for i in range(n):
        for ch in input():
            ingredients[i][ord(ch)-ord('a')] += 1
    #print(ingredients)
    count = 0
    trans = list(zip(*ingredients))
    #print(trans)
    for i in range(26):
        count += min(trans[i])
    print(count)
