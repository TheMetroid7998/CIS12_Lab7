import re

"""8.12.2 -- Brought to you by ChatGPT"""
def head_dirty(file_path, lines, output_path):
    file = open(file_path, 'r')

    output_file = None
    if output_path:
        output_file = open(output_path, 'w')

    line_count = 0
    while line_count < lines:
        line = file.readline()
        if not line:
            break
        if output_file:
            output_file.write(line)
        else:
            print(line, end='')
        line_count += 1

    file.close()
    if output_file:
        output_file.close()

def head_clean(file_path, lines, output_path):
    with open(file_path, 'r') as file:
        output_file = None
        if output_path:
            with open(output_path, 'w') as output_file:
                line_count = 0
                while line_count < lines:
                    line = file.readline()
                    if not line:
                        break
                    output_file.write(line)
                    line_count += 1
        else:
            line_count = 0
            while line_count < lines:
                line = file.readline()
                if not line:
                    break
                print(line, end='')
                line_count += 1

"""8.12.3"""
def uses_any(word, chars):
    word = word.lower()
    chars = chars.lower()
    matching_chars = [char for char in word if char in chars]

    if matching_chars:
        return matching_chars
    return None

def wordle(word, chars, answer):
    word = word.strip().lower()
    chars = chars.strip.lower()
    pass

def check_word(word):
    if len(word) > 5:
        return print("5 letter words only!")
    else: pass

    pattern = r'\b(?: \w{2} E \w | \w{4} E \w | \w_[chars]\w_)\b'
    # okay, fairly new to this... had to copy you. as I understand it,
    # you have the word boundary \b
    # I dont really get the ?: thing, moving on...
    # \w{2} takes any two characters, then a capital E then any one character OR
    # \w{4} takes any four characters, then E, then any one character OR
    # \w takes any one character, [] takes any of the set of characters, then any one character
    if not re.match(pattern, word, re.IGNORECASE):
        return False, print("This word is incorrect.")
    else: return True

def give_clue():
    count = 0
    with open('words.txt', 'r') as file:
        for word in file:
            word = word.strip()
            if len(word) == 5 and check_word(word):
                print(word)
                count += 1

    print(f"A total of {count} words could still match.")

"""8.12.5"""

def word_check():
    with open('TheCountofMnteCristo.txt', 'r') as book:
        count = 0
        for line in book:
            pattern = r'\b(?:pale(s | d | ness)? | pallor)\b'
            sentence = line.strip()
            if re.match(pattern, sentence):
                print(line)
                count += 1

    print(f"Lines with some form of pale: {count}")