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


def caesar_cipher(message, n):
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    for letter in alphabet_string:
        alphabet_list.append(letter)
    input_string = message
    encoded_message = ""

    for letter in input_string:
        if letter != " ":
            if letter in alphabet_list:
                letter_index = (alphabet_list.index(letter)+int(n))
                if letter_index <= 25:
                    encoded_message += alphabet_list[letter_index]
                if letter_index > 25:
                    letter_index = letter_index-26
                    encoded_message += alphabet_list[letter_index]
        if letter == " ":
            encoded_message += letter
    return encoded_message                    


secret_message = str(input('Please enter the secret message you want to encode...\n')).lower()
try:
    letter_shift_value = input('What would you like the shift value of the cipher to be?\n')
except:
    print('Could not convert the cipher value to an integer')
    exit()    
final_solution = caesar_cipher(secret_message, letter_shift_value)                
print(final_solution)
