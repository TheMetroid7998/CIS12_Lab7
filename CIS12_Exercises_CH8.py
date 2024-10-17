

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

    if word > 5:
        return print("5 letter words only!")

    if uses_any(word, chars):
        return print(f"This word is partially correct; {uses_any} is/are in the word but may or may not be in the right spot.")
    return print("This word is completely incorrect.")

