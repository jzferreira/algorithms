def negative_left_side(elems: list) -> list:
    i = 0
    j = len(elems) - 1
    while (i < j):
        while (elems[i] < 0):
            i += 1
        while (elems[j] >= 0):
            j -= 1
        if (i < j):
            aux = elems[j]
            elems[j] = elems[i]
            elems[i] = aux
    return elems

if __name__ == "__main__":
    print(negative_left_side([-6, 3, -8, 10, -5, -7, -9, 12, -4, 2]))