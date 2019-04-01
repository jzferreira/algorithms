#!/bin/python3

from sort_tools import generate_random_list

def selection_sort(a):
    for i in range(len(a)):
        current = i
        for j in range(i+1, len(a)):
            if (a[current]) > a[j]:
                current = j
        
        a[i], a[current] = a[current], a[i]
    return a


values = generate_random_list(10000)
print(selection_sort(values))
                
