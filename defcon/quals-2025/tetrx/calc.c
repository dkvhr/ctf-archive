#include <stdio.h>
#include <stdlib.h> 
#include <stdint.h>

#define HIGHD(x) ((int32_t)((x) >> 32))
#define LOWD(x)  ((int32_t)(x))

int sim() {

    int32_t rndval_start = rand();

    int32_t temp0_1;
    int32_t temp1_1;
    uint64_t r8_6;
    int32_t piece_idx_3;

    int64_t rndval_start_64 = (int64_t)rndval_start;
    temp0_1 = HIGHD(rndval_start_64);
    temp1_1 = LOWD(rndval_start_64);  

    int64_t mul_result = rndval_start_64 * -(int64_t)0x6db6db6dL;
    int32_t high_mul = (int32_t)(mul_result >> 32);
    int32_t sum_result = high_mul + temp1_1;
    int32_t shift_result = sum_result >> 2;
    int32_t sub_result = shift_result - temp0_1;
    r8_6 = (uint64_t)sub_result;

    uint64_t r8_6_shifted = r8_6 << 3;
    uint64_t r8_6_times_7 = r8_6_shifted - r8_6;
    int32_t term_to_subtract = (int32_t)r8_6_times_7;
    piece_idx_3 = temp1_1 - term_to_subtract;

    return piece_idx_3;
}


int main() {

    srand(1);

    for(int i = 0; i < 0x100; i++) {
        int x = sim();
        printf("(%d) = %d\n", i, x);
    }
    return 0;
}
