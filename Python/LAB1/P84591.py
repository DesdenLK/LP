def absValue(x):
    return -x if x < 0 else x

def power(x, p):
    return x**p

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int((x**0.5)+1)):
        if x % i == 0:
            return False
    return True

def slowFib(n):
    if n < 2: return n
    return slowFib(n-1) + slowFib(n-2)

def quickFib(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b