import math

primes = [2,3,5,7,11]
def next_prime(num):
    n = num + num%2 +1
    while True:
        if is_prime(n):
            return n

def is_prime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

term = False
ans = False
for _ in range(int(input())):
    x = 2
    if term:
        break
    while True:
        if not ans:
            print(1,x)
        else:
            print(2,x)
        resp = input()
        if ans:
            if resp == "Yes":
                ans = False
                break
            elif resp == "No":
                #DONT KNOW
                continue
        resp = int(resp)
        if resp == -1:#Too many queries or query invalid
            term = True
            break
        elif resp == 0:
            ans = True
        elif resp == x*x: #number greater than x*x
            x = next_prime(x)
        elif is_prime(x*x -resp):
            x = x*x - resp
            ans = True
        #else:

