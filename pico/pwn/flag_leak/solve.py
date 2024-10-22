from pwn import *

p = gdb.debug(["./vuln"], gdbscript='''
                b *0x08049380
                b *0x08049418
                b *0x80493a4
                continue
                ''')

p.interactive()
