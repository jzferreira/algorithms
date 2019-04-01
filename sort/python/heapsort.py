#!/bin/python3

from sort_tools import generate_random_list

def max_heapify(a, n, i):
    largest = i #inicia o maior elementos como raiz
    l = 2 * i + 1 #desloca para a esquerda + 1
    r = 2 * i + 2 #desloca para a direita +1

    #veja se o filho da esquerda da raiz existe e 
    # se é maior que a raiz
    if (l < n and a[i] < a[l]):
        largest = l
    
    #veja se o filho da direita da raiz existe e
    #  se é maior que a raiz
    if (r < n and a[largest] < a[r]) :
        largest = r

    #muda o root, se necessário
    if largest != i:
        a[i], a[largest] = a[largest], a[i] #troca

        #max_heapify a raiz
        max_heapify(a, n, largest)
    

def heapsort(a):
    n = len(a) #numero de elementos

    #constroi o maxhep
    for i in range (n, -1, -1):
        max_heapify(a, n, i)
    
    #um por um extrai os elementos
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i] # swap
        max_heapify(a, i, 0)
    
    return a


values = generate_random_list(1000000)
values = heapsort(values)
print(values)