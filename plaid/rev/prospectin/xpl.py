#!/usr/bin/env python3
from pwn import *

exe = ELF("chall_patched")
context.arch = 'amd64'
context.log_level = 'info'
context.binary = exe

def conn():
    if args.REMOTE:
        io = remote("timeleap.grisufrj.com", 32775)
    else:
        if args.GDB:
            io = gdb.debug([exe.path], aslr=False, api=False, gdbscript="""
            """)
        else:
            io = process([exe.path])
    return io

def criar_capacitor():
    sleep(0.2)
    p.sendlineafter(b'> ', b'1')

def nomear_capacitor(idx, nome):
    sleep(0.2)
    p.sendlineafter(b'> ', b'2')
    sleep(0.2)
    p.sendlineafter(b': ', str(idx).encode())
    sleep(0.2)
    p.sendlineafter(b': ', nome)

def ativar_capacitor(idx):
    sleep(0.2)
    p.sendlineafter(b'> ', b'3')
    sleep(0.2)
    p.sendlineafter(b': ', str(idx).encode())

def excluir_capacitor(idx):
    sleep(0.2)
    p.sendlineafter(b'> ', b'4')
    sleep(0.2)
    p.sendlineafter(b': ', str(idx).encode())

def sair_programa():
    sleep(0.2)
    p.sendlineafter(b'> ', b'5')


p = conn()

# seu codigo aqui!

p.interactive()
