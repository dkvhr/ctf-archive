from pwn import *

sh = remote('challenge.nahamcon.com', 31547)

sh.recvuntil(b'> ')
sh.sendline('1'.encode())
sh.recvuntil(b'> ')
sh.sendline(str('\x01').encode())
sh.recvuntil(b'> ')
n = int(sh.recvline().decode().strip())
sh.recvuntil(b'> [')
 = int(sh.recvline().decode().strip())
sh.interactive()
