from algorithms.helpers import generate_random_list
'''
A ideia entender os algoritmos de reverse. Por favor, no mundo real
utilize list.reverse().

Primeiro Algoritmo:
Você pode utilizar um array com o mesmo tamanho do original e ir salvando
os valores.

Podemos iniciar o reverse_elems = [] e para inserir elementos, nós usamos
reverse_elems.append(elems[i]). Nesse caso, a variável j não é necessária.

Segundo Algoritmo:
Podemos fazer uma troca de valores com o inicio e fim até os indices serão
iguais.
'''
def reverse_copy(elems: list) -> list:
    reverse_elems = [None] * len(elems)
    i = len(elems) - 1
    j = 0
    while (i >= 0):
        reverse_elems[j] = elems[i]
        i -= 1
        j += 1
    return reverse_elems

def reverse(elems: list) -> list:
    i = 0
    j = len(elems) - 1
    while (i < j):
        first = elems[i]
        last = elems[j]
        elems[i] = elems[j]
        elems[j] = first
        i += 1
        j -= 1
    return elems

if __name__ == "__main__":
    values = generate_random_list(10)
    print(f'List original: {values}')
    print('----------------------------')
    print(reverse_copy(values))
    print(reverse(values))
    
