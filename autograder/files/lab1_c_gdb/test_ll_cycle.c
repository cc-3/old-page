#include <stdio.h>
#include "node.h"
#include "ll_cycle.c"
#define BAD "NO\n"
#define OK "OK\n"
void test_ll_has_cycle(void) {
  int i;
  node nodes[25]; //enough to run our tests
  for(i=0; i < sizeof(nodes)/sizeof(node); i++) {
    nodes[i].next = 0;
    nodes[i].val = 0;
  }
  nodes[0].next = &nodes[1];
  nodes[1].next = &nodes[2];
  nodes[2].next = &nodes[3];
  printf(ll_has_cycle(&nodes[0])?BAD:OK);

  nodes[4].next = &nodes[5];
  nodes[5].next = &nodes[6];
  nodes[6].next = &nodes[7];
  nodes[7].next = &nodes[8];
  nodes[8].next = &nodes[9];
  nodes[9].next = &nodes[10];
  nodes[10].next = &nodes[4];
  printf(ll_has_cycle(&nodes[4])?OK:BAD);

  nodes[11].next = &nodes[12];
  nodes[12].next = &nodes[13];
  nodes[13].next = &nodes[14];
  nodes[14].next = &nodes[15];
  nodes[15].next = &nodes[16];
  nodes[16].next = &nodes[17];
  nodes[17].next = &nodes[14];
  printf(ll_has_cycle(&nodes[11])?OK:BAD);

  nodes[18].next = &nodes[18];
  printf(ll_has_cycle(&nodes[18])?OK:BAD);

  nodes[19].next = &nodes[20];
  nodes[20].next = &nodes[21];
  nodes[21].next = &nodes[22];
  nodes[22].next = &nodes[23];
  printf(ll_has_cycle(&nodes[19])?BAD:OK);

  printf(ll_has_cycle(NULL)?BAD:OK);
}

int main(void) {
  test_ll_has_cycle();
  return 0;
}
