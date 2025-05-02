from z3 import *
import struct

def xs128p(state0, state1):
        s1 = state0 & 0xFFFFFFFFFFFFFFFF
        s0 = state1 & 0xFFFFFFFFFFFFFFFF
        s1 ^= (s1 << 23) & 0xFFFFFFFFFFFFFFFF
        s1 ^= (s1 >> 17) & 0xFFFFFFFFFFFFFFFF
        s1 ^= s0 & 0xFFFFFFFFFFFFFFFF
        s1 ^= (s0 >> 26) & 0xFFFFFFFFFFFFFFFF
        state0 = state1 & 0xFFFFFFFFFFFFFFFF
        state1 = s1 & 0xFFFFFFFFFFFFFFFF
        generated = state0 & 0xFFFFFFFFFFFFFFFF

        return state0, state1, generated


def xs128p_symbolic(sym_state0, sym_state1):
        s1 = sym_state0
        s0 = sym_state1
        s1 ^= (s1 << 23)
        s1 ^= LShR(s1, 17)
        s1 ^= s0
        s1 ^= LShR(s0, 26)
        sym_state0 = sym_state1
        sym_state1 = s1

        return sym_state0, sym_state1


def sym_random(slvr, sym_state0, sym_state1, generated, multiple):
        sym_state0, sym_state1 = xs128p_symbolic(sym_state0, sym_state1)
        calc = LShR(sym_state0, 12)

        slvr.add(And())


# we can implement the v8 or node function, I will just use node's as
# there is already stuff about it on the web 
# (the v8 one is new and the 13.6.1 release is from 2 months ago)
def to_double(value):
        # uint64_t random = (state0 >> 12) | kExponentBits;
        double_bits = (value >> 12) | 0x3FF0000000000000
        return struct.unpack('d', struct.pack('<Q', double_bits))[0] - 1


def from_double(doubl):
        return struct.unpack('<Q', struct.pack('d', dbl + 1))[0] & 0x7FFFFFFFFFFFFFFF


def solve(points, multiple):
        #symbolic state for XorShift128+
        ostate0, ostate1 = BitVecs('ostate0 ostate1', 64)
        sym_state0 = ostate0
        sym_state1 = ostate1

        solver = SolverFor("QF_BV")

        for point in points:
                sym_state0, sym_state1 = sym


def main():
        result_bits = []
        state0, state1 = solve(points, multiple)

        if state0 is not None and state1 is not None:
                result_bits.append('1')