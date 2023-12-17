# JMJ
class CaesarCipher:
    _DEFAULT_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, symbols: str = '', *, key: int):
        self._symbols = self._DEFAULT_SYMBOLS
        if '' != symbols:
            self._symbols = symbols

        self._key = key

    def encrypt_message(self, message):
        shifted_symbols = str.maketrans(self._symbols, self._symbols[self._key:] + self._symbols[:self._key])
        return(message.translate(shifted_symbols))
    
    def decrypt_message(self, message):
        shifted_symbols = str.maketrans(self._symbols[self._key:] + self._symbols[:self._key], self._symbols)
        return(message.translate(shifted_symbols))

c1 = CaesarCipher(key=5)
e = c1.encrypt_message('HELLO WORLD')
d = c1.decrypt_message(e)

print('e: ' + e)
print('d: ' + d)