
def count_vogals(phrase: str) -> int:
    vogals = 'aeiou'
    v = 0
    return len([letter for letter in phrase if letter.lower() in vogals])


def is_palindrome(word: str) -> bool:
    i = 0
    j = len(word) - 1

    while i < j:
        if (word[i] != word[j]):
            return False
        i += 1
        j -= 1
    return True


def find_duplicates(word: str) -> list:
    keys = {}
    for w in word:
        if (w in keys):
            keys[w] += 1
        else:
            keys[w] = 1
    return [key for key, val in keys.items() if val > 1]


def is_anagram(word_one: str, word_two: str) -> bool:
    if (len(word_one) != len(word_two)):
        return False
    word = {w:1 for w in word_one}
    for w in word_two:
        if (w in word_two):
            word[w] -= 1
    for val in word.values():
        if (val > 0):
            return False
    return True

def permutation(word: str, lower: int, higher: int) -> list:
    if (lower == higher):
        print(word)
    else:
        for i in range(lower, higher + 1):
            word[lower], word[i] = word[i], word[lower]
            permutation(word, lower + 1, higher)
            word[lower], word[i] = word[i], word[lower]

    

if __name__ == "__main__":
    print(count_vogals('aeiou'))
    print(is_palindrome('ana'))
    print(find_duplicates('finding'))
    print(is_anagram('decimal', 'medical'))
    print(permutation('abc', 0, len('abc')))
