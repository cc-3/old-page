#include <stdio.h>
#include <stdlib.h>

#include "vector.h"

int main(int argc, char **argv) {
  vector_t *v;

  v = vector_new();
  vector_delete(v);
  v = vector_new();

  if(vector_get(v, 0) == 0){
      if(vector_get(v, 1) == 0){
          if(vector_get(v, 50) == 0){
              printf("OK\n");
          }else{
              printf("NO\n");
          }
      }else{
          printf("NO\n");
      }
   }else{
      printf("NO\n");
   }

  vector_set(v, 0, 98);
  vector_set(v, 11, 15);
  vector_set(v, 15, -23);
  vector_set(v, 24, 65);
  vector_set(v, 500, 3);
  vector_set(v, 12, -123);
  vector_set(v, 15, 21);
  vector_set(v, 25, 43);

  if(vector_get(v, 0) == 98){
    if(vector_get(v, 11) == 15){
      if(vector_get(v, 24) == 65){
          if(vector_get(v, 12) == -123){
              if(vector_get(v, 15) == 21){
                  if(vector_get(v, 25) == 43){
                      if(vector_get(v, 23) == 0){
                          if(vector_get(v, 1) == 0){
                              if(vector_get(v, 501) == 0){
                                  if(vector_get(v, 500) == 3){
                                      printf("OK\n");
                                  }else{
                                      printf("NO\n");
                                  }
                              }else{
                                  printf("NO\n");
                              }
                          }else{
                              printf("NO\n");
                          }
                      }else{
                          printf("NO\n");
                      }
                  }else{
                      printf("NO\n");
                  }
              }else{
                  printf("NO\n");
              }
          }else{
              printf("NO\n");
          }
      }else{
          printf("NO\n");
      }
    }else{
      printf("NO\n");
    }
  }else{
      printf("NO\n");
  }

    vector_delete(v);

  return 0;
}
