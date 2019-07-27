n, m = map(int,input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
arr_index = [(i,0) for i in range(n)]
arr_set = set([num + arr_b[0] for num in arr_a])
done = False
for i,num1 in enumerate(arr_a):
    for j,num2 in enumerate(arr_b[1:]):
        if num1 + num2 not in arr_set:
            arr_index.append((i,j+1))
            arr_set.add(num1+num2)
            if len(arr_set) == n+m-1:
                done = True
                break
    if done:
        break
#print(arr_set)
for i,j in arr_index:
    print(i,j,sep = ' ')
