import base64
import base58
import base62
import argparse

parser = argparse.ArgumentParser (
        prog='base',
        description='simple base format encoder')

parser.add_argument('string')
parser.add_argument('-f', '--format', required=True, type=int, choices=[64, 32, 16, 85, 58, 62, 2])

args = parser.parse_args()

match args.format:
    case 64:
        out = base64.b64encode(args.string.encode('utf-8')).decode('utf-8')
    case 32:
        out = base64.b32encode(args.string.encode('utf-8')).decode('utf-8')
    case 16:
        out = base64.b16encode(args.string.encode('utf-8')).decode('utf-8')
    case 85:
        out = base64.b85encode(args.string.encode('utf-8')).decode('utf-8')
    case 58:
        out = base58.b58encode(args.string.encode('utf-8')).decode('utf-8')
    case 62:
        out = base62.encodebytes(args.string.encode('utf-8'))
    case 2:
        out = ''.join(format(byte, '08b') for byte in args.string.encode('utf-8'))
    case _:
        out = "later"

print(out)
