import sys
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_vigenere_list():
    """Writes a line using an indexed letter and the alphabet starting from the index/going up to the index."""
    rows = []
    header = '-'
    for i in range(len(alphabet)+2):
        row = alphabet[i-2] + alphabet[i-2:] + alphabet[:i-2]
        if i == 0:
            row = '#' + alphabet[i:] + alphabet[:i]
        if i == 1:
            row = header * (len(alphabet)+1)
        rows.append(list(row))

    return rows

rows = get_vigenere_list()

def vigenere_sq(rows):
    """Adds more pretty formatting."""
    print("Printing Vigenère Square...")
    get_vigenere_list()
    for row in rows:
        if '-' in row[1]:
            print(f"{'|---' * len(row)}|")
        else:
            print(f'| {' | '.join(row)} | ')

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
    try:
        if isinstance(char, str):
            if len(char) != 1 or not char.isalpha or char == ' ':
                raise ValueError("Input must be a single alphabet letter.")
            else:
                return letter_to_index(char)
        elif isinstance(char, int):
            if 0 <= char <= 25:
                return index_to_letter(char)
            else:
                raise IndexError("Integer must between 0 and 25.")
        else:
            raise TypeError("Input must be a string or an integer.")

    except (ValueError, TypeError, IndexError) as error:
        print(f"An error occurred:\n{error}\n")
        return main_menu()
    except Exception as error:
        print(f"An unexpected error occurred:\n{error}\n")
        return main_menu()

def vigenere_index(key, ptext):
    """Converts a single letter from the key and the plaintext and returns a matching ciphertext letter."""
    k_index = letter_conversion(key)
    p_index = letter_conversion(ptext)
    c_index = (k_index + p_index) % 26
    c_text = letter_conversion(c_index)
    return c_text

def plaintext_index(key, ctext):
    """Converts a single letter from the key and the ciphertext and returns a matching plaintext letter."""
    k_index = letter_conversion(key)
    c_index = letter_conversion(ctext)
    p_index = (c_index - k_index) % 26
    p_text = letter_conversion(p_index)
    return p_text

def vigenere_encrypt(plaintext, key):
    """Converts a single letter from the key and the plaintext and returns a matching ciphertext letter."""
    #crypt_menu(mode='Encrypt')
    #key = crypt_menu[1]()
    #plaintext = crypt_menu[0]()
    cipherlist = []
    key_length = len(key)
    for i, char in enumerate(plaintext):
        cipherlist.append(vigenere_index(key[i%key_length], char))
    ciphertext = ''.join(cipherlist)
    print(f"Your encrypted text is {ciphertext}.")
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """Converts a single letter from the key and the ciphertext and returns a matching plaintext letter."""
    #crypt_menu(mode='Decrypt')
    #key = crypt_menu[1]()
    #ciphertext = crypt_menu[0]()
    plainlist = []
    key_length = len(key)
    for i, char, in enumerate(ciphertext):
        plainlist.append(plaintext_index(key[i%key_length], char))
    plaintext = ''.join(plainlist)
    print(f"Your decrypted text is {plaintext}.")
    return plaintext

menu_list = [
    ['1. Encrypt', lambda: vigenere_encrypt(*crypt_menu(mode='Encrypt'))],
    ['2. Decrypt', lambda: vigenere_decrypt(*crypt_menu(mode='Decrypt'))],
    ['3. Print Vigenère Square', lambda: vigenere_sq(get_vigenere_list())],
    ['0. Quit', lambda: sys.exit()],
    [1, 2, 3, 0]
    ] # Used lambdas because they were recommended by ChatGPT, looked into them though.
      # As I understand it, lambdas are like small, temporary functions for one-time use.

def crypt_menu(mode=''):
    """Accepts the mode (Encrypt/Decrypt) and collects/validates input as needed
    before passing the key and the text to the appropriate function."""
    try:
        text = input(f"Please enter the text you wish to {mode}:\n").upper().strip()
        if not all(char in alphabet for char in text):
            raise ValueError("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        key = input(f"Please enter the key to {mode} this text with:\n").upper().strip()
        if not all(char in alphabet for char in key):
            raise ValueError("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        return [text, key]

    except ValueError as error:
        print(f"An error occurred:\n{error}\n")
        return crypt_menu(mode)

    except Exception as error:
        print(f"An unexpected error occurred:\n{error}\n")
        return main_menu()

def main_menu():
    """Lists the possible functions in menu_list, and accepts input
    before running the appropriate sequence of functions."""
    while True:
        for i in range(len(menu_list) - 1):
            print(menu_list[i][0])
        try:
            selected = int(input("Make a selection:\n"))
            if selected == 0:
                print("Exiting...")
                menu_list[3][1]()
            elif selected in (1, 2, 3):
                menu_list[selected - 1][1]()
            else:
                raise Exception("Invalid selection, please try again.")

        except Exception as error:
            print(f"An error occurred.\n{error}\nLet's try again.")
            main_menu()

main_menu()