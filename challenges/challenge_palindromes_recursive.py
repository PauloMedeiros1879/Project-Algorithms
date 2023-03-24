def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    # Retorna True se a palavra passada por parâmetro for um palíndromo
    if low_index > high_index:
        return True
    # Retorne False se a palavra passada por parâmetro não for um palíndromo;
    if word[low_index] != word[high_index]:
        return False
    # Retorne False se nenhuma palavra for passada por parâmetro
    if word == "":
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
