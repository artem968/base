import re

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

# Your input string
string = "Xk~0{Zv"

# In Python, use 'print()', not 'printf()'
print(f"Input: {string}")
print(f"Possible Bases: {identify(string)}")
