def zerosumsubarray(array):
    if len(array) == 1:
        if array[0]%2==0:
            return 1
        return 0
    result=0
    if sum(array)%2==0:
        result=1
    for i in range(int(len(array))-1):
        for j in range(i+1,int(len(array))):
            if sum(array[i:j])%2==0:
                result = result+1
    return result

n = int(input().strip())
array = list(map(int,input().strip().split(' ')))
print(zerosumsubarray(array))

