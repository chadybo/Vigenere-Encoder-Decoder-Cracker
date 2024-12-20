import collections
from collections import Counter
import statistics


def encrypt_func(plaintext, cipher_key):
    ciphertext = ""
    plaintext_counter = 0
    cipher_key_counter = 0
    cipher_key_len = len(cipher_key)

    for char in plaintext:
        if plaintext[plaintext_counter].isalpha():
            letter = plaintext[plaintext_counter]
            shift_by = abs(ord('a') - ord(cipher_key[cipher_key_counter].lower()))

            if (ord(letter.lower()) + shift_by) > ord('z'):
                new_shift = abs(ord('z') - (ord(letter.lower()) + shift_by))
                shift_by = new_shift - 1
                shifted_letter = chr(ord('a') + shift_by)
            else:
                shifted_letter = chr(ord(letter.lower()) + shift_by)

            if letter.isupper():
                ciphertext += shifted_letter.upper()
            else:
                ciphertext += shifted_letter

            plaintext_counter += 1
            cipher_key_counter += 1

            if cipher_key_counter >= cipher_key_len:
                cipher_key_counter = 0
        else:
            ciphertext += plaintext[plaintext_counter]
            plaintext_counter += 1

    return ciphertext


plaintext = input()
cipher_key = input()

print(encrypt_func(plaintext, cipher_key))
