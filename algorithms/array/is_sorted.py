def is_sorted(elems: list) -> bool:
    elem = elems[0]
    for i in range(1, len(elems)):
        if (elem > elems[i]):
            return False
        elem = elems[i]
    return True


if __name__ == "__main__":
    print(is_sorted([1, 2, 3]))
    print(is_sorted([3, 2, 4]))
