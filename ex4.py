def solucao(encoded):
    decoded = ''
    number = ''
    for char in encoded:
        if char.isdigit(): # Se o caractere for um número
            number += char #incrementa o número
        else: # Se o caractere não for um número
            decoded += char * int(number) if number else char # Se o número for diferente de vazio, multiplica o caractere pelo número, senão, apenas adiciona o caractere
            number = ''
    return decoded
