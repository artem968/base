import argparse
import base58
import base62
import base64

def get_file_bytes(args):
    try:
        with open (args.file, "rb") as file:
            while True:
                chunk = file.read(args.chunk_size)

                if not chunk:
                    break

                yield chunk
    except FileNotFoundError:
        print("file not found")

def encode_file(args, stream):
    for chunk in stream:
        match args.format:
            case 16:
                print(base64.b16encode(chunk).decode('utf-8'), end="")
            case 32:
                print(base64.b32encode(chunk).decode('utf-8'), end="")
            case 58:
                print(base58.b58encode(chunk).decode('utf-8'), end="")
            case 62:
                print(base62.encodebytes(chunk).decode('utf-8'), end="")
            case 64:
                print(base64.b64encode(chunk).decode('utf-8'), end="")
            case 85:
                print(base64.b85encode(chunk).decode('utf-8'), end="")

def encode(args, byte_data):
    match args.format:
        case 16:
            print(base64.b16encode(byte_data).decode('utf-8'), end="")
        case 32:
            print(base64.b32encode(byte_data).decode('utf-8'), end="")
        case 58:
            print(base58.b58encode(byte_data).decode('utf-8'), end="")
        case 62:
            print(base62.encodebytes(byte_data).decode('utf-8'), end="")
        case 64:
            print(base64.b64encode(byte_data).decode('utf-8'), end="")
        case 85:
            print(base64.b85encode(byte_data).decode('utf-8'), end="")

def main():
    parser = argparse.ArgumentParser(
            prog='base',
            description='simple base format encoder and decoder')

    parser.add_argument('string', nargs='?', default='')
    parser.add_argument('--file', type=str)

    parser.add_argument('-f', '--format', required=True, type=int, choices=[16, 32, 58, 62, 64, 85])
    parser.add_argument('--chunk_size', type=int, default=1024)

    args = parser.parse_args()

    if args.file:
        stream = get_file_bytes(args)
        encode_file(args, stream)
    else:
        byte_data = args.string.encode('utf-8')
        encode(args, byte_data)

if __name__ == "__main__":
    main()
