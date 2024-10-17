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