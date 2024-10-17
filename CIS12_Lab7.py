#import sys

def alpha_line(header=' ', shift=0):
    """Prints a header letter and the alphabet with an offset, all separated by pipes."""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f"| {header} ", end='|')
    for letter in range(0, 26): # Goes to 26 because of header
        shifted_letter = alphabet[shift]
        print(f"| {shifted_letter} ", end='')
        shift += 1
    print(f"|")

alpha_line(' ')