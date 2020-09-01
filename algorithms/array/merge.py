
def merge(array_one: list, array_two: list) -> list:
    i = 0
    j = 0
    k = 0
    size_array_one = len(array_one)
    size_array_two = len(array_two)
    result = [None] * (size_array_one + size_array_two)
    while (i < size_array_one and j < size_array_two):
        if array_one[i] < array_two[j]:
            result[k] = array_one[i]
            i += 1
        else:
            result[k] = array_two[j]
            j += 1
        k += 1

    while (i < size_array_one):
        result[k] = array_one[i]
        k += 1
        i += 1

    while (j < size_array_two):
        result[k] = array_two[j]
        k += 1
        j += 1

    return result


if __name__ == "__main__":
    array_one = [3, 8, 16, 20, 25]
    array_two = [4, 10, 12, 22, 23]
    print(merge(array_one, array_two))
