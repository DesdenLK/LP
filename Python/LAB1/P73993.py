from functools import reduce

def evens_product(L):
    R = list(filter(lambda x: x%2 == 0, L))
    return reduce(lambda acc,y: acc*y, R, 1)

def reverse(L):
    return reduce(lambda acc,y: [y] + acc, L, [])

def zip_with(f, L1, L2):
    return list(map(lambda x: f(x[0], x[1]), zip(L1,L2)))

def count_if (f, L):
    return len(list(filter(lambda x: f(x), L)))