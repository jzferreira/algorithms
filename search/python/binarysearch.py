#!/bin/python


def binary_search(a, chave, size):
    inf = 0  # limite inferior
    sup = size - 1  # limite superior
    meio = None
    while (inf <= sup):
        meio = int((inf + sup)/2)
        if (chave == a[meio]):
            return meio, a[meio]
        if (chave < a[meio]):
            sup = meio - 1
        else:
            inf = meio + 1

    return -1


def binary_search_recursively(x, v, e, d):
    meio = int((e + d)/2)
    if (v[meio] == x):
        return meio, v[meio]
    if (e >= d):
        return -1
    else:
        if (v[meio] < x):
            return binary_search_recursively(x, v, meio+1, d)
        else:
            return binary_search_recursively(x, v, e, meio - 1)


values = [1,3,5,6,7,8,9,0]
print(binary_search(values, 8, len(values)))
