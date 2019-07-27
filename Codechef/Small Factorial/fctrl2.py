def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1)*num

n = int(raw_input())
for i in xrange(n):
    num = int(raw_input())
    ans = factorial(num)
    print(ans)

