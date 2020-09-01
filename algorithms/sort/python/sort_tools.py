#!/bin/python3
from random import randint
from random import seed


def generate_random_list(size):
    seed(1)
    elems = []
    for _ in range(size):
        elems.append(randint(0, size))
    return elems
