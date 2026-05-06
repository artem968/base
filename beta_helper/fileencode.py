import base64
import base58
import base62
import argparse

parser = argparse.ArgumentParser (
        prog='base',
        description='simple base format file encoder')

parser.add_argument('filename')
#parser.add_argument('-f', '--format', required=True, type=int, choices=[64, 32, 16, 85, 58, 62, 2])

args = parser.parse_args()

CHUNK_SIZE = 1024

try:
    with open(args.filename, "rb") as file:
        while True:
            chunk = file.read(CHUNK_SIZE)

            if not chunk:
                break

            print(base64.b64encode(chunk).decode("utf-8"), end="")

            #print(f"Read a chunk of {len(chunk)} bytes.")

except FileNotFoundError:
    print("file {args.filename} not found")


