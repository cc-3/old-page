#include <stdio.h>
#include "eccentric.c"


#define FAILED "V%d has an invalid value '%d'\n"
#define PASSED "V%d OK\n"


void test(int num, int success, int v) {
  if (success)
    printf(PASSED, num);
  else
    printf(FAILED, num, v);
}


int main() {
  test(0, V0 == 3, V0);
  test(1, V1 == 3, V1);
  test(2, V2 != 0, V2);
  test(3, V3 == 3, V3);

  return 0;
}
