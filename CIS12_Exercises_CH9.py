
"""9.15.2"""
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    #return str1 == str2[::-1] """Original, accounts for palindromes, not anagrams."""
    return sorted(str1) == sorted(str2)

def anagram_finder():
    """I copied you because I initially didn't have words.txt - had to create it myself."""
    count = 0
    with open('words.txt', 'r', encoding = "utf_8") as textfile:
        for word in textfile:
            word = word.strip().lower()
            if is_anagram(word, 'takes'):
                count += 1
    print(f"Found {count} anagrams for 'takes'.")

"""9.15.3"""
def is_palindrome(str0):
    return str0 == str0[::-1]

def palindrome_finder(): # TODO: Fix.
    count = 0
    with open('words.txt', 'r', encoding = "utf_8") as textfile:
        for word in textfile:
            word = word.strip().lower()
            if len(word) >= 7 and is_palindrome(word):
                print(word)
                count += 1
    print(f"Found {count} palindromes in words.txt")

palindrome_finder()