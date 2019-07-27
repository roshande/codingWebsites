import math

def num_squares(num):
    count = 0
    while num > 0:
        sqrt = math.floor(math.sqrt(num))
        num -= sqrt*sqrt
        count += 1
    return count

#for i in range(1,1000):
#    squares.append(num_squares(i))
#print((squares))
for _ in range(int(input())):
    N = int(input())
    print(num_squares(N))
