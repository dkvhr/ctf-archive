import binascii

#flag = open('flag.txt').read()

def encode_base_65536(string):
    base = 65536
    encoded_value = 0

    for char in string:
        encoded_value = encoded_value * 256 + ord(char)
        print(f"encoded value: {encoded_value}")

    encoded_string = ""
    while encoded_value > 0:
        encoded_string = chr(encoded_value % base) + encoded_string
        encoded_value //= base

    return encoded_string

def decode_base_65536(encoded_string):
    base = 65536
    decoded_value = 0

    for char in encoded_string:
        decoded_value = decoded_value * base + ord(char)

    decoded_string = ""
    while decoded_value > 0:
        decoded_string = chr(decoded_value % 256) + decoded_string
        decoded_value //= 256

    return decoded_string

string = b"RU46IFlvdSBhcmUgZ2V0dGluZyBjbG9zZSB0byB0aGUgZmxhZy4uLiBDYW4geW91ICoqZGVjb2RlKiogdGhlIG1lc3NhZ2UgYmVsb3c"

decoded = decode_base_65536(string.decode())
print(decoded)
