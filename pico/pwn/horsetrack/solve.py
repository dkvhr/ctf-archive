from pwn import *

file_elf = ELF("./vuln")

p = gdb.debug("./vuln")

p.interactive()
