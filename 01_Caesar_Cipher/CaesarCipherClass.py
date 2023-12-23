# JMJ
class CaesarCipher:
    _DEFAULT_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, symbols: str = '', *, key: int):
        self._symbols = self._DEFAULT_SYMBOLS
        if '' != symbols:
            self._symbols = symbols

        self._key = key

    def encrypt_message(self, message: str) -> str:
        shifted_symbols = str.maketrans(self._symbols, self._symbols[self._key:] + self._symbols[:self._key])
        return(message.upper().translate(shifted_symbols))
    
    def decrypt_message(self, message: str) -> str:
        shifted_symbols = str.maketrans(self._symbols[self._key:] + self._symbols[:self._key], self._symbols)
        return(message.upper().translate(shifted_symbols))

if '__main__' == __name__:
    c = CaesarCipher(key=5)
    print(c.encrypt_message("Hello"))