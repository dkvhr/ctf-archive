#!/usr/bin/env python3

from pwn import *

exe = ELF("challenge")
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

    p.recvuntil(b'main: ')
    main_addr = int(p.recvline(), 16)
    p.recvuntil(b'var: ')
    var_addr = int(p.recvline(), 16)
    p.recvuntil(b'printf: ')
    printf_addr = int(p.recvline(), 16)

    p.interactive()


if __name__ == "__main__":
    main()
