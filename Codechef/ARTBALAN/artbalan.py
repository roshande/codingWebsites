import math

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(prime_array = set([2,3,5,7]))
def isprime(num):
    for n in isprime.prime_array:
        if num%n == 0:
            return False
    sqrt_num = int(math.sqrt(num))
    n += 2
    while n < sqrt_num:
        sqrt_n = int(math.sqrt(n))
        for i in isprime.prime_array:
            if n%i == 0:
                break
            if i > sqrt_n:
                isprime.prime_array.add(n)
                if num%n == 0:
                    return False
                break
        n+=2

for _ in range(int(input())):
    st = input()
    alphabets = [0]*26
    prime_lengths = [2,3,5,7,11,13,17,19,23]
    for s in st:
        alphabets[ord(s)-ord('A')] +=1

    for num in prime_lengths:
        if len(st)%num == 0:
            break
    
