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


def dec_symbol(symbol):
    ascii_number = ord(symbol)

    if ((ascii_number >= 65 and ascii_number <= 90) or (ascii_number >= 97 and ascii_number <= 122)):
        if (symbol == "c" or symbol == "C"):
            return chr(ascii_number + 23)
        elif (symbol == "b" or symbol == "B"):
            return chr(ascii_number + 23)
        elif (symbol == "a" or symbol == "A"):
            return chr(ascii_number + 23)

        return chr(ord(symbol) - 3)
    else:
        return symbol


def encrypt_caesar(plaintext):
    
    """
        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
    """

    ciphertext = ''.join(list(map(lambda x: inc_symbol(x), list(plaintext))))
    return ciphertext


def decrypt_caesar(ciphertext):

    """
       >>> decrypt_caesar("SBWKRQ")
       'PYTHON'
       >>> decrypt_caesar("sbwkrq")
       'python'
       >>> decrypt_caesar("Sbwkrq3.6")
       'Python3.6'
       >>> decrypt_caesar("")
       ''
    """

    plaintext = ''.join(list(map(lambda x: dec_symbol(x), list(ciphertext))))
    return plaintext
