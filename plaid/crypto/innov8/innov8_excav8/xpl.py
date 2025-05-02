#!/usr/bin/python3
import z3
import struct
import sys

def read_numbers(filename):
    with open(filename, 'r') as f:
        return [float(line.strip()) for line in f if line.strip()]

def check_batch(reversed_batch):
    solver = z3.Solver()
    se_state0, se_state1 = z3.BitVecs("se_state0 se_state1", 64)
    current_s0, current_s1 = se_state0, se_state1

    for num in reversed_batch:
        # Compute new state
        new_s0 = current_s1
        s1 = current_s0
        s1 ^= s1 << 23
        s1 ^= z3.LShR(s1, 17)
        s1 ^= new_s0
        s1 ^= z3.LShR(new_s0, 26)
        new_s1 = s1

        # Calculate mantissa from the current number
        float_plus_1 = num + 1
        packed = struct.pack('d', float_plus_1)
        ulong = struct.unpack('<Q', packed)[0]
        mantissa = ulong & ((1 << 52) - 1)

        # Add constraint for the new state's mantissa
        solver.add(z3.LShR(new_s0, 12) == mantissa)

        current_s0, current_s1 = new_s0, new_s1

    return solver.check() == z3.sat

def main():
    numbers = read_numbers('output.txt')
    batch_size = 24
    batches = [numbers[i:i+batch_size] for i in range(0, len(numbers), batch_size)]
    result_bits = []

    for batch in batches:
        if len(batch) != batch_size:
            continue  # Skip incomplete batches
        reversed_batch = batch[::-1]
        valid = check_batch(reversed_batch)
        result_bits.append('1' if valid else '0')
        print('1' if valid else '0')

    print(''.join(result_bits))

if __name__ == "__main__":
    main()