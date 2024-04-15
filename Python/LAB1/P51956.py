def myLength(L):
    return len(L)


def myMaximum(L):
    return max(L)

def average(L):
    return sum(L)/len(L)

def buildPalindrome(L):
    r = list(reversed(L))
    for l in L: r.append(l)
    return r

def remove(L1, L2):
    R = []
    for l in L1:
        if l not in L2:
            R.append(l)
    return R

def flatten(L):
    R = []
    for l in L:
        if isinstance(l, list):
            R += flatten(l)
        else:
            R.append(l)
    return R

def oddsNevens(L):
    par = []
    sen = []
    for l in L:
        if l % 2 == 0:
            par.append(l)
        else:
            sen.append(l)
    return sen, par

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int((x**0.5)+1)):
        if x % i == 0:
            return False
    return True

def primeDivisors(n):
    l = []
    for i in range (2, int(n/2) + 1):
        if n % i == 0 and isPrime(i):
            l.append(i)
    
    if isPrime(n):
        l.append(n)
    return l