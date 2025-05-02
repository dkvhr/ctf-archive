import sys
from pwn import *

def generate_hanoi_moves(n, source, target, auxiliary):
    moves = []
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            moves.append((source, target))
        else:
            hanoi(n-1, source, auxiliary, target)
            moves.append((source, target))
            hanoi(n-1, auxiliary, target, source)
    hanoi(n, source, target, auxiliary)
    return moves

def solve_hanoi(io, num_disks):
    io.sendlineafter(b'Select an option: ', b'1')
    io.sendlineafter(b'Enter the number of burger layers (1-10): ', str(num_disks).encode())

    moves = generate_hanoi_moves(num_disks, 0, 2, 1)
    for from_tower, to_tower in moves:
        io.sendlineafter(b'Move from plate (1-3): ', str(from_tower + 1).encode())
        io.sendlineafter(b'Move to plate (1-3): ', str(to_tower + 1).encode())

    io.recvuntil(b'Congratulations!')
    output = io.recvline().decode()
    bits = output.split('are ')[1].strip().rstrip('.')
    offset = int(bits, 0)
    return offset

def get_encrypted_flag(io):
    io.sendlineafter(b'Select an option: ', b'3')
    encrypted_flag = io.recvline().decode().strip()
    return bytes.fromhex(encrypted_flag)

def decrypt_flag(encrypted_flag, offset):
    decrypted = bytearray()
    for i, byte in enumerate(encrypted_flag):
        n = i + offset
        key = (n ^ (n >> 1)) & 0xFF  # Gray code key generation
        decrypted.append(byte ^ key)
    return decrypted.decode(errors='ignore')  # Handle non-UTF-8 characters

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <host:port>")
        sys.exit(1)
    
    host, port = sys.argv[1].split(':')
    io = remote(host, port)
    
    # Solve for 6 disks to get the full 6-bit offset
    offset = solve_hanoi(io, 6)
    print(f"Offset: {offset} (0b{offset:06b})")
    
    # Get the encrypted flag
    encrypted_flag = get_encrypted_flag(io)
    print(f"Encrypted flag: {encrypted_flag.hex()}")
    
    # Decrypt with the correct key generation (Gray code)
    flag = decrypt_flag(encrypted_flag, offset)
    print(f"Decrypted flag: {flag}")
    
    io.close()

if __name__ == '__main__':
    main()
