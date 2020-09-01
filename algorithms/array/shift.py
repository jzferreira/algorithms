from algorithms.helpers import generate_random_list

def shift(elems: list) -> list:
    if (len(elems) > 0):
        pos = 0
        while (pos < len(elems) - 1):
            elems[pos] = elems[pos+1]
            elems[pos+1] = 0
            pos += 1
    return elems

if __name__ == "__main__":
    values = generate_random_list(10)
    print(f'List original: {values}')
    print('----------------------------')
    print(shift(values))
