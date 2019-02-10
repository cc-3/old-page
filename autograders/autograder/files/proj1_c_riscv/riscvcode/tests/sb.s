######################
#      sb TESTS      #
######################

.globl main

.text

main:
  li t0, 0xef
  sb t0, 0(gp)
  sb t0, 1(gp)
  sb t0, 2(gp)
  sb t0, 3(gp)
  sb t0, 4(gp)
  sb t0, 5(gp)
  sb t0, 6(gp)
  sb t0, 7(gp)
  sb t0, 8(gp)
  sb t0, 9(gp)

test01:
  li a1, 1
  mv x1, gp
  li x2, 0xffffffaa
  sb x2, 0(x1)
  lb x30, 0(x1)
  li x29, 0xffffffaa
  bne x30, x29, fail

test02:
  li a1, 2
  mv x1, gp
  li x2, 0x00000000
  sb x2, 1(x1)
  lb x30, 1(x1)
  li x29, 0x00000000
  bne x30, x29, fail

test03:
  li a1, 3
  mv x1, gp
  li x2, 0xffffefa0
  sb x2, 2(x1)
  lh x30, 2(x1)
  li x29, 0xffffefa0
  bne x30, x29, fail

test04:
  li a1, 4
  mv x1, gp
  li x2, 0x0000000a
  sb x2, 3(x1)
  lb x30, 3(x1)
  li x29, 0x0000000a
  bne x30, x29, fail

test05:
  li a1, 5
  mv x1, gp
  addi x1, x1, 7
  li x2, 0xffffffaa
  sb x2, -3(x1)
  lb x30, -3(x1)
  li x29, 0xffffffaa
  bne x30, x29, fail

test06:
  li a1, 6
  mv x1, gp
  addi x1, x1, 7
  li x2, 0x00000000
  sb x2, -2(x1)
  lb x30, -2(x1)
  li x29, 0x00000000
  bne x30, x29, fail

test07:
  li a1, 7
  mv x1, gp
  addi x1, x1, 7
  li x2, 0xffffffa0
  sb x2, -1(x1)
  lb x30, -1(x1)
  li x29, 0xffffffa0
  bne x30, x29, fail

test08:
  li a1, 8
  mv x1, gp
  addi x1, x1, 7
  li x2, 0x0000000a
  sb x2, 0(x1)
  lb x30, 0(x1)
  li x29, 0x0000000a
  bne x30, x29, fail

test09:
  li a1, 9
  mv x1, gp
  addi x1, x1, 8
  li x2, 0x12345678
  addi x4, x1, -32
  sb x2, 32(x4)
  lb x5, 0(x1)
  li x29, 0x00000078
  bne x5, x29, fail

test10:
  li a1, 10
  mv x1, gp
  addi x1, x1, 8
  li x2, 0x00003098
  addi x1, x1, -6
  sb x2, 7(x1)
  mv x4, gp
  addi x4, x4, 9
  lb x5, 0(x4)
  li x29, 0xffffff98
  bne x5, x29, fail

test11:
  li a1, 11
  li x4, 0
label1_test11:
  li x1, 0xffffffdd
  mv x2, gp
  sb x1, 0(x2)
  lb x30, 0(x2)
  li x29, 0xffffffdd
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test11

test12:
  li a1, 12
  li x4, 0
label1_test12:
  li x1, 0xffffffcd
  mv x2, gp
  nop
  sb x1, 1(x2)
  lb x30, 1(x2)
  li x29, 0xffffffcd
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test12

test13:
  li a1, 13
  li x4, 0
label1_test13:
  li x1, 0xffffffcc
  mv x2, gp
  nop
  nop
  sb x1, 2(x2)
  lb x30, 2(x2)
  li x29, 0xffffffcc
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test13

test14:
  li a1, 14
  li x4, 0
label1_test14:
  li x1, 0xffffffbc
  nop
  mv x2, gp
  sb x1, 3(x2)
  lb x30, 3(x2)
  li x29, 0xffffffbc
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test14

test15:
  li a1, 15
  li x4, 0
label1_test15:
  li x1, 0xffffffbb
  nop
  mv x2, gp
  nop
  sb x1, 4(x2)
  lb x30, 4(x2)
  li x29, 0xffffffbb
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test15

test16:
  li a1, 16
  li x4, 0
label1_test16:
  li x1, 0xffffffab
  nop
  nop
  mv x2, gp
  sb x1, 5(x2)
  lb x30, 5(x2)
  li x29, 0xffffffab
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test16

test17:
  li a1, 17
  li x4, 0
label1_test17:
  mv x2, gp
  li x1, 0x00000033
  sb x1, 0(x2)
  lb x30, 0(x2)
  li x29, 0x00000033
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test17

test18:
  li a1, 18
  li x4, 0
label1_test18:
  mv x2, gp
  li x1, 0x00000023
  nop
  sb x1, 1(x2)
  lb x30, 1(x2)
  li x29, 0x00000023
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test18

test19:
  li a1, 19
  li x4, 0
label1_test19:
  mv x2, gp
  li x1, 0x00000022
  nop
  nop
  sb x1, 2(x2)
  lb x30, 2(x2)
  li x29, 0x00000022
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test19

test20:
  li a1, 20
  li x4, 0
label1_test20:
  mv x2, gp
  nop
  li x1, 0x00000012
  sb x1, 3(x2)
  lb x30, 3(x2)
  li x29, 0x00000012
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test20

test21:
  li a1, 21
  li x4, 0
label1_test21:
  mv x2, gp
  nop
  li x1, 0x00000011
  nop
  sb x1, 4(x2)
  lb x30, 4(x2)
  li x29, 0x00000011
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test21

test22:
  li a1, 22
  li x4, 0
label1_test22:
  mv x2, gp
  nop
  nop
  li x1, 0x00000001
  sb x1, 5(x2)
  lb x30, 5(x2)
  li x29, 0x00000001
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test22

success:
  li a0, 10
  ecall

fail:
  li a0, 1
  ecall
  li a0, 10
  ecall
