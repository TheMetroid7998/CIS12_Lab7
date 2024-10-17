#import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alpha_line(header=' ', index=0):
    """Prints a header letter and the alphabet with an offset, all separated by pipes."""
    print(f"| {header} ", end='|')
    for letter in range(0, 26): # Goes to 26 because of the header column
        letter_index = alphabet[index % 26]
        print(f"| {letter_index} ", end='')
        index += 1
    print(f"|")

def header_line():
    """Prints a header and 26 columns of dashes, separated by pipes."""
    print(f"|---", end='|')
    for _ in range(26):
        print(f"|---", end='')
    print(f"|")

def vigenere_sq(header=' ', index=0):
    """Prints an initial 27 columns with the alphabet, a header line of dashes, and 26 rows of the alphabet with increasing offsets."""
    alpha_line(' ')
    header_line()
    for index in range(26):
        header = alphabet[index]
        alpha_line(header, index)

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

print(letter_conversion(' '), "Should be error")