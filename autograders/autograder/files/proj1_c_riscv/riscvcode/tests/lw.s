######################
#      lw TESTS      #
######################

.globl main

.text

main:
  li t0, 0x00ff00ff
  li t1, 0xff00ff00
  li t2, 0x0ff00ff0
  li t3, 0xf00ff00f
  sw t0, 0(gp)
  sw t1, 4(gp)
  sw t2, 8(gp)
  sw t3, 12(gp)

test01:
  li a1, 1
  lw x30, 0(gp)
  li x29, 0x00ff00ff
  bne x30, x29, fail

test02:
  li a1, 2
  lw x30, 4(gp)
  li x29, 0xff00ff00
  bne x30, x29, fail

test03:
  li a1, 3
  lw x30, 8(gp)
  li x29, 0x0ff00ff0
  bne x30, x29, fail

test04:
  li a1, 4
  lw x30, 12(gp)
  li x29, 0xf00ff00f
  bne x30, x29, fail

test05:
  li a1, 5
  mv x1, gp
  addi x1, x1, 12
  lw x30, -12(x1)
  li x29, 0x00ff00ff
  bne x30, x29, fail

test06:
  li a1, 6
  mv x1, gp
  addi x1, x1, 12
  lw x30, -8(x1)
  li x29, 0xff00ff00
  bne x30, x29, fail

test07:
  li a1, 7
  mv x1, gp
  addi x1, x1, 12
  lw x30, -4(x1)
  li x29, 0x0ff00ff0
  bne x30, x29, fail

test08:
  li a1, 8
  mv x1, gp
  addi x1, x1, 12
  lw x30, 0(x1)
  li x29, 0xf00ff00f
  bne x30, x29, fail

test09:
  li a1, 9
  mv x1, gp
  addi x1, x1, -32
  lw x5, 32(x1)
  li x29, 0x00ff00ff
  bne x5, x29, fail

test10:
  li a1, 10
  mv x1, gp
  addi x1, x1, -3
  lw x5, 7(x1)
  li x29, 0xff00ff00
  bne x5, x29, fail

test11:
  li a1, 11
  li x4, 0
label1_test11:
  mv x1, gp
  addi x1, x1, 4
  lw x30, 4(x1)
  addi x6, x30, 0
  li x29, 0x0ff00ff0
  bne x6, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test11

test12:
  li a1, 12
  li x4, 0
label1_test12:
  mv x1, gp
  addi x1, x1, 8
  lw x30, 4(x1)
  nop
  addi x6, x30, 0
  li x29, 0xf00ff00f
  bne x6, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test12

test13:
  li a1, 13
  li x4, 0
label1_test13:
  mv x1, gp
  lw x30, 4(x1)
  nop
  nop
  addi x6, x30, 0
  li x29, 0xff00ff00
  bne x6, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test13

test14:
  li a1, 14
  li x4, 0
label1_test14:
  mv x1, gp
  addi x1, x1, 4
  lw x30, 4(x1)
  li x29, 0x0ff00ff0
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test14

test15:
  li a1, 15
  li x4, 0
label1_test15:
  mv x1, gp
  addi x1, x1, 8
  nop
  lw x30, 4(x1)
  li x29, 0xf00ff00f
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test15

test16:
  li a1, 16
  li x4, 0
label1_test16:
  mv x1, gp
  nop
  nop
  lw x30, 4(x1)
  li x29, 0xff00ff00
  bne x30, x29, fail
  addi x4, x4, 1
  li x5, 2
  bne x4, x5, label1_test16

test17:
  li a1, 17
  mv x5, gp
  lw x2, 0(x5)
  li x2, 2
  li x29, 0x00000002
  bne x2, x29, fail

test18:
  li a1, 18
  mv x5, gp
  lw x2, 0(x5)
  nop
  li x2, 2
  li x29, 0x00000002
  bne x2, x29, fail

success:
  li a0, 10
  ecall

fail:
  li a0, 1
  ecall
  li a0, 10
  ecall
