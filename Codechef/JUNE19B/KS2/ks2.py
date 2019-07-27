from functools import reduce
for _ in range(int(input())):
    num = input()
    sum_digit = reduce(lambda x,y: int(x)+int(y), num)
    if sum_digit%10 == 0:
        print(num+"0")
    else:
        print(f"{num}{10-sum_digit%10}")
