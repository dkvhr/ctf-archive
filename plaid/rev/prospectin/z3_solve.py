from z3 import *

def solve_flag():
    opt = Optimize()
    
    flag = [BitVec(f'flag_{i}', 8) for i in range(0x41)]
    
    opt.add(flag[0] == ord('P'))
    opt.add(flag[1] == ord('C'))
    opt.add(flag[2] == ord('T'))
    opt.add(flag[3] == ord('F'))
    opt.add(flag[4] == ord('{'))
    opt.add(flag[0x40] == ord('}'))
    
    for c in flag:
        opt.add(Or(And(c >= ord(' '), c <= ord('~')), c == 0))
    
    score = 0

    # LOL
    # Condition 1
    cond1 = (flag[27] == 0x32)
    score += If(cond1, 1, 0)

    # Condition 2
    cond2 = ((flag[31] ^ flag[24]) == 0xaa)
    score += If(cond2, 1, 0)

    # Condition 3
    cond3 = ((flag[31] + flag[46] & 0xFF) == 0x90)
    score += If(cond3, 1, 0)

    # Condition 4
    cond4 = ((flag[59] + flag[36] & 0xFF) == 0x81)
    score += If(cond4, 1, 0)

    # Condition 5
    cond5 = (flag[13] == 0xbe)
    score += If(cond5, 1, 0)

    # Condition 6
    cond6 = (flag[32] == 100)
    score += If(cond6, 1, 0)

    # Condition 7
    cond7 = (flag[26] == 0x31)
    score += If(cond7, 1, 0)

    # Condition 8
    cond8 = (flag[42] == 0x39)
    score += If(cond8, 1, 0)

    # Condition 9
    cond9 = ((flag[45] + flag[63] & 0xFF) == 0x93)
    score += If(cond9, 1, 0)

    # Condition 10
    cond10 = (flag[50] == 0x31)
    score += If(cond10, 1, 0)

    # Condition 11
    cond11 = ((flag[1] + flag[15] & 0xFF) == ord('8'))
    score += If(cond11, 1, 0)

    # Condition 12
    cond12 = ((flag[13] ^ flag[35]) == 0x8e)
    score += If(cond12, 1, 0)

    # Condition 13
    cond13 = ((flag[1] ^ flag[46]) == 0x71)
    score += If(cond13, 1, 0)

    # Condition 14
    cond14 = (flag[42] == 0xb4)
    score += If(cond14, 1, 0)

    # Condition 15
    cond15 = (flag[19] == 0x36)
    score += If(cond15, 1, 0)

    # Condition 16
    cond16 = (flag[28] == flag[48])
    score += If(cond16, 1, 0)

    # Condition 17
    cond17 = ((flag[10] ^ flag[33]) == 3)
    score += If(cond17, 1, 0)

    # Condition 18
    cond18 = (flag[30] == 0x76)
    score += If(cond18, 1, 0)

    # Condition 19
    cond19 = (flag[5] == 0x32)
    score += If(cond19, 1, 0)

    # Condition 20
    cond20 = ((flag[1] ^ flag[48]) == 0x85)
    score += If(cond20, 1, 0)

    # Condition 21
    cond21 = (flag[2] == 0x54)
    score += If(cond21, 1, 0)

    # Condition 22
    cond22 = (flag[23] == 0xe1)
    score += If(cond22, 1, 0)

    # Condition 23
    cond23 = ((flag[9] ^ flag[54]) == 0x81)
    score += If(cond23, 1, 0)

    # Condition 24
    cond24 = ((flag[53] + flag[26] & 0xFF) == ord('a'))
    score += If(cond24, 1, 0)

    # Condition 25
    cond25 = ((flag[18] ^ flag[57]) == 7)
    score += If(cond25, 1, 0)

    # Condition 26
    cond26 = ((flag[18] ^ flag[5]) == 0x56)
    score += If(cond26, 1, 0)

    # Condition 27
    cond27 = ((flag[14] + flag[53] & 0xFF) == ord('f'))
    score += If(cond27, 1, 0)

    # Condition 28
    cond28 = ((flag[48] ^ flag[56]) == 0x54)
    score += If(cond28, 1, 0)

    # Condition 29
    cond29 = (flag[52] == 0xe5)
    score += If(cond29, 1, 0)

    # Condition 30
    cond30 = (flag[36] == ord('o'))
    score += If(cond30, 1, 0)

    # Condition 31
    cond31 = ((flag[37] + flag[30] & 0xFF) == ord('f'))
    score += If(cond31, 1, 0)

    # Condition 32
    cond32 = (flag[50] == 0x31)
    score += If(cond32, 1, 0)

    # Condition 33
    cond33 = (flag[23] == 0x38)
    score += If(cond33, 1, 0)

    # Condition 34
    cond34 = (flag[39] == ord('4'))
    score += If(cond34, 1, 0)

    # Condition 35
    cond35 = ((flag[56] + flag[19] & 0xFF) == 0x97)
    score += If(cond35, 1, 0)

    # Condition 36
    cond36 = ((flag[19] ^ flag[50]) == 0x2d)
    score += If(cond36, 1, 0)

    # Condition 37
    cond37 = ((flag[34] + flag[1] & 0xFF) == 0xa4)
    score += If(cond37, 1, 0)

    # Condition 38
    cond38 = ((flag[47] + flag[38] & 0xFF) == 0xf4)
    score += If(cond38, 1, 0)

    # Condition 39
    cond39 = ((flag[27] + flag[47] & 0xFF) == 0x97)
    score += If(cond39, 1, 0)

    # Condition 40
    cond40 = ((flag[47] + flag[10] & 0xFF) == 0x96)
    score += If(cond40, 1, 0)

    # Condition 41
    cond41 = (flag[2] == 0x72)
    score += If(cond41, 1, 0)

    # Condition 42
    cond42 = (flag[59] == 0x36)
    score += If(cond42, 1, 0)

    # Condition 43
    cond43 = (flag[28] == 0xb1)
    score += If(cond43, 1, 0)

    # Condition 44
    cond44 = ((flag[8] ^ flag[58]) == 8)
    score += If(cond44, 1, 0)

    # Condition 45
    cond45 = ((flag[2] ^ flag[46]) == 0x3a)
    score += If(cond45, 1, 0)

    # Condition 46
    cond46 = (flag[59] == 0x44)
    score += If(cond46, 1, 0)

    # Condition 47
    cond47 = (flag[57] == 0x12)
    score += If(cond47, 1, 0)

    # Condition 48
    cond48 = ((flag[17] ^ flag[40]) == 0x5b)
    score += If(cond48, 1, 0)

    # Condition 49
    cond49 = (flag[41] == 0x2a)
    score += If(cond49, 1, 0)

    # Condition 50
    cond50 = (flag[41] == 0x33)
    score += If(cond50, 1, 0)

    # Condition 51
    cond51 = ((flag[26] + flag[38] & 0xFF) == ord('?'))
    score += If(cond51, 1, 0)

    # Condition 52
    cond52 = ((flag[61] ^ flag[0]) == 0x60)
    score += If(cond52, 1, 0)

    # Condition 53
    cond53 = (flag[21] == 0x24)
    score += If(cond53, 1, 0)

    # Condition 54
    cond54 = ((flag[5] + flag[43] & 0xFF) == ord('-'))
    score += If(cond54, 1, 0)

    # Condition 55
    cond55 = (flag[57] == 99)
    score += If(cond55, 1, 0)

    # Condition 56
    cond56 = ((flag[55] ^ flag[52]) == 5)
    score += If(cond56, 1, 0)

    # Condition 57
    cond57 = (flag[4] == 0x7b)
    score += If(cond57, 1, 0)

    # Condition 58
    cond58 = ((flag[16] + flag[9] & 0xFF) == 0xad)
    score += If(cond58, 1, 0)

    # Condition 59
    cond59 = ((flag[22] + flag[45] & 0xFF) == 0x98)
    score += If(cond59, 1, 0)

    # Condition 60
    cond60 = (flag[24] == 0x32)
    score += If(cond60, 1, 0)

    # Condition 61
    cond61 = (flag[48] == 0x35)
    score += If(cond61, 1, 0)

    # Condition 62
    cond62 = ((flag[54] ^ flag[19]) == 0x5b)
    score += If(cond62, 1, 0)

    # Condition 63
    cond63 = ((flag[54] + flag[14] & 0xFF) == 0x99)
    score += If(cond63, 1, 0)

    # Condition 64
    cond64 = (flag[53] == 0xd2)
    score += If(cond64, 1, 0)

    # Condition 65
    cond65 = ((flag[0] ^ flag[48]) == 0x65)
    score += If(cond65, 1, 0)

    # Condition 66
    cond66 = ((flag[42] + flag[49] & 0xFF) == 0x9a)
    score += If(cond66, 1, 0)

    # Condition 67
    cond67 = ((flag[20] + flag[29] & 0xFF) == 0x96)
    score += If(cond67, 1, 0)

    # Condition 68
    cond68 = ((flag[40] ^ flag[50]) == 0xda)
    score += If(cond68, 1, 0)

    # Condition 69
    cond69 = ((flag[60] + flag[32] & 0xFF) == 0x96)
    score += If(cond69, 1, 0)

    # Condition 70
    cond70 = ((flag[39] + flag[7] & 0xFF) == 0x98)
    score += If(cond70, 1, 0)

    # Condition 71
    cond71 = (flag[50] == flag[10])
    score += If(cond71, 1, 0)

    # Condition 72
    cond72 = ((flag[57] ^ flag[10]) == 0x52)
    score += If(cond72, 1, 0)

    # Condition 73
    cond73 = (flag[56] == 0x61)
    score += If(cond73, 1, 0)

    # Condition 74
    cond74 = (flag[20] == 0x61)
    score += If(cond74, 1, 0)

    # Condition 75
    cond75 = ((flag[62] ^ flag[8]) == 1)
    score += If(cond75, 1, 0)

    # Condition 76
    cond76 = ((flag[44] ^ flag[34]) == 0x30)
    score += If(cond76, 1, 0)

    # Condition 77
    cond77 = (flag[33] == 0x32)
    score += If(cond77, 1, 0)

    # Condition 78
    cond78 = ((flag[47] ^ flag[49]) == 4)
    score += If(cond78, 1, 0)

    # Condition 79
    cond79 = ((flag[27] ^ flag[22]) == 0x53)
    score += If(cond79, 1, 0)

    # Condition 80
    cond80 = ((flag[0] + flag[41] & 0xFF) == 0x83)
    score += If(cond80, 1, 0)

    # Condition 81
    cond81 = (flag[18] == 0xf1)
    score += If(cond81, 1, 0)

    # Condition 82
    cond82 = (flag[28] == 0x35)
    score += If(cond82, 1, 0)

    # Condition 83
    cond83 = (flag[16] == 0xd3)
    score += If(cond83, 1, 0)

    # Condition 84
    cond84 = ((flag[6] + flag[47] & 0xFF) == 0x99)
    score += If(cond84, 1, 0)

    # Condition 85
    cond85 = ((flag[28] + flag[25] & 0xFF) == 0xaf)
    score += If(cond85, 1, 0)

    # Condition 86
    cond86 = ((flag[63] + flag[19] & 0xFF) == 0xb3)
    score += If(cond86, 1, 0)

    # Condition 87
    cond87 = (flag[29] == 0x35)
    score += If(cond87, 1, 0)

    # Condition 88
    cond88 = (flag[61] == 0x30)
    score += If(cond88, 1, 0)

    # Condition 89
    cond89 = ((flag[15] + flag[25] & 0xFF) == 0x85)
    score += If(cond89, 1, 0)

    # Condition 90
    cond90 = ((flag[20] ^ flag[61]) == 0x4f)
    score += If(cond90, 1, 0)

    # Condition 91
    cond91 = ((flag[27] ^ flag[50]) == 3)
    score += If(cond91, 1, 0)

    # Condition 92
    cond92 = ((flag[62] + flag[51] & 0xFF) == ord('b'))
    score += If(cond92, 1, 0)

    # Condition 93
    cond93 = ((flag[20] + flag[44] & 0xFF) == 0xc5)
    score += If(cond93, 1, 0)

    # Condition 94
    cond94 = ((flag[43] + flag[18] & 0xFF) == 0xc9)
    score += If(cond94, 1, 0)

    # Condition 95
    cond95 = ((flag[9] + flag[36] & 0xFF) == ord('h'))
    score += If(cond95, 1, 0)

    # Condition 96
    cond96 = (flag[9] == flag[19])
    score += If(cond96, 1, 0)

    # Condition 97
    cond97 = ((flag[19] ^ flag[33]) == 4)
    score += If(cond97, 1, 0)

    # Condition 98
    cond98 = ((flag[55] + flag[0] & 0xFF) == 0x85)
    score += If(cond98, 1, 0)

    # Condition 99
    cond99 = (flag[22] == 0x61)
    score += If(cond99, 1, 0)

    # Condition 100
    cond100 = (flag[17] == 0x39)
    score += If(cond100, 1, 0)

    # Condition 101
    cond101 = (flag[10] == 0x31)
    score += If(cond101, 1, 0)

    # Condition 102
    cond102 = (flag[53] == 0x30)
    score += If(cond102, 1, 0)

    # Condition 103
    cond103 = ((flag[49] + flag[61] & 0xFF) == 0xe9)
    score += If(cond103, 1, 0)

    # Condition 104
    cond104 = (flag[50] == 0x31)
    score += If(cond104, 1, 0)

    # Condition 105
    cond105 = ((flag[55] + flag[3] & 0xFF) == 0xbf)
    score += If(cond105, 1, 0)

    # Condition 106
    cond106 = ((flag[45] + flag[25] & 0xFF) == 0x99)
    score += If(cond106, 1, 0)

    # Condition 107
    cond107 = (flag[46] == 0x32)
    score += If(cond107, 1, 0)

    # Condition 108
    cond108 = ((flag[24] + flag[43] & 0xFF) == 0x97)
    score += If(cond108, 1, 0)

    # Condition 109
    cond109 = (flag[26] == 0x31)
    score += If(cond109, 1, 0)

    # Condition 110
    cond110 = (flag[14] == 0x36)
    score += If(cond110, 1, 0)

    # Condition 111
    cond111 = ((flag[3] + flag[62] & 0xFF) == ord('v'))
    score += If(cond111, 1, 0)

    # Condition 112
    cond112 = (flag[27] == 0x32)
    score += If(cond112, 1, 0)

    # Condition 113
    cond113 = ((flag[63] ^ flag[45]) == 0x4a)
    score += If(cond113, 1, 0)

    # Condition 114
    cond114 = ((flag[44] + flag[14] & 0xFF) == 0xf0)
    score += If(cond114, 1, 0)

    # Condition 115
    cond115 = (flag[9] == 0xd8)
    score += If(cond115, 1, 0)

    # Condition 116
    cond116 = ((flag[58] + flag[62] & 0xFF) == ord('b'))
    score += If(cond116, 1, 0)

    # Condition 117
    cond117 = ((flag[61] + flag[22] & 0xFF) == 0x93)
    score += If(cond117, 1, 0)

    # Condition 118
    cond118 = ((flag[51] ^ flag[53]) == 2)
    score += If(cond118, 1, 0)

    # Condition 119
    cond119 = (flag[27] == 0x32)
    score += If(cond119, 1, 0)

    # Condition 120
    cond120 = ((flag[50] ^ flag[59]) == 7)
    score += If(cond120, 1, 0)

    # Condition 121
    cond121 = (flag[52] == 0x30)
    score += If(cond121, 1, 0)

    # Condition 122
    cond122 = (flag[33] == 0x79)
    score += If(cond122, 1, 0)

    # Condition 123
    cond123 = (flag[61] == 0x33)
    score += If(cond123, 1, 0)

    # Condition 124
    cond124 = ((flag[21] + flag[49] & 0xFF) == 0xc5)
    score += If(cond124, 1, 0)

    # Condition 125
    cond125 = (flag[36] == ord('S'))
    score += If(cond125, 1, 0)

    # Condition 126
    cond126 = (flag[15] == 9)
    score += If(cond126, 1, 0)

    # Condition 127
    cond127 = ((flag[0] + flag[32] & 0xFF) == 0xb4)
    score += If(cond127, 1, 0)

    # Condition 128
    cond128 = ((flag[14] + flag[51] & 0xFF) == ord('h'))
    score += If(cond128, 1, 0)

    # Condition 129
    cond129 = ((flag[43] ^ flag[14]) == 0xfb)
    score += If(cond129, 1, 0)

    # Condition 130
    cond130 = (flag[58] == 0x4f)
    score += If(cond130, 1, 0)

    # Condition 131
    cond131 = (flag[10] == 0x3e)
    score += If(cond131, 1, 0)

    # Condition 132
    cond132 = (flag[47] == 0xec)
    score += If(cond132, 1, 0)

    # Condition 133
    cond133 = (flag[45] == 0x37)
    score += If(cond133, 1, 0)

    # Condition 134
    cond134 = ((flag[22] + flag[59] & 0xFF) == -1)
    score += If(cond134, 1, 0)

    # Condition 135
    cond135 = ((flag[24] ^ flag[2]) == 0x28)
    score += If(cond135, 1, 0)

    # Condition 136
    cond136 = (flag[48] == 0xd1)
    score += If(cond136, 1, 0)

    # Condition 137
    cond137 = ((flag[55] ^ flag[7]) == 0xe8)
    score += If(cond137, 1, 0)

    # Condition 138
    cond138 = (flag[47] == 0x65)
    score += If(cond138, 1, 0)

    # Condition 139
    cond139 = ((flag[5] + flag[57] & 0xFF) == -4)
    score += If(cond139, 1, 0)

    # Condition 140
    cond140 = ((flag[24] + flag[5] & 0xFF) == ord('d'))
    score += If(cond140, 1, 0)

    # Condition 141
    cond141 = ((flag[34] ^ flag[54]) == 2)
    score += If(cond141, 1, 0)

    # Condition 142
    cond142 = (flag[9] == 0x36)
    score += If(cond142, 1, 0)

    # Condition 143
    cond143 = (flag[5] == 0x32)
    score += If(cond143, 1, 0)

    # Condition 144
    cond144 = (flag[26] == 0x31)
    score += If(cond144, 1, 0)

    # Condition 145
    cond145 = (flag[60] == 0x32)
    score += If(cond145, 1, 0)

    # Condition 146
    cond146 = ((flag[4] + flag[7] & 0xFF) == 0xdf)
    score += If(cond146, 1, 0)

    # Condition 147
    cond147 = (flag[31] == 0x34)
    score += If(cond147, 1, 0)

    # Condition 148
    cond148 = ((flag[50] ^ flag[52]) == 0x59)
    score += If(cond148, 1, 0)

    # Condition 149
    cond149 = (flag[58] == 0x39)
    score += If(cond149, 1, 0)

    # Condition 150
    cond150 = ((flag[12] ^ flag[43]) == 0x53)
    score += If(cond150, 1, 0)

    # Condition 151
    cond151 = (flag[7] == 0x61)
    score += If(cond151, 1, 0)

    # Condition 152
    cond152 = ((flag[53] ^ flag[7]) == 0x54)
    score += If(cond152, 1, 0)

    # Condition 153
    cond153 = ((flag[59] + flag[6] & 0xFF) == ord('j'))
    score += If(cond153, 1, 0)

    # Condition 154
    cond154 = ((flag[17] + flag[28] & 0xFF) == ord('n'))
    score += If(cond154, 1, 0)

    # Condition 155
    cond155 = (flag[4] == 0x7b)
    score += If(cond155, 1, 0)

    # Condition 156
    cond156 = (flag[35] == 0x65)
    score += If(cond156, 1, 0)

    # Condition 157
    cond157 = ((flag[36] + flag[44] & 0xFF) == 0x96)
    score += If(cond157, 1, 0)

    # Condition 158
    cond158 = (flag[63] == 0x7d)
    score += If(cond158, 1, 0)

    # Condition 159
    cond159 = ((flag[27] ^ flag[41]) == 0x5d)
    score += If(cond159, 1, 0)

    # Condition 160
    cond160 = (flag[40] == 0x62)
    score += If(cond160, 1, 0)

    # Condition 161
    cond161 = ((flag[24] ^ flag[21]) == 99)
    score += If(cond161, 1, 0)

    # Condition 162
    cond162 = ((flag[21] ^ flag[19]) == 0x52)
    score += If(cond162, 1, 0)

    # Condition 163
    cond163 = (flag[10] == 0x31)
    score += If(cond163, 1, 0)

    # Condition 164
    cond164 = ((flag[37] + flag[6] & 0xFF) == ord('g'))
    score += If(cond164, 1, 0)

    # Condition 165
    cond165 = (flag[6] == 0x7b)
    score += If(cond165, 1, 0)

    # Condition 166
    cond166 = (flag[56] == 0x93)
    score += If(cond166, 1, 0)

    # Condition 167
    cond167 = ((flag[9] ^ flag[29]) == 3)
    score += If(cond167, 1, 0)

    # Condition 168
    cond168 = (flag[47] == 199)
    score += If(cond168, 1, 0)

    # Condition 169
    cond169 = (flag[29] == 0x35)
    score += If(cond169, 1, 0)

    # Condition 170
    cond170 = (flag[63] == 0x7d)
    score += If(cond170, 1, 0)

    # Condition 171
    cond171 = ((flag[51] + flag[38] & 0xFF) == ord('G'))
    score += If(cond171, 1, 0)

    # Condition 172
    cond172 = ((flag[60] + flag[20] & 0xFF) == 0x93)
    score += If(cond172, 1, 0)

    # Condition 173
    cond173 = ((flag[1] ^ flag[15]) == 0x74)
    score += If(cond173, 1, 0)

    # Condition 174
    cond174 = ((flag[11] ^ flag[58]) == 0x16)
    score += If(cond174, 1, 0)

    # Condition 175
    cond175 = (flag[50] == 0x31)
    score += If(cond175, 1, 0)

    # Condition 176
    cond176 = ((flag[0] + flag[63] & 0xFF) == 0xcd)
    score += If(cond176, 1, 0)

    # Condition 177
    cond177 = (flag[60] == 0x32)
    score += If(cond177, 1, 0)

    # Condition 178
    cond178 = (flag[54] == 99)
    score += If(cond178, 1, 0)

    # Condition 179
    cond179 = (flag[7] == 0x4b)
    score += If(cond179, 1, 0)

    # Condition 180
    cond180 = ((flag[29] ^ flag[40]) == 0x57)
    score += If(cond180, 1, 0)

    # Condition 181
    cond181 = (flag[58] == 0x39)
    score += If(cond181, 1, 0)

    # Condition 182
    cond182 = ((flag[33] ^ flag[44]) == 0x56)
    score += If(cond182, 1, 0)

    # Condition 183
    cond183 = (flag[17] == 0x96)
    score += If(cond183, 1, 0)

    # Condition 184
    cond184 = (flag[19] == 0xab)
    score += If(cond184, 1, 0)

    # Condition 185
    cond185 = ((flag[59] + flag[51] & 0xFF) == 0xaf)
    score += If(cond185, 1, 0)

    # Condition 186
    cond186 = (flag[21] == 0x7f)
    score += If(cond186, 1, 0)

    # Condition 187
    cond187 = ((flag[35] ^ flag[11]) == 0xd1)
    score += If(cond187, 1, 0)

    # Condition 188
    cond188 = (flag[40] == 0x62)
    score += If(cond188, 1, 0)

    # Condition 189
    cond189 = ((flag[18] ^ flag[13]) == 0x5e)
    score += If(cond189, 1, 0)

    # Condition 190
    cond190 = (flag[7] == 0x16)
    score += If(cond190, 1, 0)

    # Condition 191
    cond191 = ((flag[54] + flag[6] & 0xFF) == 0x97)
    score += If(cond191, 1, 0)

    # Condition 192
    cond192 = (flag[50] == 0x31)
    score += If(cond192, 1, 0)

    # Condition 193
    cond193 = (flag[45] == 0x37)
    score += If(cond193, 1, 0)

    # Condition 194
    cond194 = ((flag[19] + flag[5] & 0xFF) == ord('h'))
    score += If(cond194, 1, 0)

    # Condition 195
    cond195 = (flag[4] == 0x1a)
    score += If(cond195, 1, 0)

    # Condition 196
    cond196 = (flag[62] == 0x30)
    score += If(cond196, 1, 0)

    # Condition 197
    cond197 = ((flag[12] ^ flag[24]) == 4)
    score += If(cond197, 1, 0)

    # Condition 198
    cond198 = ((flag[46] + flag[32] & 0xFF) == 0x96)
    score += If(cond198, 1, 0)

    # Condition 199
    cond199 = (flag[34] == 0x61)
    score += If(cond199, 1, 0)

    # Condition 200
    cond200 = (flag[3] == 0x46)
    score += If(cond200, 1, 0)

    # Condition 201
    cond201 = ((flag[11] + flag[47] & 0xFF) == 0x97)
    score += If(cond201, 1, 0)

    # Condition 202
    cond202 = (flag[46] == 0x32)
    score += If(cond202, 1, 0)

    # Condition 203
    cond203 = (flag[25] == 0x60)
    score += If(cond203, 1, 0)

    # Condition 204
    cond204 = (flag[9] == 0x36)
    score += If(cond204, 1, 0)

    # Condition 205
    cond205 = (flag[26] == 0x3a)
    score += If(cond205, 1, 0)

    # Condition 206
    cond206 = ((flag[55] ^ flag[42]) == 0xc)
    score += If(cond206, 1, 0)

    # Condition 207
    cond207 = ((flag[34] ^ flag[19]) == 0x57)
    score += If(cond207, 1, 0)

    # Condition 208
    cond208 = (flag[56] == 0x61)
    score += If(cond208, 1, 0)

    # Condition 209
    cond209 = ((flag[43] ^ flag[31]) == 0x51)
    score += If(cond209, 1, 0)

    # Condition 210
    cond210 = (flag[55] == 0x35)
    score += If(cond210, 1, 0)

    # Condition 211
    cond211 = (flag[9] == 0xa9)
    score += If(cond211, 1, 0)

    # Condition 212
    cond212 = ((flag[46] + flag[3] & 0xFF) == ord('x'))
    score += If(cond212, 1, 0)

    # Condition 213
    cond213 = (flag[48] == 0x1f)
    score += If(cond213, 1, 0)

    # Condition 214
    cond214 = ((flag[35] + flag[23] & 0xFF) == -99)
    score += If(cond214, 1, 0)

    # Condition 215
    cond215 = (flag[36] == ord('m'))
    score += If(cond215, 1, 0)

    # Condition 216
    cond216 = ((flag[30] ^ flag[28]) == 6)
    score += If(cond216, 1, 0)

    # Condition 217
    cond217 = (flag[53] == 0x30)
    score += If(cond217, 1, 0)

    # Condition 218
    cond218 = (flag[20] == 0xf7)
    score += If(cond218, 1, 0)

    # Condition 219
    cond219 = (flag[50] == 0x31)
    score += If(cond219, 1, 0)

    # Condition 220
    cond220 = ((flag[60] + flag[45] & 0xFF) == ord('i'))
    score += If(cond220, 1, 0)

    # Condition 221
    cond221 = ((flag[41] ^ flag[12]) == 5)
    score += If(cond221, 1, 0)

    # Condition 222
    cond222 = ((flag[9] ^ flag[42]) == 0x85)
    score += If(cond222, 1, 0)

    # Condition 223
    cond223 = (flag[32] == 100)
    score += If(cond223, 1, 0)

    # Condition 224
    cond224 = (flag[53] == 0x30)
    score += If(cond224, 1, 0)

    # Condition 225
    cond225 = ((flag[38] + flag[55] & 0xFF) == ord('g'))
    score += If(cond225, 1, 0)

    # Condition 226
    cond226 = (flag[32] == flag[13])
    score += If(cond226, 1, 0)

    # Condition 227
    cond227 = (flag[36] == ord('2'))
    score += If(cond227, 1, 0)

    # Condition 228
    cond228 = (flag[23] == 0x9b)
    score += If(cond228, 1, 0)

    # Condition 229
    cond229 = (flag[13] == 100)
    score += If(cond229, 1, 0)

    # Condition 230
    cond230 = (flag[8] == 0x31)
    score += If(cond230, 1, 0)

    # Condition 231
    cond231 = (flag[36] == ord('2'))
    score += If(cond231, 1, 0)

    # Condition 232
    cond232 = (flag[14] == 0xc3)
    score += If(cond232, 1, 0)

    # Condition 233
    cond233 = ((flag[41] + flag[21] & 0xFF) == 0x97)
    score += If(cond233, 1, 0)

    # Condition 234
    cond234 = ((flag[45] + flag[37] & 0xFF) == ord('j'))
    score += If(cond234, 1, 0)

    # Condition 235
    cond235 = (flag[32] == 0x32)
    score += If(cond235, 1, 0)

    # Condition 236
    cond236 = (flag[44] == 100)
    score += If(cond236, 1, 0)

    # Condition 237
    cond237 = (flag[2] == 0x54)
    score += If(cond237, 1, 0)

    # Condition 238
    cond238 = ((flag[35] ^ flag[50]) == 0x54)
    score += If(cond238, 1, 0)

    # Condition 239
    cond239 = (flag[51] == 0x32)
    score += If(cond239, 1, 0)

    # Condition 240
    cond240 = (flag[48] == 0x35)
    score += If(cond240, 1, 0)

    # Condition 241
    cond241 = (flag[41] == 0x33)
    score += If(cond241, 1, 0)

    # Condition 242
    cond242 = (flag[27] == 0x32)
    score += If(cond242, 1, 0)

    # Condition 243
    cond243 = ((flag[49] + flag[59] & 0xFF) == 0x97)
    score += If(cond243, 1, 0)

    # Condition 244
    cond244 = (flag[36] == ord('2'))
    score += If(cond244, 1, 0)

    # Condition 245
    cond245 = (flag[22] == 0x61)
    score += If(cond245, 1, 0)

    # Condition 246
    cond246 = ((flag[55] + flag[4] & 0xFF) == ord('\x12'))
    score += If(cond246, 1, 0)

    # Condition 247
    cond247 = (flag[46] == 0x9e)
    score += If(cond247, 1, 0)

    # Condition 248
    cond248 = ((flag[22] ^ flag[31]) == 0x55)
    score += If(cond248, 1, 0)

    # Condition 249
    cond249 = (flag[50] == 0x43)
    score += If(cond249, 1, 0)

    # Condition 250
    cond250 = (flag[23] == 0x38)
    score += If(cond250, 1, 0)

    # Condition 251
    cond251 = (flag[52] == 0xc)
    score += If(cond251, 1, 0)

    # Condition 252
    cond252 = (flag[52] == 0x30)
    score += If(cond252, 1, 0)

    # Condition 253
    cond253 = (flag[22] == 0x61)
    score += If(cond253, 1, 0)

    # Condition 254
    cond254 = (flag[14] == 0x36)
    score += If(cond254, 1, 0)

    # Condition 255
    cond255 = (flag[2] == 0x54)
    score += If(cond255, 1, 0)

    # Condition 256
    cond256 = ((flag[8] ^ flag[22]) == 0x50)
    score += If(cond256, 1, 0)

    # Condition 257
    cond257 = ((flag[35] + flag[0] & 0xFF) == 0xa7)
    score += If(cond257, 1, 0)

    # Condition 258
    cond258 = ((flag[39] + flag[2] & 0xFF) == 0xc7)
    score += If(cond258, 1, 0)

    # Condition 259
    cond259 = ((flag[41] ^ flag[6]) == 7)
    score += If(cond259, 1, 0)

    # Condition 260
    cond260 = ((flag[33] + flag[11] & 0xFF) == 0xa5)
    score += If(cond260, 1, 0)

    # Condition 261
    cond261 = (flag[25] == 0x62)
    score += If(cond261, 1, 0)

    # Condition 262
    cond262 = (flag[26] == 0x31)
    score += If(cond262, 1, 0)

    # Condition 263
    cond263 = ((flag[20] + flag[27] & 0xFF) == ord('#'))
    score += If(cond263, 1, 0)

    # Condition 264
    cond264 = ((flag[6] ^ flag[35]) == 0x9c)
    score += If(cond264, 1, 0)

    # Condition 265
    cond265 = ((flag[14] ^ flag[11]) == 4)
    score += If(cond265, 1, 0)

    # Condition 266
    cond266 = (flag[39] == ord('4'))
    score += If(cond266, 1, 0)

    # Condition 267
    cond267 = ((flag[40] + flag[31] & 0xFF) == 0x96)
    score += If(cond267, 1, 0)

    # Condition 268
    cond268 = (flag[57] == 99)
    score += If(cond268, 1, 0)

    # Condition 269
    cond269 = (flag[7] == 100)
    score += If(cond269, 1, 0)

    # Condition 270
    cond270 = (flag[14] == 0x36)
    score += If(cond270, 1, 0)

    # Condition 271
    cond271 = (flag[5] == 0x43)
    score += If(cond271, 1, 0)

    # Condition 272
    cond272 = ((flag[23] ^ flag[22]) == 0x59)
    score += If(cond272, 1, 0)

    # Condition 273
    cond273 = (flag[21] == 100)
    score += If(cond273, 1, 0)

    # Condition 274
    cond274 = ((flag[22] ^ flag[44]) == 5)
    score += If(cond274, 1, 0)

    # Condition 275
    cond275 = (flag[53] == 0x30)
    score += If(cond275, 1, 0)

    # Condition 276
    cond276 = (flag[31] == 0x34)
    score += If(cond276, 1, 0)

    # Condition 277
    cond277 = (flag[22] == 0x61)
    score += If(cond277, 1, 0)

    # Condition 278
    cond278 = ((flag[46] + flag[8] & 0xFF) == ord('z'))
    score += If(cond278, 1, 0)

    # Condition 279
    cond279 = ((flag[25] ^ flag[3]) == 0x24)
    score += If(cond279, 1, 0)

    # Condition 280
    cond280 = (flag[43] == 0x65)
    score += If(cond280, 1, 0)

    # Condition 281
    cond281 = (flag[44] == 0xf)
    score += If(cond281, 1, 0)

    # Condition 282
    cond282 = ((flag[16] ^ flag[21]) == 0x57)
    score += If(cond282, 1, 0)

    # Condition 283
    cond283 = ((flag[9] ^ flag[62]) == 6)
    score += If(cond283, 1, 0)

    # Condition 284
    cond284 = (flag[27] == 0x32)
    score += If(cond284, 1, 0)

    # Condition 285
    cond285 = ((flag[18] + flag[54] & 0xFF) == 0xd1)
    score += If(cond285, 1, 0)

    # Condition 286
    cond286 = (flag[32] == 100)
    score += If(cond286, 1, 0)

    # Condition 287
    cond287 = ((flag[57] + flag[18] & 0xFF) == 0xc7)
    score += If(cond287, 1, 0)

    # Condition 288
    cond288 = ((flag[43] ^ flag[32]) == 1)
    score += If(cond288, 1, 0)

    # Condition 289
    cond289 = (flag[17] == 0xa4)
    score += If(cond289, 1, 0)

    # Condition 290
    cond290 = ((flag[8] ^ flag[9]) == 7)
    score += If(cond290, 1, 0)

    # Condition 291
    cond291 = (flag[40] == 0x62)
    score += If(cond291, 1, 0)

    # Condition 292
    cond292 = ((flag[56] + flag[4] & 0xFF) == ord('\n'))
    score += If(cond292, 1, 0)

    # Condition 293
    cond293 = ((flag[21] + flag[28] & 0xFF) == 0x99)
    score += If(cond293, 1, 0)

    # Condition 294
    cond294 = (flag[12] == 0x7c)
    score += If(cond294, 1, 0)

    # Condition 295
    cond295 = ((flag[63] + flag[18] & 0xFF) == 0xe1)
    score += If(cond295, 1, 0)

    # Condition 296
    cond296 = (flag[27] == 0x32)
    score += If(cond296, 1, 0)

    # Condition 297
    cond297 = (flag[23] == 0x38)
    score += If(cond297, 1, 0)

    # Condition 298
    cond298 = ((flag[44] + flag[18] & 0xFF) == 0xc8)
    score += If(cond298, 1, 0)

    # Condition 299
    cond299 = ((flag[9] + flag[19] & 0xFF) == ord('l'))
    score += If(cond299, 1, 0)

    # Condition 300
    cond300 = ((flag[61] + flag[11] & 0xFF) == 0xe7)
    score += If(cond300, 1, 0)

    # Condition 301
    cond301 = (flag[21] == 100)
    score += If(cond301, 1, 0)

    # Condition 302
    cond302 = ((flag[57] + flag[31] & 0xFF) == 0x97)
    score += If(cond302, 1, 0)

    # Condition 303
    cond303 = ((flag[28] ^ flag[40]) == 0x57)
    score += If(cond303, 1, 0)

    # Condition 304
    cond304 = (flag[45] == 0x37)
    score += If(cond304, 1, 0)

    # Condition 305
    cond305 = ((flag[13] + flag[47] & 0xFF) == 0xc9)
    score += If(cond305, 1, 0)

    # Condition 306
    cond306 = (flag[18] == 100)
    score += If(cond306, 1, 0)

    # Condition 307
    cond307 = (flag[15] == 0x37)
    score += If(cond307, 1, 0)

    # Condition 308
    cond308 = ((flag[58] ^ flag[16]) == 10)
    score += If(cond308, 1, 0)

    # Condition 309
    cond309 = ((flag[0] ^ flag[21]) == 0x34)
    score += If(cond309, 1, 0)

    # Condition 310
    cond310 = ((flag[62] + flag[49] & 0xFF) == 0x91)
    score += If(cond310, 1, 0)

    # Condition 311
    cond311 = (flag[46] == 0x32)
    score += If(cond311, 1, 0)

    # Condition 312
    cond312 = ((flag[57] + flag[0] & 0xFF) == 0xa8)
    score += If(cond312, 1, 0)

    # Condition 313
    cond313 = (flag[36] == ord('2'))
    score += If(cond313, 1, 0)

    # Condition 314
    cond314 = (flag[50] == 0x31)
    score += If(cond314, 1, 0)

    # Condition 315
    cond315 = (flag[48] == 0x35)
    score += If(cond315, 1, 0)

    # Condition 316
    cond316 = (flag[42] == 0x39)
    score += If(cond316, 1, 0)

    # Condition 317
    cond317 = ((flag[61] + flag[35] & 0xFF) == 0x95)
    score += If(cond317, 1, 0)

    # Condition 318
    cond318 = ((flag[27] + flag[1] & 0xFF) == ord('u'))
    score += If(cond318, 1, 0)

    # Condition 319
    cond319 = (flag[48] == 0x35)
    score += If(cond319, 1, 0)

    # Condition 320
    cond320 = ((flag[35] ^ flag[33]) == 0x51)
    score += If(cond320, 1, 0)

    # Condition 321
    cond321 = ((flag[29] ^ flag[57]) == 0x56)
    score += If(cond321, 1, 0)

    # Condition 322
    cond322 = (flag[23] == 0x4b)
    score += If(cond322, 1, 0)

    # Condition 323
    cond323 = ((flag[31] + flag[13] & 0xFF) == 0xac)
    score += If(cond323, 1, 0)

    # Condition 324
    cond324 = (flag[39] == ord('J'))
    score += If(cond324, 1, 0)

    # Condition 325
    cond325 = (flag[39] == ord('4'))
    score += If(cond325, 1, 0)

    # Condition 326
    cond326 = (flag[33] == 0x73)
    score += If(cond326, 1, 0)

    # Condition 327
    cond327 = (flag[7] == 100)
    score += If(cond327, 1, 0)

    # Condition 328
    cond328 = (flag[0] == 0x50)
    score += If(cond328, 1, 0)

    # Condition 329
    cond329 = (flag[22] == 0x61)
    score += If(cond329, 1, 0)

    # Condition 330
    cond330 = ((flag[62] + flag[55] & 0xFF) == ord('e'))
    score += If(cond330, 1, 0)

    # Condition 331
    cond331 = (flag[52] == 0x30)
    score += If(cond331, 1, 0)

    # Condition 332
    cond332 = ((flag[7] + flag[22] & 0xFF) == 0xcc)
    score += If(cond332, 1, 0)

    # Condition 333
    cond333 = ((flag[26] ^ flag[14]) == 7)
    score += If(cond333, 1, 0)

    # Condition 334
    cond334 = (flag[2] == 0x54)
    score += If(cond334, 1, 0)

    # Condition 335
    cond335 = (flag[46] == 0x32)
    score += If(cond335, 1, 0)

    # Condition 336
    cond336 = (flag[52] == 0x30)
    score += If(cond336, 1, 0)

    # Condition 337
    cond337 = ((flag[54] ^ flag[35]) == 6)
    score += If(cond337, 1, 0)

    # Condition 338
    cond338 = ((flag[31] ^ flag[34]) == 0x55)
    score += If(cond338, 1, 0)

    # Condition 339
    cond339 = (flag[33] == 0x32)
    score += If(cond339, 1, 0)

    # Condition 340
    cond340 = ((flag[40] + flag[33] & 0xFF) == 0x94)
    score += If(cond340, 1, 0)

    # Condition 341
    cond341 = (flag[7] == 100)
    score += If(cond341, 1, 0)

    # Condition 342
    cond342 = (flag[15] == 0x37)
    score += If(cond342, 1, 0)

    # Condition 343
    cond343 = ((flag[10] ^ flag[43]) == 0x54)
    score += If(cond343, 1, 0)

    # Condition 344
    cond344 = (flag[15] == 0x37)
    score += If(cond344, 1, 0)

    # Condition 345
    cond345 = ((flag[29] + flag[30] & 0xFF) == ord('h'))
    score += If(cond345, 1, 0)

    # Condition 346
    cond346 = ((flag[43] ^ flag[13]) == 1)
    score += If(cond346, 1, 0)

    # Condition 347
    cond347 = ((flag[58] + flag[24] & 0xFF) == 0xd9)
    score += If(cond347, 1, 0)

    # Condition 348
    cond348 = ((flag[17] + flag[61] & 0xFF) == ord('i'))
    score += If(cond348, 1, 0)

    # Condition 349
    cond349 = (flag[41] == 0xa6)
    score += If(cond349, 1, 0)

    # Condition 350
    cond350 = ((flag[54] ^ flag[24]) == 0x51)
    score += If(cond350, 1, 0)

    # Condition 351
    cond351 = (flag[62] == 0x30)
    score += If(cond351, 1, 0)

    # Condition 352
    cond352 = ((flag[57] + flag[37] & 0xFF) == 0x96)
    score += If(cond352, 1, 0)

    # Condition 353
    cond353 = ((flag[61] ^ flag[4]) == 0x4b)
    score += If(cond353, 1, 0)

    # Condition 354
    cond354 = ((flag[37] + flag[52] & 0xFF) == ord('c'))
    score += If(cond354, 1, 0)

    # Condition 355
    cond355 = ((flag[21] ^ flag[26]) == 0x3d)
    score += If(cond355, 1, 0)

    # Condition 356
    cond356 = (flag[50] == 0xe9)
    score += If(cond356, 1, 0)

    # Condition 357
    cond357 = ((flag[5] ^ flag[29]) == 7)
    score += If(cond357, 1, 0)

    # Condition 358
    cond358 = (flag[31] == 0x34)
    score += If(cond358, 1, 0)

    # Condition 359
    cond359 = (flag[53] == 1)
    score += If(cond359, 1, 0)

    # Condition 360
    cond360 = ((flag[15] + flag[7] & 0xFF) == 0x9b)
    score += If(cond360, 1, 0)

    # Condition 361
    cond361 = (flag[41] == 0x33)
    score += If(cond361, 1, 0)

    # Condition 362
    cond362 = ((flag[35] + flag[27] & 0xFF) == 0x97)
    score += If(cond362, 1, 0)

    # Condition 363
    cond363 = (flag[42] == 0x39)
    score += If(cond363, 1, 0)

    # Condition 364
    cond364 = (flag[27] == 0x32)
    score += If(cond364, 1, 0)

    # Condition 365
    cond365 = (flag[47] == 0x65)
    score += If(cond365, 1, 0)

    # Condition 366
    cond366 = ((flag[45] ^ flag[30]) == 4)
    score += If(cond366, 1, 0)

    # Condition 367
    cond367 = (flag[30] == 0x33)
    score += If(cond367, 1, 0)

    # Condition 368
    cond368 = (flag[22] == 0x61)
    score += If(cond368, 1, 0)

    # Condition 369
    cond369 = (flag[49] == 0x61)
    score += If(cond369, 1, 0)

    # Condition 370
    cond370 = ((flag[31] + flag[21] & 0xFF) == 0x98)
    score += If(cond370, 1, 0)

    # Condition 371
    cond371 = (flag[24] == 0x32)
    score += If(cond371, 1, 0)

    # Condition 372
    cond372 = (flag[15] == 0x37)
    score += If(cond372, 1, 0)

    # Condition 373
    cond373 = (flag[35] == 0xcb)
    score += If(cond373, 1, 0)

    # Condition 374
    cond374 = ((flag[4] + flag[37] & 0xFF) == 0xae)
    score += If(cond374, 1, 0)

    # Condition 375
    cond375 = (flag[49] == 0x61)
    score += If(cond375, 1, 0)

    # Condition 376
    cond376 = ((flag[7] ^ flag[31]) == 0x50)
    score += If(cond376, 1, 0)

    # Condition 377
    cond377 = ((flag[15] + flag[19] & 0xFF) == ord('m'))
    score += If(cond377, 1, 0)

    # Condition 378
    cond378 = ((flag[30] ^ flag[22]) == 199)
    score += If(cond378, 1, 0)

    # Condition 379
    cond379 = ((flag[16] ^ flag[60]) == 1)
    score += If(cond379, 1, 0)

    # Condition 380
    cond380 = (flag[12] == 0x36)
    score += If(cond380, 1, 0)

    # Condition 381
    cond381 = (flag[28] == 1)
    score += If(cond381, 1, 0)

    # Condition 382
    cond382 = ((flag[44] + flag[58] & 0xFF) == -99)
    score += If(cond382, 1, 0)

    # Condition 383
    cond383 = ((flag[49] ^ flag[37]) == 0x52)
    score += If(cond383, 1, 0)

    # Condition 384
    cond384 = (flag[6] == 0x34)
    score += If(cond384, 1, 0)

    # Condition 385
    cond385 = (flag[38] == 0x32)
    score += If(cond385, 1, 0)

    # Condition 386
    cond386 = (flag[62] == 0x30)
    score += If(cond386, 1, 0)

    # Condition 387
    cond387 = ((flag[37] ^ flag[21]) == 0x57)
    score += If(cond387, 1, 0)

    # Condition 388
    cond388 = ((flag[40] + flag[5] & 0xFF) == 0x94)
    score += If(cond388, 1, 0)

    # Condition 389
    cond389 = ((flag[11] + flag[34] & 0xFF) == 0x93)
    score += If(cond389, 1, 0)

    # Condition 390
    cond390 = (flag[43] == 0x99)
    score += If(cond390, 1, 0)

    # Condition 391
    cond391 = ((flag[22] + flag[27] & 0xFF) == 0x88)
    score += If(cond391, 1, 0)

    # Condition 392
    cond392 = (flag[46] == flag[38])
    score += If(cond392, 1, 0)

    # Condition 393
    cond393 = ((flag[48] ^ flag[61]) == 5)
    score += If(cond393, 1, 0)

    # Condition 394
    cond394 = (flag[12] == 0x56)
    score += If(cond394, 1, 0)

    # Condition 395
    cond395 = ((flag[44] ^ flag[28]) == 0x51)
    score += If(cond395, 1, 0)

    # Condition 396
    cond396 = (flag[45] == 0x37)
    score += If(cond396, 1, 0)

    # Condition 397
    cond397 = ((flag[37] ^ flag[2]) == 0x67)
    score += If(cond397, 1, 0)

    # Condition 398
    cond398 = ((flag[54] ^ flag[16]) == 0x7b)
    score += If(cond398, 1, 0)

    # Condition 399
    cond399 = ((flag[45] ^ flag[18]) == 0x91)
    score += If(cond399, 1, 0)

    # Condition 400
    cond400 = (flag[18] == 100)
    score += If(cond400, 1, 0)    

    
    opt.maximize(score)
    
    if opt.check() == sat:
        model = opt.model()
        solution = ''.join([chr(model.eval(flag[i]).as_long()) for i in range(0x41)])
        print(f"Found flag: {solution}")
    else:
        print("No solution found")

if __name__ == "__main__":
    solve_flag()