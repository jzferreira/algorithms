#!/bin/python3

from sort_tools import generate_random_list
from random import randint

def particao(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if (a[j] <= x):
            i = i + 1
            a[i],a[j] = a[j],a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return (i + 1)


def quicksort(a, p, r):
    if p < r:
        q = particao(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def random_particao(a, p, r):
    i = randint(p, r)
    a[p], a[i] = a[i], a[p]
    return particao(a, p, r)


def random_quick(a, p, r):
    if (p < r):
        q = random_particao(a, p, r)
        random_particao(a, p, q - 1)
        random_particao(a, q + 1, r)


values = generate_random_list(10000)
# print(values)
# quicksort(values, 0, len(values)-1)
# print(values)
# values2 = [4, 2, 5, 1011, 999]
random_quick(values, 0, len(values)-1)
print(values)

