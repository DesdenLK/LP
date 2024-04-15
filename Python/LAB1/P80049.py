def count_unique(L):
    return len(set(L))


def remove_duplicates(L):
    return list(set(L))

def flatten(L):
    R = []
    for li in L:
        for e in li:
            R.append(e)
    return R


def flatten_rec(L):
    R = []
    for l in L:
        if isinstance(l, list):
            R += flatten_rec(l)
        else:
            R.append(l)
    return R