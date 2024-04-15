def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a+b


def roots(x):
    f = x
    yield f
    r = 0.5*(f + (x/f))
    while True:
        yield r
        r = 0.5 * (r + (x/r))

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int((x**0.5)+1)):
        if x % i == 0:
            return False
    return True

def primes():
    i = 2
    while True:
        if isPrime(i):
            yield i
        i += 1

def hammings():
    i = 1
    while True:
        if isHamming(i):
            yield i
        i += 1

def isHamming(x):
    if x == 1: return True
    elif x % 2 == 0: return isHamming(x/2)
    elif x % 3 == 0: return isHamming(x/3)
    elif x % 5 == 0: return isHamming(x/5)
    return False