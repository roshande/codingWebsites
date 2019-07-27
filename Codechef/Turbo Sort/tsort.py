t = int(raw_input())
array = []
for i in range(t):
    num = int(raw_input())
    array.append(num)
array.sort()
print('\n'.join(map(str,array)))
