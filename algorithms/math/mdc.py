import time

'''
Máximo Divisor Comum - Algoritmo de Euclides
Versão recursiva e iterativa
'''

def mdc_recursive(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return mdc_recursive(b, a % b)


def mdc(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a = b
        b = r
    return a