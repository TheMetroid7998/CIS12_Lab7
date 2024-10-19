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

def main_menu():
    menu_items = ['Encrypt', 'Decrypt', 'Quit']
    #menu_functions = [vigenere_encrypt, vigenere_decrypt, sys.exit()]
    try:
        print("Please make a selection.")
        for i, item in enumerate(menu_items):
            print(i+1, item)
            i += 1
            if i >= 2: break
        if 'Quit' in menu_items[2]:
            print('0', menu_items[2])

        select = input("\n").strip()
        if select.isalpha() or not 0 <= int(select) <= 2:
            raise Exception("Invalid selection. Please try again.")
        """
        if select == 1:
            menu_functions[0]()
        elif select == 2:
            menu_functions[1]()
        elif select == 0:
            menu_functions[3]()
        """
    except Exception as error:
        print(f"An error occurred.\n{error}\nLet's try again.")
        main_menu()

"""
def vigenere_encrypt(plaintext, key):
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
    ['1. Encrypt', vigenere_encrypt],
    ['2. Decrypt', vigenere_decrypt],
    ['3. Print Vigenère Square', vigenere_sq, get_vigenere_list],
    ['0. Quit', lambda: sys.exit()],
    [1, 2, 3, 0]
    ]

def crypt_menu(mode=''):
    try:
        text = input(f"Please enter the text you wish to {mode}:\n").upper().strip()
        if not all(char in alphabet for char in text):
            raise Exception("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        key = input(f"Please enter the key to {mode} this text with:\n").upper().strip()
        if not all(char in alphabet for char in text):
            raise Exception("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        return [text, key]
    except Exception as error:
        print(f"An error occurred.\n{error}\nLet's try again.")

def main_menu():
    while True:
        for i in range(len(menu_list)-1):
            print(menu_list[i][0])
        try:
            selected = int(input("Make a selection:\n"))
            if selected == 0:
                print("Exiting...")
                menu_list[3][1]()
            elif selected in (1, 2):
                text, key = crypt_menu(mode='Encrypt' if selected == 1 else 'Decrypt')
                menu_list[selected - 1][1](text, key)
            elif selected == 3:
                print("Printing Vigenère Square...")
                menu_list[2][1](rows)
                print("\n")
            else:
                raise Exception("Invalid selection, please try again.")

        except Exception as error:
            print(f"An error occurred.\n{error}\nLet's try again.")
            main_menu()

main_menu()
"""