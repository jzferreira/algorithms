def search(elems: list, target: int) -> int:
    pos = 0
    for elem in elems:
        if elem == target:
            return pos
        pos += 1
    return -1


def binary_search(elems: list, target: int) -> int:
    lower = 0
    higher = len(elems) - 1
    while lower <= higher:
        middle = (lower + higher) // 2
        if (target == elems[middle]):
            return middle
        elif (target < elems[middle]):
            higher = middle - 1
        else:
            lower = middle + 1
    return -1


def binary_search_recursive(elems: list, lower: int, higher: int, target: int) -> int:
    middle = (lower + higher)//2
    if (target == elems[middle]):
        return middle
    if lower >= higher:
        return -1
    elif (target < elems[middle]):
        return binary_search_recursive(elems, lower, middle - 1, target)
    else:
        return binary_search_recursive(elems, middle + 1, higher, target)


def max_elem(elems: list) -> int:
    maximum = elems[0]
    for pos in range(1, len(elems)):
        if (maximum < elems[pos]):
            maximum = elems[pos]
    return maximum


def min_elem(elems: list) -> int:
    minimun = elems[0]
    for pos in range(1, len(elems)):
        if (minimun > elems[pos]):
            minimun = elems[pos]
    return minimun


'''
Ex array: [1,2,3,4,5,6,8,9,10,11,12]
Para encontrar o elemento faltante em um vetor ordenado.
Vamos usar a formula = (n*(n+1))/2 onde n é o valor do último
elemento, ou seja, o maior.
'''


def missing_element(elems: list) -> int:
    sorted(elems)
    n = elems[-1]
    sum_last_number = n*(n+1) // 2
    sum_elems = sum(elems)
    return sum_last_number - sum_elems


'''
Ex array: [6,7,8,9,11,12,15,16,17,18,19]
Multiplos elementos que estão perdidos na lista ordenada
'''


def missing_multiple_elements(elems: list) -> list:
    sorted(elems)
    response = []
    diff = elems[0]
    for i in range(len(elems)):
        if (elems[i] - i != diff):
            while (diff < elems[i] - i):
                response.append(diff + i)
                diff += 1
    return response


def missing_elements_not_sorted(elems: list) -> list:
    response = []
    maximum = max_elem(elems)
    minimun = min_elem(elems)
    keys = {key: 0 for key in range(maximum+1)}
    for i in range(len(elems)):
        keys[elems[i]] += 1
    i = minimun
    while (i <= maximum):
        if keys[i] == 0:
            response.append(i)
        i += 1
    return response

# WITH BUG


def find_duplicates(elems: list) -> list:
    response = []
    lastDuplicate = 0
    for i in range(len(elems) - 1):
        if (elems[i] == elems[i + 1] and elems[i] != lastDuplicate):
            response.append(elems[i])
            lastDuplicate = elems[i]
    return response


def find_pair_sum(elems: list, key: int) -> list:
    pairs = []
    size_elems = len(elems)
    for i in range(size_elems - 1):
        for j in range(i+1, size_elems):
            if (elems[i] + elems[j]) == key:
                pairs.append((elems[i], elems[j]))
    return pairs


def find_pair_sum_linear(elems: list, key: int) -> list:
    pairs = []
    i = 0
    j = len(elems) - 1
    while i < j:
        current_sum = elems[i] + elems[j]
        if (current_sum == key):
            pairs.append((elems[i], elems[j]))
            i += 1
            j -= 1
        elif (current_sum < key):
            i += 1
        else:
            j -= 1
    return pairs

def find_pair_product(elems: list, key: int) -> list:
    pairs = []
    size_elems = len(elems)
    for i in range(size_elems - 1):
        for j in range(i + 1, size_elems):
            if (elems[i] * elems[j] == key):
                pairs.append((elems[i], elems[j]))
    return pairs


if __name__ == "__main__":
    # elems = [4, 8, 10, 15, 18, 21, 24, 27, 29, 33, 34, 37, 39, 41, 43]
    # print(search(elems, 2))
    # print(search(elems, 39))
    # print(binary_search(elems, 2))
    # print(binary_search(elems, 34))
    # print(binary_search_recursive(elems, 0, len(elems), 2))
    # print(binary_search_recursive(elems, 0, len(elems) ,34))
    # print(max_elem(elems=[4, 8, 10, 15, 18, 21,
    #                       24, 27, 50, 33, 34, 37, 39, 41, 43]))
    # print(min_elem(elems=[4, 8, 10, 15, 18, 21,
    #                       24, 27, 50, 33, 34, 37, 39, 41, 43]))

    # print(missing_element([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]))
    # print(missing_multiple_elements([6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]))
    # print(missing_elements_not_sorted([3, 7, 4, 9, 12, 6, 1, 11, 2, 10]))
    # print(find_duplicates([1,2,461,2,5,6,7,6,5,8]))
    print(find_pair_sum([6, 3, 8, 10, 16, 7, 5, 2, 9, 14], 10))
    print(find_pair_sum_linear([3,2,4], 6))
    print(find_pair_product([2,3,4,6,9], 18))