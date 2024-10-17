#import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_vigenere_list():
    rows = []
    header = '-'
    for i in range(len(alphabet)+2):
        row = alphabet[i-2] + alphabet[i-2:] + alphabet[:i-2]
        if i == 0:
            row = '#' + alphabet[i:] + alphabet[:i]
        if i == 1:
            row = header * (len(alphabet)+1)
        #print(list(row))
        rows.append(list(row))

    return rows

def vigenere_sq(rows):
    get_vigenere_list()
    for row in rows:
        if '-' in row[1]:
            print(f"{'|---' * len(row)}|")
        else:
            print(f'| {' | '.join(row)} | ')

vigenere_sq(get_vigenere_list())

def letter_to_index(letter):
    """Converts an alphabetic letter to an index in range 0 - 25."""
    alpha_letter = str(letter).upper()
    alpha_index = alphabet.find(alpha_letter)
    return alpha_index

def index_to_letter(number):
    """Converts an index value in range 0 - 25 to an alphabetic letter."""
    alpha_index = int(number)
    alpha_letter = alphabet[alpha_index]
    return alpha_letter

def letter_conversion(char):
    """Determines the type of input, validates it, and passes to the appropriate conversion function."""
    if isinstance(char, str):
        if len(char) != 1 or not char.isalpha or char == ' ':
            raise ValueError("Input must be a single alphabet letter.")
        else:
            return letter_to_index(char)
    elif isinstance(char, int):
        if 0 <= char <= 25:
            return index_to_letter(char)
        else:
            raise Exception("Integer must between 0 and 25.")
    else:
        raise Exception("Input must be a string or an integer.")

def vigenere_index(key, ptext):
    """Converts a single letter from the key and the plaintext and returns a matching ciphertext letter."""
    k_index = letter_conversion(key)
    p_index = letter_conversion(ptext)
    c_index = (k_index + p_index) % 26
    c_text = letter_conversion(c_index)
    return c_text

