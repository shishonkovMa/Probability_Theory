from itertools import product

omega = set(product(['H', 'T'], repeat=20))

A = {om for om in omega if om.count('H') % 2 == 0}
B = {om for om in omega if om.count('T') < 4}


def cond_prob(x, y):
    return len(x & y) / len(y)

# print(cond_prob(A,B))
