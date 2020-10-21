def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for c in plaintext:
        if not c.isalpha():
            ciphertext += c
            continue
        num = ord(c.lower()) + shift
        while num > 122:
            num -= 26
        if c.isupper():
            new_chr = chr(num).upper()
        else:
            new_chr = chr(num)
        ciphertext += new_chr

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for c in ciphertext:
        if not c.isalpha():
            plaintext += c
            continue
        num = ord(c.lower()) - shift
        while num < 97:
            num += 26
        if c.isupper():
            new_chr = chr(num).upper()
        else:
            new_chr = chr(num)
        plaintext += new_chr
    return plaintext


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for ind, character in enumerate(plaintext):
        shift = ord(keyword[ind % len(keyword)].lower()) - 97
        ciphertext += encrypt_caesar(character, shift)

    return ciphertext





def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    for ind, character in enumerate(ciphertext):
        shift = ord(keyword[ind % len(keyword)].lower()) - 97
        plaintext += decrypt_caesar(character, shift)

    return plaintext

