import re
import argparse
import base64
import base62
import base58

parser = argparse.ArgumentParser (
        prog='base',
        description='simple base format decoder')

parser.add_argument('string')
parser.add_argument('-f', '--format', required=True, type=int, choices=[64, 32, 16, 85, 58, 62, 2])

args = parser.parse_args()

match args.format:
    case 64:
        out = base64.b64decode(args.string)
    case 32:
        out = base64.b32decode(args.string)
    case 16:
        out = base64.b16decode(args.string)
    case 85:
        out = base64.b85decode(args.string)
    case 58:
        out = base58.b58decode(args.string)
    case 62:
        out = base62.decode(args.string)
    case 2:
        bytes([int(b, 2) for b in args.string.split()]).decode('utf-8')

print(out.decode('utf-8'))
