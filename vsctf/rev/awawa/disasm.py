#bin is a string

bin = '0001100111001100001000110000110011000100001100000100110001100011000101001100001100110010100011010100001101011000110110010011000011001100000000110000000011000010001100001100110001000011000001001100011000110001010011000011001100101000110101000011010110001101100100110000110011000000001100000000110000000011010000001101101000110111110000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001000010000100001'

ops = {
        0x0 : 'nop',
        0x1 : 'prn',
        0x2 : 'pr1',
        0x3 : 'red',
        0x4 : 'r3d',
        0x5 : 'blo', #s8
        0x6 : 'sbm', #u5
        0x7 : 'pop',
        0x8 : 'dpl',
        0x9 : 'snr', #u5
        0xa : "mrg",
        0xb : '4dd',
        0xc : 'sub',
        0xd : 'mul',
        0xe : 'div',
        0xf : 'cnt',
        0x10 : 'lbl', #u5
        0x11 : 'jmp', #u5
        0x12 : 'eql',
        0x13 : 'lss',
        0x14 : 'gr8',
        0x1f : 'trm',
}

bit_counter = 0
opcode = ""
opcodes = []
for i in range(len(bin)):
    opcode += bin[i]
    #print(opcode)
    bit_counter += 1
    if bit_counter == 5:
        opcodes.append(int(opcode, 2))
        #print("\n\n\nFULL OPCODE!")
        #print(int(opcode, 2))
        if int(opcode, 2) == 0x5:
            opcode = ''
            for j in range(8):
                opcode += bin[i+j+1]
            i += 8
            #print(int(opcode, 2))
            opcodes.append(int(opcode, 2))
        bit_counter = 0
        opcode = ''

#print(opcodes)

double_opcodes = [0x5, 0x6, 0x9, 0x10, 0x11]

for i in range(len(opcodes)):
    instruction = ops.get(opcodes[i])
    print(instruction)
    if opcodes[i] in double_opcodes:
        i += 1
        print(opcodes[i])
