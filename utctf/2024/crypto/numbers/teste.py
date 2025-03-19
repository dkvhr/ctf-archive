import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

seed = int(time.time() * 1000) % (10 ** 6)

def get_random_number():
    global seed
    seed = int(str(seed * seed).zfill(12)[3:9])
    return seed


def encrypt(message):
    key = b''
    for i in range(8):
        key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    print(key)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext.hex()


def decrypt(ciphertext_hex, key):
    #key = b''
    #for i in range(8):
    #    key += (get_random_number() % (2 ** 16)).to_bytes(2, 'big')
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode('utf-8')


flag = "teste{hello}"
encrypted_msg = encrypt(flag.encode())
decrypted_message = decrypt(encrypted_msg)
print(decrypted_message)
