from CaesarCipherClass import CaesarCipher
from argparse import ArgumentParser, BooleanOptionalAction

parser = ArgumentParser()
parser.add_argument('-e', dest='encrypt', type=bool, action=BooleanOptionalAction, help='Encrpyt the message')
parser.add_argument('-d', dest='decrypt', type=bool, action=BooleanOptionalAction, help='Decrypt the message')
parser.add_argument('-k', dest='key', type=int, help='Key used to encrypt/decrypt the message')
parser.add_argument('message', nargs='+')
args = parser.parse_args()

if args.key is None:
    raise AttributeError('The following arguments are required: -k')

if args.message is None:
    raise AttributeError('The following arguments are required: message')

if '' == args.message:
    raise AttributeError('The message parameter cannot be empty')

if args.encrypt and args.decrypt:
    raise AttributeError('Cannot pass -e and -d. Use one or the other')

c = CaesarCipher(key=args.key)