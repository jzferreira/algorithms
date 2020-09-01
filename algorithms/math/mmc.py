from algorithms.math import mdc

'''
Mínimo Múltiplo Comum
'''

def mmc(a: int, b: int) -> int:
    resposta_mdc = mdc(a, b)
    return a * (b/resposta_mdc)