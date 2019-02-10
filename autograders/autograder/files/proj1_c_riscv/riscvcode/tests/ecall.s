######################
#    ecall TESTS     #
######################

.globl main

.text

main:

test01:
  li a1, 10
  li a0, 1
  ecall
  li a1, -1
  li a0, 1
  ecall
  li a1, 65535
  li a0, 1
  ecall
  li a0, 10
  ecall
