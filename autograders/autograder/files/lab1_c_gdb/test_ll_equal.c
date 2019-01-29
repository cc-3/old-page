#include <stdio.h>
#include "node.h"
#include "ll_equal.c"


int main(int argc, char** argv) {
  int i;
  node nodes[10];

  for (i=0; i<10; i++) {
    nodes[i].val = 0;
    nodes[i].next = NULL;
  }

  nodes[0].next = &nodes[1];
  nodes[1].next = &nodes[2];
  nodes[2].next = &nodes[3];

  printf(ll_equal(&nodes[0], &nodes[4])?"NO\n":"OK\n");
  printf(ll_equal(&nodes[0], &nodes[0])?"OK\n":"NO\n");

  return 0;
}
