import collections
from collections import Counter
import statistics

alphabet_frequencies = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

def get_group(txt, start, key_len):
    group_string = ""
    for x_counter in range(start, len(txt), key_len):
        group_string += txt[x_counter]

    return group_string


def rotationcaesarcipher(grp, shift):
    decoded_txt = ""
    char_counter = 0
    for char_frm_grp in grp:
        letter_frm_grp = grp[char_counter]

        if letter_frm_grp.isalpha():
            if (ord(letter_frm_grp) - shift) < ord('a'):
                new_shift_amt = abs((ord(letter_frm_grp) - shift) - ord('a') + 1)
                new_letter = chr(abs(ord('z') - new_shift_amt))

                if letter_frm_grp.isupper():
                    decoded_txt += new_letter.upper()
                    char_counter = char_counter + 1
                else:
                    decoded_txt += new_letter
                    char_counter = char_counter + 1
            else:
                if letter_frm_grp.isupper():
                    decoded_txt += (chr(ord(letter_frm_grp) - shift)).upper()
                    char_counter = char_counter + 1
                else:
                    decoded_txt += chr(ord(letter_frm_grp) - shift)
                    char_counter = char_counter + 1
        else:
            decoded_txt += letter_frm_grp
            char_counter = char_counter + 1

    return decoded_txt

def count_matching_positions(str1, str2, off):
        # Count matching characters at the same position
        count = 0
        # print("THIS IS OFF: ", off)
        # print("THIS IS STR1: ", str1)
        # print("THIS IS STR2: ", str2)
        for x_counting in range(len(str2) - 1):

            # print("THIS IS THE CHARACTER STR1: ", str1[x_counting])
            # print("THIS IS THE CHARACTER STR2: ", str2[x_counting])
            if str1[x_counting + off] == str2[x_counting]:
                # print("THIS IS STR1: ", str1)
                # print("THIS IS STR2: ", str2)
                # print("THIS IS THE CHARACTER: ", str1[i])
                count += 1

        return count
def decrypt_with_only_ciphertext(ciphertext, cipher_key_len, cipher_key, plaintext):
    cipher_text_clone = ciphertext[:]


    cipher_text_cleaned = ''.join([char for char in cipher_text_clone if char.isalpha()])


    lower_case_cipher_txt_cleaned = cipher_text_cleaned.lower()
    lower_case_cipher_txt_cleaned_clone = lower_case_cipher_txt_cleaned[:]

    counts_arr = []

    off = 0
    # print("THIS IS THE LENGTH OF THE CLEANED CIPHERTEXT: ", len(lower_case_cipher_txt_cleaned))
    for i in range(int(len(lower_case_cipher_txt_cleaned) * 0.5)):
        lower_case_cipher_txt_cleaned_clone = lower_case_cipher_txt_cleaned_clone[:-1]
        off = off + 1;
        # print("THIS IS STR1: ", lower_case_cipher_txt_cleaned)
        # print("THIS IS STR2: ", lower_case_cipher_txt_cleaned_clone)
        counts_arr.append(count_matching_positions(lower_case_cipher_txt_cleaned, lower_case_cipher_txt_cleaned_clone, off))

    # print(counts_arr)
    # print("THIS IS LEN OF COUNTS_ARR: ", len(counts_arr))
    avg = statistics.mean(counts_arr)
    # print(avg)

    std_dev = statistics.stdev(counts_arr)

    # print(std_dev)

    two_index_arr = []

    for x in range(len(counts_arr)):
        if counts_arr[x] >= (avg + (1.5 * std_dev)):
            # print("THIS IS THE VALUE OF COUNTS_ARR[x]: ", counts_arr[x])
            two_index_arr.append(x + 1)

    # print(two_index_arr)

    differences = [two_index_arr[i] - two_index_arr[i - 1] for i in range(1, len(two_index_arr))]

    # print(differences)

    length = statistics.mode(differences)

    # print(length)

    # length = abs(two_index_arr[0] - two_index_arr[1]) + 1
    #
    # print(length)
    # ic_val_arr = []
    # for i in range(26):
    #     decoded = rotationcaesarcipher(lower_case_cipher_txt_cleaned, i)
    #     print(decoded)
    #     bag = Counter()
    #     bag.update(decoded)
    #
    #     print(bag)
    #
    #     numerator_sum = 0
    #     for char in decoded:
    #         numerator_sum = numerator_sum + (bag[char] * (bag[char] - 1))
    #     denominator = len(decoded) * (len(decoded) - 1)
    #     ic_val = numerator_sum / denominator
    #     ic_val_arr.append(ic_val)
    #
    # print(ic_val_arr)

    # def index_of_coincidence(text):
    #     freq = Counter(text)
    #
    #     n = len(text)
    #     sum_freq = sum(f * (f - 1) for f in freq.values())
    #
    #     total_pairs = n * (n - 1)
    #
    #     ic = sum_freq / total_pairs
    #     return ic
    #
    # ic_val_final = []
    # for x in range(26):
    #     ic_val_for_set_of_groups = []
    #     for i in range (x):
    #         group = get_group(lower_case_cipher_txt_cleaned, i, x)
    #         # print(group)
    #         ic_val_for_set_of_groups.append(index_of_coincidence(group))
    #         # print(index_of_coincidence(group))
    #         # print(ic_val_for_set_of_groups)
    #     if len(ic_val_for_set_of_groups) > 0:
    #         ic_val = sum(ic_val_for_set_of_groups) / len(ic_val_for_set_of_groups)
    #         ic_val_final.append(ic_val)
    #
    # # differences = []
    #
    # print("THIS IS IC_VAL_FINAL")
    # print(ic_val_final)
    #
    # index = 0
    # for x in range(len(ic_val_final)):
    #     if ic_val_final[x] > .068 or ic_val_final[x] > .063:
    #         index = x
    #         break



    # min_value_index = differences.index(min(differences))

    cipher_key_len = length

    list_of_n_shift_values = []

    total_bags = 0

    cipher_text_clone = ciphertext[:]

    cipher_text_cleaned = ''.join([char for char in cipher_text_clone if char.isalpha()])

    lower_case_cipher_txt_cleaned = cipher_text_cleaned.lower()

    for i in range(int(cipher_key_len)):
        group = get_group(lower_case_cipher_txt_cleaned, i, int(cipher_key_len))

        list_of_twenty_six_chi_squared = []
        # print("THIS IS GROUP")
        # print(group)

        for x in range(0, 26, 1):
            decoded = rotationcaesarcipher(group, x)
            # print("THIS IS DECODED WITH SHIFT ", x)
            # print(decoded)

            bag = Counter()
            bag.update(decoded)

            total_bags = total_bags + 1

            # print("THIS IS THE BAG", bag)

            sum_chi_squared = 0

            for char in decoded:
                if char.isalpha():
                    # print("THIS IS CHAR: ", char)
                    # print("THIS IS THE BAG FREQUENCY: ", bag[char])
                    # print("THIS IS ITS ACTUAL FREQUENCY: ", alphabet_frequencies[char])
                    expected = alphabet_frequencies[char] * len(decoded)
                    chi_squared_amt = (bag[char] - expected) ** 2 / expected
                    sum_chi_squared = sum_chi_squared + chi_squared_amt
            # print("THIS IS THE SHIFT VALUE: ", x)
            # print("THIS IS DECODED: ", decoded)
            # print("THIS IS THE CHI_SQUARED AMOUNT: ", sum_chi_squared)
            list_of_twenty_six_chi_squared.append(sum_chi_squared)

        # print("THIS IS THE LIST OF TWENTY SIX VALUES:", list_of_twenty_six_chi_squared)
        # print("THIS IS THE LENGTH OF THE TWENTY SIX VALUES: ", len(list_of_twenty_six_chi_squared))
        temp_min_chi_squared_val = 0
        temp_min_chi_squared_index = 0

        # for x in range(0, 26, 1):
        #     if x == 0:
        #         temp_min_chi_squared_val = list_of_twenty_six_chi_squared[x]
        #         temp_min_chi_squared_index = x
        #     elif temp_min_chi_squared_val > list_of_twenty_six_chi_squared[x]:
        #         temp_min_chi_squared_val = list_of_twenty_six_chi_squared[x]
        #         temp_min_chi_squared_index = x

        temp_min_chi_squared_val = min(list_of_twenty_six_chi_squared)
        # print("THIS IS THE MIN CHI SQUARED VALUE: ", temp_min_chi_squared_val)
        temp_min_chi_squared_index = list_of_twenty_six_chi_squared.index(temp_min_chi_squared_val)

        list_of_n_shift_values.append(temp_min_chi_squared_index)

    # print(list_of_n_shift_values)

    for x in range(len(list_of_n_shift_values)):
        cipher_key += chr(ord('a') + list_of_n_shift_values[x]).upper()

    print(cipher_key)

    # print("CIPHERTEXT: ", ciphertext)

    plaintext = ""

    ciphertext_counter = 0
    cipher_key_counter = 0
    cipher_key_len = len(cipher_key)

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
    # print(total_bags)

    print(plaintext)


ciphertext = input()


cipher_key_len = 0
cipher_key = ""
plaintext = ""

decrypt_with_only_ciphertext(ciphertext, cipher_key_len, cipher_key, plaintext)
