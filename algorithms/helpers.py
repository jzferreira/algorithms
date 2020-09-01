from random import randint, seed

def generate_random_list(size):
    seed()
    elems = []
    for _ in range(size):
        elems.append(randint(0, size))
    return elems
