'''
    Dado um array de números(positivos e negativos) retornar a maior soma de um subarray contínuo.
    [20, 50, -1, 3] e a soma total desse trecho é 72.
'''


def s(elems):
    result = 0
    # [3, -3, 4, -2, 5, -9]
    for i in range(len(elems)):
        current_soma = elems[i]
        for j in range(i + 1, len(elems)):
            current_soma += elems[j]
            if (current_soma > result):
                result = current_soma
            print(f'i={i} j={j} soma={current_soma}')
        print(f'result={result}')
    return result


def soma_linear(elems):
    max_antes = elems[0]
    max_agora = elems[0]

    for elem in elems[1:]:
        max_antes = max(elem, max_antes + elem)
        max_agora = max(max_agora, max_antes)
    return max_agora
