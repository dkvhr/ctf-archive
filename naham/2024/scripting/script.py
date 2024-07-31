import base64
from hashlib import md5
 
CIPHERTEXT = "GyseOBdHRQ49Mz1h"
HASHES = [
    "c1d9f50f86825a1a2302ec2449c17196",
    "a64cf5823262686e1a28b2245be34ce0",
    "6b6e667a40e816c4da7bb4ab64cbb82b",
    "1824e8e0307cbfdd1993511ab040075c",
    "8b1a9953c4611296a827abf8c47804d7",
    "d1a7fb5eab1c16cb4f7cf341cf188c3d",
    "d245114cd44bdcd540a014ad78257432",
    "fd05d5cc96e2e85fa2dfc2505932cf76",
    "cd3719c301dce67f4440f42be83ef6f3",
    "ad7fe93595f81645e06239701fbd8084",
    "e8ea7a8d1e93e8764a84a0f3df4644de",
    "9d6a2963872077db674a27a39c492e61",
]
 
ciphertext = base64.b64decode(CIPHERTEXT)
plaintext = b""
key = b""
 
for i, b in enumerate(ciphertext):
    for guess in range(0xFF):
        partial = plaintext + (b ^ guess).to_bytes(1, "big")
        partial_hash = md5(partial).hexdigest()
        if partial_hash == HASHES[i]:
            key += guess.to_bytes(1, "big")
            plaintext = partial
            break
 
print(f"{plaintext=}")
print(f"{key=}")
 
print("================")
 
OTHER_MESSAGES = [
    "FCscMQoGXUYTJDYgFzFKEzZEL3kYCBZKCWcSHQEDWQ49K1w=",
    "CiEHJlgKXhA9bw==",
    "CiEHdB4IXgp2YRFoAz1GUSpONHkNCBIDBiIUUgQJWRg8OwB0GxVIFiwuPz0UKA5Kb0ooLQpaERNIBB8HAxNZJTwhGSFZ",
    "EjoGNRsMHUYTJDYgFzFHEylHOz4CG0FZDnBCQwwCHwdkLERhGgQJUT1zbH9EbQcGe0o7bEoH",
    "ACFSIRYEWBAxLTE1EDxIHWE=",
]
 
def decrypt(encrypted, key):
    factor = len(encrypted) // len(key) + 1
    key = key * factor
 
    enc_bytes = base64.b64decode(encrypted)
    dec_bytes = bytearray()
 
    for i in range(len(enc_bytes)):
        dec_bytes.append(enc_bytes[i] ^ key[i])
    decrypted = dec_bytes.decode()
    return decrypted
 
for m in OTHER_MESSAGES:
    print(decrypt(m, key))
