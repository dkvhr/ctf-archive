#!/usr/bin/env python3

from pwn import *

exe = ELF("tetrx")
#libc = ELF("./libc.so.6")

context.binary = exe

def conn():
    if args.REMOTE:
        p = remote("addr", 1337)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    p.interactive()


if __name__ == "__main__":
    main()
