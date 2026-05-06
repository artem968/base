import re
import argparse

parser = argparse.ArgumentParser (
        prog='identify',
        description='simple base format identifier')

parser.add_argument('string')

args = parser.parse_args()

def identify(s):
    # Dictionary requires "Key": "Value" pairs
    patterns = {
        "Base2":  r"^[01]+$",
        "Base16": r"^[0-9a-fA-F]+$",
        "Base32": r"^[A-Z2-7]+=*$",
        "Base58": r"^[1-9A-HJ-NP-Za-km-z]+$",
        "Base62": r"^[a-zA-Z0-9]+$",
        "Base64": r"^[A-Za-z0-9+/]+=*$",
        "Base85": r"^[A-Za-z0-9!#$%&()*+-;<=>?@^_`{|}~]+$"
    }

    # Iterate through the dictionary items
    matches = [base for base, reg in patterns.items() if re.match(reg, s)]
    return matches

string = "ONSWG33OMQQHO33SMQ======"

# In Python, use 'print()', not 'printf()'
print(f"Input: {args.string}")
print(f"Possible Bases: {identify(args.string)}")
