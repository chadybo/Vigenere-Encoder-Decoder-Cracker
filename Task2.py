import collections
from collections import Counter
import statistics
def decrypt_func(ciphertext, cipher_key, plaintext, ciphertext_counter, cipher_key_counter, cipher_key_len):
    for char in ciphertext:

        if ciphertext[ciphertext_counter].isalpha():
            letter = ciphertext[ciphertext_counter]

            # print("CIPHER_KEY_COUNTER")
            # print(cipher_key_counter)
            shift_by = abs(ord('a') - ord(cipher_key[cipher_key_counter].lower()))
            # print("SHIFT_BY")
            # print(shift_by)

            if (ord(letter.lower()) - shift_by) < ord('a'):
                # print("IN THIS IF STATEMENT")
                new_shift = abs(ord('a') - (ord(letter.lower()) - shift_by))
                # print(new_shift)
                shift_by = new_shift - 1
                shifted_letter = chr(ord('z') - shift_by)
            else:
                shifted_letter = chr(ord(letter.lower()) - shift_by)

            if letter.isupper():
                plaintext += shifted_letter.upper()
            else:
                plaintext += shifted_letter

            ciphertext_counter = ciphertext_counter + 1
            cipher_key_counter = cipher_key_counter + 1

            if cipher_key_counter >= cipher_key_len:
                cipher_key_counter = 0
        else:
            plaintext += ciphertext[ciphertext_counter]
            ciphertext_counter = ciphertext_counter + 1
    return plaintext


ciphertext = input()
cipher_key = input()
plaintext = ""

ciphertext_counter = 0
cipher_key_counter = 0
cipher_key_len = len(cipher_key)

print(decrypt_func(ciphertext, cipher_key, plaintext, ciphertext_counter, cipher_key_counter, cipher_key_len))