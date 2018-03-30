def match_the_keyword(word, length):
    word = (word * (length // len(word))) + word[:length - len(word * (length // len(word)))]
    return word


def create_dict():
    dict = {a: chr(a + 65) for a in range(26)}
    return dict


def encrypt_vigenere(plaintext, keyword):

    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    dict = create_dict()
    if (len(keyword) < len(plaintext)):
        keyword = match_the_keyword(keyword, len(plaintext))
    else:
        pass

    plaintext = list(plaintext)
    for i in range(len(keyword)):
        if ((ord(plaintext[i].upper()) + list(dict.keys())[ord(keyword[i].upper()) - 65] > 90)):
            plaintext[i] = chr((ord(plaintext[i]) + list(dict.keys())[ord(keyword[i].upper()) - 65] - 26))
        else:
            plaintext[i] = chr(ord(plaintext[i]) + list(dict.keys())[ord(keyword[i].upper()) - 65])

    ciphertext = "".join(plaintext)

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    dict = create_dict()
    if (len(keyword) < len(ciphertext)):
        keyword = match_the_keyword(keyword, len(ciphertext))
    else:
        pass

    ciphertext = list(ciphertext)
    for i in range(len(keyword)):
        if ((ord(ciphertext[i].upper()) - list(dict.keys())[ord(keyword[i].upper()) - 65] < 65)):
            ciphertext[i] = chr((ord(ciphertext[i]) - list(dict.keys())[ord(keyword[i].upper()) - 65]) + 26)
        else:
            ciphertext[i] = chr((ord(ciphertext[i]) - list(dict.keys())[ord(keyword[i].upper()) - 65]))



    plaintext = "".join(ciphertext)
    return plaintext

