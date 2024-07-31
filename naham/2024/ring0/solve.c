#include<stdio.h>
#include<string.h>

int main(void) {
  char tmp;
  char *local_88 = "eyrnou jngkiaccre af suryot arsto  tdyea rre aouY";
  for (int k = 0; k < 0x30; k = k + 2) {
    tmp = local_88[k];
    local_88[k] = local_88[k + 1];
    local_88[k + 1] = tmp;
  }
  printf("first alteration: %s\n", local_88);
  for (int j = 0; j < 0x32; j = j + 1) {
    tmp = local_88[j];
    local_88[j] = local_88[j + 1];
    local_88[j + 1] = tmp;
  }
  printf("second alteration: %s\n", local_88);
  //local_88 = strrev(local_88);
  int len = strlen(local_88);
  for (int i = 0, l = len - 1; i <= l; i++, l--) {
      // swapping characters
      char c = local_88[i];
      local_88[i] = local_88[l];
      local_88[l] = c;
  }
  printf("third alteration: %s\n", local_88);
}
