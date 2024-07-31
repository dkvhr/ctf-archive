from pwn import *
from randcrack import RandCrack
import subprocess
#
#io = remote("chal.osugaming.lol", 7275)
#
#output = io.recvuntil(b'solution:')
#
#sh_command = output.decode().replace('proof of work:\n', '').replace('\nsolution:', '')
#sh_result = subprocess.run(sh_command, shell=True, capture_output=True, text=True).stdout
#
#io.sendline(sh_result.encode())
#
#n = int(io.recvline().decode().replace('n = ', ''))
#io.recvuntil(b'vs = ')
#vs = [int(num) for num in io.recvline().decode().strip()[1:-1].split(',')]
#
#rc = RandCrack()
#
#io.recvuntil(b': ')
#io.sendline(b'1')
#io.recvuntil(b': ')
#random_mask = int(io.recvline().decode().strip(), 2)
#io.interactive()
#rc.submit(random_mask)
#io.recvuntil(b': ')
#io.sendline(b'1')
#
#io.interactive()

rc = RandCrack()

sh = remote('chal.osugaming.lol', 7275)
print(sh.recvuntil(b'solution: '))
sh.sendline(input().encode())

sh.recvuntil(b'n = ')
n = int(sh.recvline().decode().strip())
sh.recvuntil(b'vs = ')
vs = [int(num) for num in sh.recvline().decode().strip()[1:-1].split(',')]

for i in range(624):
	sh.recvuntil(b': ')
	sh.sendline(b'1')
	sh.recvuntil(b': ')
	random_mask = int(sh.recvline().decode().strip(), 2)
	rc.submit(random_mask)
	sh.recvuntil(b': ')
	sh.sendline(b'1')

for i in range(10):
	predicted_mask = '{:032b}'.format(rc.predict_getrandbits(32))
	r = 1
	for j in range(32):
		if predicted_mask[j] == '1':
			r *= pow(vs[j], -1, n)
	r = r % n
	
	sh.recvuntil(b': ')
	sh.sendline(str(r).encode())
	sh.recvuntil(b': ')
	sh.recvline().decode().strip()
	sh.recvuntil(b': ')
	sh.sendline(b'1')

sh.interactive()