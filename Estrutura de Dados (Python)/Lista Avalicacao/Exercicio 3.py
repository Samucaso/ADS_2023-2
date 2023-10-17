def palindromo(palavra, lista):
    letras_invert = lista[::-1]
    if len(palavra) == 0:
        if letras_invert == lista:
            return "é palindromo"
        else:
            return "não é palindromo"

    lista.append(palavra[0])
    return palindromo(palavra[1:], lista)


letras = []
print(palindromo("ana", letras))
