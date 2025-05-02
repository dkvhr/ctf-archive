#include<stdio.h>
#include<stdlib.h>

void bump(int *s) {
	*s = *s + 1;
	printf("score: %d\n", *s);
}

int main(void)

{
  char buffer [65];
  int score = 0;
  
  setvbuf(stdout,(char *)0x0,2,0);
  printf("=== The Prospector\'s Claim ===\n");
  printf("Old Man Jenkins\' map to his modest gold claim has been floating around\n");
  printf("Fool\'s Gulch for years. Most folks think it\'s worthless, but you\'ve\n");
  printf("noticed something peculiar in the worn-out corners...\n\n");
  printf("Enter the claim sequence: ");
  fgets(buffer,65, stdin);
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if ((buffer[0x1f] ^ buffer[0x18]) == 0xaa) {
    bump(&score);
  }
  if ((char)(buffer[0x1f] + buffer[0x2e]) == -0x70) {
    bump(&score);
  }
  if ((char)(buffer[0x3b] + buffer[0x24]) == -0x7f) {
    bump(&score);
  }
  if (buffer[0xd] == -0x42) {
    bump(&score);
  }
  if (buffer[0x20] == 'd') {
    bump(&score);
  }
  if (buffer[0x1a] == '1') {
    bump(&score);
  }
  if (buffer[0x2a] == '9') {
    bump(&score);
  }
  if ((char)(buffer[0x2d] + buffer[0x3f]) == -0x6d) {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if ((char)('C' + buffer[0xf]) == '8') {
    bump(&score);
  }
  if ((buffer[0xd] ^ buffer[0x23]) == 0x8e) {
    bump(&score);
  }
  if (('C' ^ buffer[0x2e]) == 0x71) {
    bump(&score);
  }
  if (buffer[0x2a] == -0x4c) {
    bump(&score);
  }
  if (buffer[0x13] == '6') {
    bump(&score);
  }
  if (buffer[0x1c] == buffer[0x30]) {
    bump(&score);
  }
  if ((buffer[10] ^ buffer[0x21]) == 3) {
    bump(&score);
  }
  if (buffer[0x1e] == 'v') {
    bump(&score);
  }
  if (buffer[5] == '2') {
    bump(&score);
  }
  if (('C' ^ buffer[0x30]) == 0x85) {
    bump(&score);
  }
  if ('T' == 'T') {
    bump(&score);
  }
  if (buffer[0x17] == -0x1f) {
    bump(&score);
  }
  if ((buffer[9] ^ buffer[0x36]) == 0x81) {
    bump(&score);
  }
  if ((char)(buffer[0x35] + buffer[0x1a]) == 'a') {
    bump(&score);
  }
  if ((buffer[0x12] ^ buffer[0x39]) == 7) {
    bump(&score);
  }
  if ((buffer[0x12] ^ buffer[5]) == 0x56) {
    bump(&score);
  }
  if ((char)(buffer[0xe] + buffer[0x35]) == 'f') {
    bump(&score);
  }
  if ((buffer[0x30] ^ buffer[0x38]) == 0x54) {
    bump(&score);
  }
  if (buffer[0x34] == -0x1b) {
    bump(&score);
  }
  if (buffer[0x24] == 'o') {
    bump(&score);
  }
  if ((char)(buffer[0x25] + buffer[0x1e]) == 'f') {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if (buffer[0x17] == '8') {
    bump(&score);
  }
  if (buffer[0x27] == '4') {
    bump(&score);
  }
  if ((char)(buffer[0x38] + buffer[0x13]) == -0x69) {
    bump(&score);
  }
  if ((buffer[0x13] ^ buffer[0x32]) == 0x2d) {
    bump(&score);
  }
  if ((char)(buffer[0x22] + 'C') == -0x5c) {
    bump(&score);
  }
  if ((char)(buffer[0x2f] + buffer[0x26]) == -0xc) {
    bump(&score);
  }
  if ((char)(buffer[0x1b] + buffer[0x2f]) == -0x69) {
    bump(&score);
  }
  if ((char)(buffer[0x2f] + buffer[10]) == -0x6a) {
    bump(&score);
  }
  if ('T' == 'r') {
    bump(&score);
  }
  if (buffer[0x3b] == '6') {
    bump(&score);
  }
  if (buffer[0x1c] == -0x4f) {
    bump(&score);
  }
  if ((buffer[8] ^ buffer[0x3a]) == 8) {
    bump(&score);
  }
  if (('T' ^ buffer[0x2e]) == 0x3a) {
    bump(&score);
  }
  if (buffer[0x3b] == 'D') {
    bump(&score);
  }
  if (buffer[0x39] == '\x12') {
    bump(&score);
  }
  if ((buffer[0x11] ^ buffer[0x28]) == 0x5b) {
    bump(&score);
  }
  if (buffer[0x29] == '*') {
    bump(&score);
  }
  if (buffer[0x29] == '3') {
    bump(&score);
  }
  if ((char)(buffer[0x1a] + buffer[0x26]) == '?') {
    bump(&score);
  }
  if ((buffer[0x3d] ^ 'P') == 0x60) {
    bump(&score);
  }
  if (buffer[0x15] == '$') {
    bump(&score);
  }
  if ((char)(buffer[5] + buffer[0x2b]) == '-') {
    bump(&score);
  }
  if (buffer[0x39] == 'c') {
    bump(&score);
  }
  if ((buffer[0x37] ^ buffer[0x34]) == 5) {
    bump(&score);
  }
  if ('{' == '{') {
    bump(&score);
  }
  if ((char)(buffer[0x10] + buffer[9]) == -0x53) {
    bump(&score);
  }
  if ((char)(buffer[0x16] + buffer[0x2d]) == -0x68) {
    bump(&score);
  }
  if (buffer[0x18] == '2') {
    bump(&score);
  }
  if (buffer[0x30] == '5') {
    bump(&score);
  }
  if ((buffer[0x36] ^ buffer[0x13]) == 0x5b) {
    bump(&score);
  }
  if ((char)(buffer[0x36] + buffer[0xe]) == -0x67) {
    bump(&score);
  }
  if (buffer[0x35] == -0x2e) {
    bump(&score);
  }
  if (('P' ^ buffer[0x30]) == 0x65) {
    bump(&score);
  }
  if ((char)(buffer[0x2a] + buffer[0x31]) == -0x66) {
    bump(&score);
  }
  if ((char)(buffer[0x14] + buffer[0x1d]) == -0x6a) {
    bump(&score);
  }
  if ((buffer[0x28] ^ buffer[0x32]) == 0xda) {
    bump(&score);
  }
  if ((char)(buffer[0x3c] + buffer[0x20]) == -0x6a) {
    bump(&score);
  }
  if ((char)(buffer[0x27] + buffer[7]) == -0x68) {
    bump(&score);
  }
  if (buffer[0x32] == buffer[10]) {
    bump(&score);
  }
  if ((buffer[0x39] ^ buffer[10]) == 0x52) {
    bump(&score);
  }
  if (buffer[0x38] == 'a') {
    bump(&score);
  }
  if (buffer[0x14] == 'a') {
    bump(&score);
  }
  if ((buffer[0x3e] ^ buffer[8]) == 1) {
    bump(&score);
  }
  if ( (buffer[0x2c] ^ buffer[0x22]) == 0x30) {
    bump(&score);
  }
  if (buffer[0x21] == '2') {
    bump(&score);
  }
  if ( (buffer[0x2f] ^ buffer[0x31]) == 4) {
    bump(&score);
  }
  if ( (buffer[0x1b] ^ buffer[0x16]) == 0x53) {
    bump(&score);
  }
  if ((char)('P' + buffer[0x29]) == -0x7d) {
    bump(&score);
  }
  if (buffer[0x12] == -0xf) {
    bump(&score);
  }
  if (buffer[0x1c] == '5') {
    bump(&score);
  }
  if (buffer[0x10] == -0x2d) {
    bump(&score);
  }
  if ((char)(buffer[6] + buffer[0x2f]) == -0x67) {
    bump(&score);
  }
  if ((char)(buffer[0x1c] + buffer[0x19]) == -0x51) {
    bump(&score);
  }
  if ((char)(buffer[0x3f] + buffer[0x13]) == -0x4d) {
    bump(&score);
  }
  if (buffer[0x1d] == '5') {
    bump(&score);
  }
  if (buffer[0x3d] == '0') {
    bump(&score);
  }
  if ((char)(buffer[0xf] + buffer[0x19]) == -0x7b) {
    bump(&score);
  }
  if ( (buffer[0x14] ^ buffer[0x3d]) == 0x4f) {
    bump(&score);
  }
  if ( (buffer[0x1b] ^ buffer[0x32]) == 3) {
    bump(&score);
  }
  if ((char)(buffer[0x3e] + buffer[0x33]) == 'b') {
    bump(&score);
  }
  if ((char)(buffer[0x14] + buffer[0x2c]) == -0x3b) {
    bump(&score);
  }
  if ((char)(buffer[0x2b] + buffer[0x12]) == -0x37) {
    bump(&score);
  }
  if ((char)(buffer[9] + buffer[0x24]) == 'h') {
    bump(&score);
  }
  if (buffer[9] == buffer[0x13]) {
    bump(&score);
  }
  if ( (buffer[0x13] ^ buffer[0x21]) == 4) {
    bump(&score);
  }
  if ((char)(buffer[0x37] + 'P') == -0x7b) {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if (buffer[0x11] == '9') {
    bump(&score);
  }
  if (buffer[10] == '1') {
    bump(&score);
  }
  if (buffer[0x35] == '0') {
    bump(&score);
  }
  if ((char)(buffer[0x31] + buffer[0x3d]) == -0x17) {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if ((char)(buffer[0x37] + 'F') == -0x41) {
    bump(&score);
  }
  if ((char)(buffer[0x2d] + buffer[0x19]) == -0x67) {
    bump(&score);
  }
  if (buffer[0x2e] == '2') {
    bump(&score);
  }
  if ((char)(buffer[0x18] + buffer[0x2b]) == -0x69) {
    bump(&score);
  }
  if (buffer[0x1a] == '1') {
    bump(&score);
  }
  if (buffer[0xe] == '6') {
    bump(&score);
  }
  if ((char)('F' + buffer[0x3e]) == 'v') {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if ( (buffer[0x3f] ^ buffer[0x2d]) == 0x4a) {
    bump(&score);
  }
  if ((char)(buffer[0x2c] + buffer[0xe]) == -0x10) {
    bump(&score);
  }
  if (buffer[9] == -0x28) {
    bump(&score);
  }
  if ((char)(buffer[0x3a] + buffer[0x3e]) == 'b') {
    bump(&score);
  }
  if ((char)(buffer[0x3d] + buffer[0x16]) == -0x6d) {
    bump(&score);
  }
  if ( (buffer[0x33] ^ buffer[0x35]) == 2) {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if ( (buffer[0x32] ^ buffer[0x3b]) == 7) {
    bump(&score);
  }
  if (buffer[0x34] == '0') {
    bump(&score);
  }
  if (buffer[0x21] == 'y') {
    bump(&score);
  }
  if (buffer[0x3d] == '3') {
    bump(&score);
  }
  if ((char)(buffer[0x15] + buffer[0x31]) == -0x3b) {
    bump(&score);
  }
  if (buffer[0x24] == 'S') {
    bump(&score);
  }
  if (buffer[0xf] == '\t') {
    bump(&score);
  }
  if ((char)('P' + buffer[0x20]) == -0x4c) {
    bump(&score);
  }
  if ((char)(buffer[0xe] + buffer[0x33]) == 'h') {
    bump(&score);
  }
  if ( (buffer[0x2b] ^ buffer[0xe]) == 0xfb) {
    bump(&score);
  }
  if (buffer[0x3a] == 'O') {
    bump(&score);
  }
  if (buffer[10] == '>') {
    bump(&score);
  }
  if (buffer[0x2f] == -0x14) {
    bump(&score);
  }
  if (buffer[0x2d] == '7') {
    bump(&score);
  }
  if ((char)(buffer[0x16] + buffer[0x3b]) == -1) {
    bump(&score);
  }
  if ( (buffer[0x18] ^ 'T') == 0x28) {
    bump(&score);
  }
  if (buffer[0x30] == -0x2f) {
    bump(&score);
  }
  if ( (buffer[0x37] ^ buffer[7]) == 0xe8) {
    bump(&score);
  }
  if (buffer[0x2f] == 'e') {
    bump(&score);
  }
  if ((char)(buffer[5] + buffer[0x39]) == -4) {
    bump(&score);
  }
  if ((char)(buffer[0x18] + buffer[5]) == 'd') {
    bump(&score);
  }
  if ( (buffer[0x22] ^ buffer[0x36]) == 2) {
    bump(&score);
  }
  if (buffer[9] == '6') {
    bump(&score);
  }
  if (buffer[5] == '2') {
    bump(&score);
  }
  if (buffer[0x1a] == '1') {
    bump(&score);
  }
  if (buffer[0x3c] == '2') {
    bump(&score);
  }
  if ((char)('{' + buffer[7]) == -0x21) {
    bump(&score);
  }
  if (buffer[0x1f] == '4') {
    bump(&score);
  }
  if ( (buffer[0x32] ^ buffer[0x34]) == 0x59) {
    bump(&score);
  }
  if (buffer[0x3a] == '9') {
    bump(&score);
  }
  if ( (buffer[0xc] ^ buffer[0x2b]) == 0x53) {
    bump(&score);
  }
  if (buffer[7] == 'a') {
    bump(&score);
  }
  if ( (buffer[0x35] ^ buffer[7]) == 0x54) {
    bump(&score);
  }
  if ((char)(buffer[0x3b] + buffer[6]) == 'j') {
    bump(&score);
  }
  if ((char)(buffer[0x11] + buffer[0x1c]) == 'n') {
    bump(&score);
  }
  if ('{' == '{') {
    bump(&score);
  }
  if (buffer[0x23] == 'e') {
    bump(&score);
  }
  if ((char)(buffer[0x24] + buffer[0x2c]) == -0x6a) {
    bump(&score);
  }
  if (buffer[0x3f] == '}') {
    bump(&score);
  }
  if ( (buffer[0x1b] ^ buffer[0x29]) == 0x5d) {
    bump(&score);
  }
  if (buffer[0x28] == 'b') {
    bump(&score);
  }
  if ( (buffer[0x18] ^ buffer[0x15]) == 99) {
    bump(&score);
  }
  if ( (buffer[0x15] ^ buffer[0x13]) == 0x52) {
    bump(&score);
  }
  if (buffer[10] == '1') {
    bump(&score);
  }
  if ((char)(buffer[0x25] + buffer[6]) == 'g') {
    bump(&score);
  }
  if (buffer[6] == '{') {
    bump(&score);
  }
  if (buffer[0x38] == -0x6d) {
    bump(&score);
  }
  if ( (buffer[9] ^ buffer[0x1d]) == 3) {
    bump(&score);
  }
  if (buffer[0x2f] == -0x39) {
    bump(&score);
  }
  if (buffer[0x1d] == '5') {
    bump(&score);
  }
  if (buffer[0x3f] == '}') {
    bump(&score);
  }
  if ((char)(buffer[0x33] + buffer[0x26]) == 'G') {
    bump(&score);
  }
  if ((char)(buffer[0x3c] + buffer[0x14]) == -0x6d) {
    bump(&score);
  }
  if ( ('C' ^ buffer[0xf]) == 0x74) {
    bump(&score);
  }
  if ( (buffer[0xb] ^ buffer[0x3a]) == 0x16) {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if ((char)('P' + buffer[0x3f]) == -0x33) {
    bump(&score);
  }
  if (buffer[0x3c] == '2') {
    bump(&score);
  }
  if (buffer[0x36] == 'c') {
    bump(&score);
  }
  if (buffer[7] == 'K') {
    bump(&score);
  }
  if ( (buffer[0x1d] ^ buffer[0x28]) == 0x57) {
    bump(&score);
  }
  if (buffer[0x3a] == '9') {
    bump(&score);
  }
  if ( (buffer[0x21] ^ buffer[0x2c]) == 0x56) {
    bump(&score);
  }
  if (buffer[0x11] == -0x6a) {
    bump(&score);
  }
  if (buffer[0x13] == -0x55) {
    bump(&score);
  }
  if ((char)(buffer[0x3b] + buffer[0x33]) == -0x51) {
    bump(&score);
  }
  if (buffer[0x15] == '\x7f') {
    bump(&score);
  }
  if ( (buffer[0x23] ^ buffer[0xb]) == 0xd1) {
    bump(&score);
  }
  if (buffer[0x28] == 'b') {
    bump(&score);
  }
  if ( (buffer[0x12] ^ buffer[0xd]) == 0x5e) {
    bump(&score);
  }
  if (buffer[7] == '\x16') {
    bump(&score);
  }
  if ((char)(buffer[0x36] + buffer[6]) == -0x69) {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if (buffer[0x2d] == '7') {
    bump(&score);
  }
  if ((char)(buffer[0x13] + buffer[5]) == 'h') {
    bump(&score);
  }
  if ('{' == '\x1a') {
    bump(&score);
  }
  if (buffer[0x3e] == '0') {
    bump(&score);
  }
  if ( (buffer[0xc] ^ buffer[0x18]) == 4) {
    bump(&score);
  }
  if ((char)(buffer[0x2e] + buffer[0x20]) == -0x6a) {
    bump(&score);
  }
  if (buffer[0x22] == 'a') {
    bump(&score);
  }
  if ('F' == 'F') {
    bump(&score);
  }
  if ((char)(buffer[0xb] + buffer[0x2f]) == -0x69) {
    bump(&score);
  }
  if (buffer[0x2e] == '2') {
    bump(&score);
  }
  if (buffer[0x19] == '`') {
    bump(&score);
  }
  if (buffer[9] == '6') {
    bump(&score);
  }
  if (buffer[0x1a] == ':') {
    bump(&score);
  }
  if ( (buffer[0x37] ^ buffer[0x2a]) == 0xc) {
    bump(&score);
  }
  if ( (buffer[0x22] ^ buffer[0x13]) == 0x57) {
    bump(&score);
  }
  if (buffer[0x38] == 'a') {
    bump(&score);
  }
  if ( (buffer[0x2b] ^ buffer[0x1f]) == 0x51) {
    bump(&score);
  }
  if (buffer[0x37] == '5') {
    bump(&score);
  }
  if (buffer[9] == -0x57) {
    bump(&score);
  }
  if ((char)(buffer[0x2e] + 'F') == 'x') {
    bump(&score);
  }
  if (buffer[0x30] == '\x1f') {
    bump(&score);
  }
  if ((char)(buffer[0x23] + buffer[0x17]) == -99) {
    bump(&score);
  }
  if (buffer[0x24] == 'm') {
    bump(&score);
  }
  if ( (buffer[0x1e] ^ buffer[0x1c]) == 6) {
    bump(&score);
  }
  if (buffer[0x35] == '0') {
    bump(&score);
  }
  if (buffer[0x14] == -9) {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if ((char)(buffer[0x3c] + buffer[0x2d]) == 'i') {
    bump(&score);
  }
  if ( (buffer[0x29] ^ buffer[0xc]) == 5) {
    bump(&score);
  }
  if ( (buffer[9] ^ buffer[0x2a]) == 0x85) {
    bump(&score);
  }
  if (buffer[0x20] == 'd') {
    bump(&score);
  }
  if (buffer[0x35] == '0') {
    bump(&score);
  }
  if ((char)(buffer[0x26] + buffer[0x37]) == 'g') {
    bump(&score);
  }
  if (buffer[0x20] == buffer[0xd]) {
    bump(&score);
  }
  if (buffer[0x24] == '2') {
    bump(&score);
  }
  if (buffer[0x17] == -0x65) {
    bump(&score);
  }
  if (buffer[0xd] == 'd') {
    bump(&score);
  }
  if (buffer[8] == '1') {
    bump(&score);
  }
  if (buffer[0x24] == '2') {
    bump(&score);
  }
  if (buffer[0xe] == -0x3d) {
    bump(&score);
  }
  if ((char)(buffer[0x29] + buffer[0x15]) == -0x69) {
    bump(&score);
  }
  if ((char)(buffer[0x2d] + buffer[0x25]) == 'j') {
    bump(&score);
  }
  if (buffer[0x20] == '2') {
    bump(&score);
  }
  if (buffer[0x2c] == 'd') {
    bump(&score);
  }
  if ('T' == 'T') {
    bump(&score);
  }
  if ( (buffer[0x23] ^ buffer[0x32]) == 0x54) {
    bump(&score);
  }
  if (buffer[0x33] == '2') {
    bump(&score);
  }
  if (buffer[0x30] == '5') {
    bump(&score);
  }
  if (buffer[0x29] == '3') {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if ((char)(buffer[0x31] + buffer[0x3b]) == -0x69) {
    bump(&score);
  }
  if (buffer[0x24] == '2') {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if ((char)(buffer[0x37] + '{') == '\x12') {
    bump(&score);
  }
  if (buffer[0x2e] == -0x62) {
    bump(&score);
  }
  if ( (buffer[0x16] ^ buffer[0x1f]) == 0x55) {
    bump(&score);
  }
  if (buffer[0x32] == 'C') {
    bump(&score);
  }
  if (buffer[0x17] == '8') {
    bump(&score);
  }
  if (buffer[0x34] == '\f') {
    bump(&score);
  }
  if (buffer[0x34] == '0') {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if (buffer[0xe] == '6') {
    bump(&score);
  }
  if ('T' == 'T') {
    bump(&score);
  }
  if ( (buffer[8] ^ buffer[0x16]) == 0x50) {
    bump(&score);
  }
  if ((char)(buffer[0x23] + 'P') == -0x59) {
    bump(&score);
  }
  if ((char)(buffer[0x27] + 'T') == -0x39) {
    bump(&score);
  }
  if ( (buffer[0x29] ^ buffer[6]) == 7) {
    bump(&score);
  }
  if ((char)(buffer[0x21] + buffer[0xb]) == -0x5b) {
    bump(&score);
  }
  if (buffer[0x19] == 'b') {
    bump(&score);
  }
  if (buffer[0x1a] == '1') {
    bump(&score);
  }
  if ((char)(buffer[0x14] + buffer[0x1b]) == '#') {
    bump(&score);
  }
  if ( (buffer[6] ^ buffer[0x23]) == 0x9c) {
    bump(&score);
  }
  if ( (buffer[0xe] ^ buffer[0xb]) == 4) {
    bump(&score);
  }
  if (buffer[0x27] == '4') {
    bump(&score);
  }
  if ((char)(buffer[0x28] + buffer[0x1f]) == -0x6a) {
    bump(&score);
  }
  if (buffer[0x39] == 'c') {
    bump(&score);
  }
  if (buffer[7] == 'd') {
    bump(&score);
  }
  if (buffer[0xe] == '6') {
    bump(&score);
  }
  if (buffer[5] == 'C') {
    bump(&score);
  }
  if ( (buffer[0x17] ^ buffer[0x16]) == 0x59) {
    bump(&score);
  }
  if (buffer[0x15] == 'd') {
    bump(&score);
  }
  if ( (buffer[0x16] ^ buffer[0x2c]) == 5) {
    bump(&score);
  }
  if (buffer[0x35] == '0') {
    bump(&score);
  }
  if (buffer[0x1f] == '4') {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if ((char)(buffer[0x2e] + buffer[8]) == 'z') {
    bump(&score);
  }
  if ( (buffer[0x19] ^ 'F') == 0x24) {
    bump(&score);
  }
  if (buffer[0x2b] == 'e') {
    bump(&score);
  }
  if (buffer[0x2c] == '\x0f') {
    bump(&score);
  }
  if ( (buffer[0x10] ^ buffer[0x15]) == 0x57) {
    bump(&score);
  }
  if ( (buffer[9] ^ buffer[0x3e]) == 6) {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if ((char)(buffer[0x12] + buffer[0x36]) == -0x2f) {
    bump(&score);
  }
  if (buffer[0x20] == 'd') {
    bump(&score);
  }
  if ((char)(buffer[0x39] + buffer[0x12]) == -0x39) {
    bump(&score);
  }
  if ( (buffer[0x2b] ^ buffer[0x20]) == 1) {
    bump(&score);
  }
  if (buffer[0x11] == -0x5c) {
    bump(&score);
  }
  if ( (buffer[8] ^ buffer[9]) == 7) {
    bump(&score);
  }
  if (buffer[0x28] == 'b') {
    bump(&score);
  }
  if ((char)(buffer[0x38] + '{') == '\n') {
    bump(&score);
  }
  if ((char)(buffer[0x15] + buffer[0x1c]) == -0x67) {
    bump(&score);
  }
  if (buffer[0xc] == '|') {
    bump(&score);
  }
  if ((char)(buffer[0x3f] + buffer[0x12]) == -0x1f) {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if (buffer[0x17] == '8') {
    bump(&score);
  }
  if ((char)(buffer[0x2c] + buffer[0x12]) == -0x38) {
    bump(&score);
  }
  if ((char)(buffer[9] + buffer[0x13]) == 'l') {
    bump(&score);
  }
  if ((char)(buffer[0x3d] + buffer[0xb]) == -0x19) {
    bump(&score);
  }
  if (buffer[0x15] == 'd') {
    bump(&score);
  }
  if ((char)(buffer[0x39] + buffer[0x1f]) == -0x69) {
    bump(&score);
  }
  if ( (buffer[0x1c] ^ buffer[0x28]) == 0x57) {
    bump(&score);
  }
  if (buffer[0x2d] == '7') {
    bump(&score);
  }
  if ((char)(buffer[0xd] + buffer[0x2f]) == -0x37) {
    bump(&score);
  }
  if (buffer[0x12] == 'd') {
    bump(&score);
  }
  if (buffer[0xf] == '7') {
    bump(&score);
  }
  if ( (buffer[0x3a] ^ buffer[0x10]) == 10) {
    bump(&score);
  }
  if ( ('P' ^ buffer[0x15]) == 0x34) {
    bump(&score);
  }
  if ((char)(buffer[0x3e] + buffer[0x31]) == -0x6f) {
    bump(&score);
  }
  if (buffer[0x2e] == '2') {
    bump(&score);
  }
  if ((char)(buffer[0x39] + 'P') == -0x58) {
    bump(&score);
  }
  if (buffer[0x24] == '2') {
    bump(&score);
  }
  if (buffer[0x32] == '1') {
    bump(&score);
  }
  if (buffer[0x30] == '5') {
    bump(&score);
  }
  if (buffer[0x2a] == '9') {
    bump(&score);
  }
  if ((char)(buffer[0x3d] + buffer[0x23]) == -0x6b) {
    bump(&score);
  }
  if ((char)(buffer[0x1b] + 'C') == 'u') {
    bump(&score);
  }
  if (buffer[0x30] == '5') {
    bump(&score);
  }
  if ( (buffer[0x23] ^ buffer[0x21]) == 0x51) {
    bump(&score);
  }
  if ( (buffer[0x1d] ^ buffer[0x39]) == 0x56) {
    bump(&score);
  }
  if (buffer[0x17] == 'K') {
    bump(&score);
  }
  if ((char)(buffer[0x1f] + buffer[0xd]) == -0x54) {
    bump(&score);
  }
  if (buffer[0x27] == 'J') {
    bump(&score);
  }
  if (buffer[0x27] == '4') {
    bump(&score);
  }
  if (buffer[0x21] == 's') {
    bump(&score);
  }
  if (buffer[7] == 'd') {
    bump(&score);
  }
  if ('P' == 'P') {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if ((char)(buffer[0x3e] + buffer[0x37]) == 'e') {
    bump(&score);
  }
  if (buffer[0x34] == '0') {
    bump(&score);
  }
  if ((char)(buffer[7] + buffer[0x16]) == -0x34) {
    bump(&score);
  }
  if ( (buffer[0x1a] ^ buffer[0xe]) == 7) {
    bump(&score);
  }
  if ('T' == 'T') {
    bump(&score);
  }
  if (buffer[0x2e] == '2') {
    bump(&score);
  }
  if (buffer[0x34] == '0') {
    bump(&score);
  }
  if ( (buffer[0x36] ^ buffer[0x23]) == 6) {
    bump(&score);
  }
  if ( (buffer[0x1f] ^ buffer[0x22]) == 0x55) {
    bump(&score);
  }
  if (buffer[0x21] == '2') {
    bump(&score);
  }
  if ((char)(buffer[0x28] + buffer[0x21]) == -0x6c) {
    bump(&score);
  }
  if (buffer[7] == 'd') {
    bump(&score);
  }
  if (buffer[0xf] == '7') {
    bump(&score);
  }
  if ( (buffer[10] ^ buffer[0x2b]) == 0x54) {
    bump(&score);
  }
  if (buffer[0xf] == '7') {
    bump(&score);
  }
  if ((char)(buffer[0x1d] + buffer[0x1e]) == 'h') {
    bump(&score);
  }
  if ( (buffer[0x2b] ^ buffer[0xd]) == 1) {
    bump(&score);
  }
  if ((char)(buffer[0x3a] + buffer[0x18]) == -0x27) {
    bump(&score);
  }
  if ((char)(buffer[0x11] + buffer[0x3d]) == 'i') {
    bump(&score);
  }
  if (buffer[0x29] == -0x5a) {
    bump(&score);
  }
  if ( (buffer[0x36] ^ buffer[0x18]) == 0x51) {
    bump(&score);
  }
  if (buffer[0x3e] == '0') {
    bump(&score);
  }
  if ((char)(buffer[0x39] + buffer[0x25]) == -0x6a) {
    bump(&score);
  }
  if ( (buffer[0x3d] ^ '{') == 0x4b) {
    bump(&score);
  }
  if ((char)(buffer[0x25] + buffer[0x34]) == 'c') {
    bump(&score);
  }
  if ( (buffer[0x15] ^ buffer[0x1a]) == 0x3d) {
    bump(&score);
  }
  if (buffer[0x32] == -0x17) {
    bump(&score);
  }
  if ( (buffer[5] ^ buffer[0x1d]) == 7) {
    bump(&score);
  }
  if (buffer[0x1f] == '4') {
    bump(&score);
  }
  if (buffer[0x35] == '\x01') {
    bump(&score);
  }
  if ((char)(buffer[0xf] + buffer[7]) == -0x65) {
    bump(&score);
  }
  if (buffer[0x29] == '3') {
    bump(&score);
  }
  if ((char)(buffer[0x23] + buffer[0x1b]) == -0x69) {
    bump(&score);
  }
  if (buffer[0x2a] == '9') {
    bump(&score);
  }
  if (buffer[0x1b] == '2') {
    bump(&score);
  }
  if (buffer[0x2f] == 'e') {
    bump(&score);
  }
  if ( (buffer[0x2d] ^ buffer[0x1e]) == 4) {
    bump(&score);
  }
  if (buffer[0x1e] == '3') {
    bump(&score);
  }
  if (buffer[0x16] == 'a') {
    bump(&score);
  }
  if (buffer[0x31] == 'a') {
    bump(&score);
  }
  if ((char)(buffer[0x1f] + buffer[0x15]) == -0x68) {
    bump(&score);
  }
  if (buffer[0x18] == '2') {
    bump(&score);
  }
  if (buffer[0xf] == '7') {
    bump(&score);
  }
  if (buffer[0x23] == -0x35) {
    bump(&score);
  }
  if ((char)('{' + buffer[0x25]) == -0x52) {
    bump(&score);
  }
  if (buffer[0x31] == 'a') {
    bump(&score);
  }
  if ( (buffer[7] ^ buffer[0x1f]) == 0x50) {
    bump(&score);
  }
  if ((char)(buffer[0xf] + buffer[0x13]) == 'm') {
    bump(&score);
  }
  if ( (buffer[0x1e] ^ buffer[0x16]) == 199) {
    bump(&score);
  }
  if ( (buffer[0x10] ^ buffer[0x3c]) == 1) {
    bump(&score);
  }
  if (buffer[0xc] == '6') {
    bump(&score);
  }
  if (buffer[0x1c] == '\x01') {
    bump(&score);
  }
  if ((char)(buffer[0x2c] + buffer[0x3a]) == -99) {
    bump(&score);
  }
  if ( (buffer[0x31] ^ buffer[0x25]) == 0x52) {
    bump(&score);
  }
  if (buffer[6] == '4') {
    bump(&score);
  }
  if (buffer[0x26] == '2') {
    bump(&score);
  }
  if (buffer[0x3e] == '0') {
    bump(&score);
  }
  if ( (buffer[0x25] ^ buffer[0x15]) == 0x57) {
    bump(&score);
  }
  if ((char)(buffer[0x28] + buffer[5]) == -0x6c) {
    bump(&score);
  }
  if ((char)(buffer[0xb] + buffer[0x22]) == -0x6d) {
    bump(&score);
  }
  if (buffer[0x2b] == -0x67) {
    bump(&score);
  }
  if ((char)(buffer[0x16] + buffer[0x1b]) == -0x78) {
    bump(&score);
  }
  if (buffer[0x2e] == buffer[0x26]) {
    bump(&score);
  }
  if ( (buffer[0x30] ^ buffer[0x3d]) == 5) {
    bump(&score);
  }
  if (buffer[0xc] == 'V') {
    bump(&score);
  }
  if ( (buffer[0x2c] ^ buffer[0x1c]) == 0x51) {
    bump(&score);
  }
  if (buffer[0x2d] == '7') {
    bump(&score);
  }
  if ( (buffer[0x25] ^ 'T') == 0x67) {
    bump(&score);
  }
  if ( (buffer[0x36] ^ buffer[0x10]) == 0x7b) {
    bump(&score);
  }
  if ( (buffer[0x2d] ^ buffer[0x12]) == 0x91) {
    bump(&score);
  }
  if (buffer[0x12] == 'd') {
    bump(&score);
  }
  if (score < 0x119) {
    if (score < 0xFC) {
      if (score < 0x8C) {
        printf("\nThat claim\'s as empty as a desert well in August.\n",
               (ulong)(uint)(score - 0x8C));
        printf("Not a speck of gold to be found. Try another spot, prospector!\n");
      }
      else {
        printf("\nYou\'ve been swindled, partner! All you\'ve dug up is worthless rock.\n",
               (ulong)(uint)(score - 0x8C));
        printf("The saloon erupts in laughter as you show off your \'treasure\'.\n");
        printf("Keep prospecting - or take up farming instead!\n");
      }
    }
    else {
      printf("\nA few gold flakes glimmer in your pan, but it ain\'t enough to stake a claim.\n",
             (ulong)(uint)(score - 0xFC));
      printf("The assayer laughs you out of his office. \"Come back when you\'ve got\n");
      printf("something worth my time, greenhorn!\"\n");
    }
  }
  else {
    printf("You\'ve struck a rich vein of gold! Your claim is officially recorded\n");
    printf("at the assayer\'s office, and the flag is yours: %s\n",buffer);
  }
  return 0;
}
