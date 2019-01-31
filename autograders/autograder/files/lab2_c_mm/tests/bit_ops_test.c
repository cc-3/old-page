#include "bit_ops.h"

void test_get_bit(unsigned x, unsigned n, unsigned expected) {
  unsigned a = get_bit(x, n);
  if(a!=expected) {
    printf("NO\n");
  } else {
    printf("OK\n");
  }
}

void test_set_bit(unsigned x, unsigned n, unsigned v, unsigned expected) {
  set_bit(&x, n, v);
  if(x!=expected) {
    printf("NO\n");
  } else {
    printf("OK\n");
  }
}

void test_flip_bit(unsigned x, unsigned n, unsigned expected) {
  flip_bit(&x, n);
  if(x!=expected) {
    printf("NO\n");
  } else {
    printf("OK\n");
  }
}

int main(int argc, const char *argv[]){

  test_get_bit(0b1001110,0,0);
  test_get_bit(0b1001110,1,1);
  test_get_bit(0b1001110,5,0);
  test_get_bit(0b11011,3,1);
  test_get_bit(0b11011,2,0);
  test_get_bit(0b11011,9,0);

  test_set_bit(0b1001110,2,0,0b1001010);
  test_set_bit(0b1101101,0,0,0b1101100);
  test_set_bit(0b1001110,2,1,0b1001110);
  test_set_bit(0b1101101,0,1,0b1101101);
  test_set_bit(0b1001110,9,0,0b1001110);
  test_set_bit(0b1101101,4,0,0b1101101);
  test_set_bit(0b1001110,9,1,0b1001001110);
  test_set_bit(0b1101101,7,1,0b11101101);

  test_flip_bit(0b1001110,0,0b1001111);
  test_flip_bit(0b1001110,1,0b1001100);
  test_flip_bit(0b1001110,2,0b1001010);
  test_flip_bit(0b1001110,5,0b1101110);
  test_flip_bit(0b1001110,9,0b1001001110);

  return 0;
}
