""" Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.
"""
# this is mostly solid but still have to figure out the nitty gritty details

n = 2
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = []
for letter in alphabet_string:
    alphabet_list.append(letter)

input_string = 'abcdefghijklmnopqrstuvwxyz'
output_string = ""

for letter in input_string:
    if letter != " ":
        if letter in alphabet_list:
            list_index = alphabet_list.index(letter)
            if list_index <= len(alphabet_list)-n-1:
                letter = alphabet_list[list_index+n]
                output_string += letter
            if list_index >= len(alphabet_list)-n-1:
                letter = alphabet_list[(list_index+n)-26]
                output_string += letter
    if letter == " ":
        output_string += letter
print(output_string)
