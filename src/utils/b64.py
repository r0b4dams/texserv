from base64 import b64encode, b64decode

ENCODING = "ascii"


def encode(string: str) -> str:
    str_bytes = string.encode(ENCODING)
    b64_bytes = b64encode(str_bytes)
    return b64_bytes.decode(ENCODING)


def decode(string: str):
    b64_bytes = string.encode(ENCODING)
    str_bytes = b64decode(b64_bytes)
    return str_bytes.decode(ENCODING)