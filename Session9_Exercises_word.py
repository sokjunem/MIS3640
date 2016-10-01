fin = open('words.txt')
line = repr(fin.readline())
# https://docs.python.org/3/library/functions.html#repr

# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)


# def read_long_words():
#     for line in fin:
#         word = line.strip()
#         if len(word) > 20:
#             print(word) 

# read_long_words()


# def has_no_e(word):
#     for letter in word:
#         if letter == 'e':
#             return False
#     return True

# print(has_no_e('hi'))


# def avoids(word, forbidden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True
#     """
#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
# print(avoids('babson', 'ab'))
# print(avoids('college','ab'))


# def uses_only(word, available):
#     for letter in word:
#         if letter not in available:
#             return False
#     return True
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
# print(uses_only('babson', 'abson'))
# print(uses_only('college','ab'))


# def uses_all(word, required):
#     for letter in required:
#         if letter not in word:
#             return False
#     return True
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
# print(uses_all('babson', 'abs'))
# print(uses_all('college', 'cbs'))

# simple way
# def uses_all(word, required):
#    return uses_only(required, word)


# def is_abecedarian(word):
#     before = word[0]
#     for letter in word:
#         if letter < before:
#             return False
#         before = letter
#     return True
        
"""
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
"""

# def is_abecedarian(word):
#     before = word[0]
#     while True:
#         for letter in word:
#             if letter < before:
#                 return False
#             before = letter
#         return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('samsara'))

