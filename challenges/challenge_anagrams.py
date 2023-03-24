def sort_string(string):
    string = list(string)
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[j] < string[i]:
                string[i], string[j] = string[j], string[i]
    return "".join(string)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_word = sort_string(list(first_string.casefold()))
    second_word = sort_string(list(second_string.casefold()))
    if first_word == second_word:
        return (first_word, second_word, True)
    else:
        return (first_word, second_word, False)
