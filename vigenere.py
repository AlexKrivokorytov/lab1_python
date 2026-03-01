import string
from collections import deque

def vigenere_decrypt(cipher_text, key):
    alphabet = string.ascii_lowercase
    decrypted = []

    key_length = len(key)

    for i, char in enumerate(cipher_text):
        shift = alphabet.index(key[i % key_length])

        rotated = deque(alphabet)

        rotated.rotate(shift)

        index = alphabet.index(char)

        decrypted.append(rotated[index])

    return "".join(decrypted)


cipher_text = "dlxioqephnfnbkxyqncixldncwypjrimiucgrfiyctgyftsehznzm"
key = "python"

result = vigenere_decrypt(cipher_text, key)
print(result)
