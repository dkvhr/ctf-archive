from pwn import *

file_elf = ELF("./chall")

p = gdb.debug("./chall")

p.interactive()
