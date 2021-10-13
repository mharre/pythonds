# import string
# def find(strng, ch):
#     ix = 0
#     while ix < len(strng):
#         if strng[ix] == ch:
#             return ix
#         ix += 1
#     return -1



# def count_letters(strng, char, new_occurance = None):
#     if new_occurance is not None:
#         return (strng.find(char), strng.find(new_occurance))
#     return strng.find(char)

# print(count_letters('banana', 'n', 'shit'))

# x = """If you're looking for random paragraphs, you've come to the right place. When a random word or a random sentence isn't quite enough, the next logical step is to find a random paragraph. We created the Random Paragraph Generator with you in mind. The process is quite simple. Choose the number of random paragraphs you'd like to see and click the button. Your chosen number of paragraphs will instantly appear.

# While it may not be obvious to everyone, there are a number of reasons creating random paragraphs can be useful. A few examples of how some people use this generator are listed in the following paragraphs."""

# def clean_string(strng):
#     no_puctuation = ''
#     for letter in strng:
#         if letter not in string.punctuation:
#             no_puctuation += letter
#             str_list = no_puctuation.split()
#             word_count = len(str_list)

#     return count_e(str_list, word_count)

# def count_e(strng, word_count = None):
#     letter_count = 0
#     for word in strng:
#         for letter in word:
#             if letter in 'e':
#                 letter_count += 1
#     percentage = letter_count / word_count * 100
#     percentage = round(percentage,1)
#     return f'Your text contains {word_count} words, of which {letter_count} ({percentage}%) contain an "e"'

# print(clean_string(x))

# def remove_letter(strng, char_removal):
#     test = []
#     for letter in strng:
#         if letter not in char_removal:
#             test.append(letter)
#     test = ''.join(str(e) for e in test)
#     return test


# print(remove_letter('Mississippi', 'i'))

# def is_palindrone(strng):
#     if strng[::-1] == strng:
#         return True
#     return False

# print(is_palindrone('hello'))
