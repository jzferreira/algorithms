#!/bin/python3

from sort_tools import generate_random_list


def bubble_sort(a):
    size = len(a)
    for i in range(size):
        for j in range(size - i - 1):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]

    return a


values = generate_random_list(100)
print(bubble_sort(values))
