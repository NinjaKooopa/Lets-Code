# JMJ
"""
Caesar Cipher - Encrpyts a message by shifting each letter in the message some number ("key") down an alphabet.
    To decrypt the mssage, simply reverse the rotation. If the end of the alphabet is reached during a shift, 
    then continue back at the beginning. 

Example:
    Using the English: ABCDEFGHIJKLMNOPQRSTUVWXYZ, and a key of 5. Shifting "A" by 5 yields "F", "B" is "G".
        "W" is "A", since we reach the end of the alphabet before shifting 5, and "Z" is "E".

    The message "HELLO", using a key of 5, is then encrpyted to "MJQQT". To decrypt, shift in the other direction.

Objectives: 
    Assume the English alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

    1. Define a function that takes a message and and a key as parameters, 
        and output the encrypted message
    2. Define a function that takes an encrypted message and a key as parameters,
        and output the decrypted (original) message
    3. Create a class that encapsulates the encrypt/decrypt logic. 
        Allow the user to define the character set

    Bonus: Create a CLI to encrpyt/decrypt a message        
"""

DEFAULT_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_encrypt(message: str, key: int):
    encrypted_message = ''
    for letter in message:
        # Only encrypt if letter is found in the symbol string
        if 0 < DEFAULT_SYMBOLS.find(letter):
            index = (DEFAULT_SYMBOLS.index(letter) + key) % len(DEFAULT_SYMBOLS)
            encrypted_message += DEFAULT_SYMBOLS[index]
        else:
            # Just add the un-encrypted letter as is
            encrypted_message += letter

    return(encrypted_message)

def carsar_decrypt(message: str, key: int):
    decrypted_message = ''
    for letter in message:
        # Only decrpyt if letter is found in the symbols string
        if 0 < DEFAULT_SYMBOLS.find(letter):
            index = (DEFAULT_SYMBOLS.index(letter) - key) % len(DEFAULT_SYMBOLS)
            decrypted_message += DEFAULT_SYMBOLS[index]
        else:
            # Just add the un-decrypted letter as is
            decrypted_message += letter

    return(decrypted_message)

def caesar_encrypt2(message: str, key: int):
    shifted_symbols = str.maketrans(DEFAULT_SYMBOLS, DEFAULT_SYMBOLS[key:] + DEFAULT_SYMBOLS[:key])
    return(message.translate(shifted_symbols))

def caesar_decrypt2(message: str, key: int):
    shifted_symbols = str.maketrans(DEFAULT_SYMBOLS[key:] + DEFAULT_SYMBOLS[:key], DEFAULT_SYMBOLS)
    return(message.translate(shifted_symbols))

shifted_symbols = str.maketrans(DEFAULT_SYMBOLS, DEFAULT_SYMBOLS[5:] + DEFAULT_SYMBOLS[:5])

print(shifted_symbols)

m = 'HELLO WORLD'
k = 5
e = caesar_encrypt(m, k)
d = carsar_decrypt(e, k)

print('Message  : ' + m)
print('Encrypted: ' + e)
print('Decrypted: ' + d)

e2 = caesar_encrypt2(m, k)
d2 = caesar_decrypt2(e2, k)
print('E2       : ' + e2)
print('D2       : ' + d2)

