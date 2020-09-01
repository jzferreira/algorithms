from algorithms.helpers import generate_random_list


def bubble_sort(elems: list) -> list:
    size_elems = len(elems)
    for i in range(size_elems - 1):
        for j in range(size_elems - i - 1):
            if (elems[j] > elems[j+1]):
                # troca
                elems[j], elems[j + 1] = elems[j + 1], elems[j]
    return elems


def insertion_sort(elems: list) -> list:
    for i in range(1, len(elems)):
        j = i - 1
        aux = elems[i]
        while j > -1 and elems[j] > aux:
            elems[j+1] = elems[j]
            j -= 1
        elems[j+1] = aux
    return elems


def selection_sort(elems: list) -> list:
    for i in range(len(elems) - 1):
        current = i
        for j in range(i+1, len(elems)):
            if (elems[j] < elems[current]):
                current = j
        elems[i], elems[current] = elems[current], elems[i]
    return elems


if __name__ == "__main__":
    elems = generate_random_list(10)
    print(f'Bubble Sort - Vetor original: \n -> {elems}')
    print('-----------------------')
    print(bubble_sort(elems))
    elems = generate_random_list(10)
    print(f'Insertion Sort - Vetor original: \n -> {elems}')
    print('-----------------------')
    print(insertion_sort(elems))
    elems = generate_random_list(10)
    print(f'Selection Sort - Vetor original: \n -> {elems}')
    print('-----------------------')
    print(selection_sort(elems))
