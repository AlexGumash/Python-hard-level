def inc_symbol(symbol):
    ascii_number = ord(symbol)

    if ((ascii_number >= 65 and ascii_number <= 90) or (ascii_number >= 97 and ascii_number <= 122)):
        if (symbol == "x" or symbol == "X"):
            return chr(ascii_number - 23)
        elif (symbol == "y" or symbol == "Y"):
            return chr(ascii_number - 23)
        elif (symbol == "z" or symbol == "Z"):
            return chr(ascii_number - 23)

        return chr(ord(symbol) + 3)
    else:
        return symbol


def encrypt_caesar(plaintext):
    ciphertext = ''.join(list(map(lambda x: inc_symbol(x), list(plaintext))))
    return ciphertext

print(encrypt_caesar("Python3.6"))