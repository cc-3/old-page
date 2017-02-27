---
layout: post
title:  "Proyecto 2: ArmV8 Assembler"
date:   2017-03-01
category: proyecto
description: >
    El objetivo de este proyecto es que ustedes desarrollen su habilidad trabajando en lenguaje ensamblador, y que logren entender como se codifica el set de instrucciones, en este caso ARMv8 
    a un formato que su computadora puede entender y ejecutar.
permalink: /:categories/:title.html
---

### Preambulo:

El set de instrucciones ARMv8 es muy vasto (incluso tomando en cuenta que es una arquitectura RISC), y no nos daría tiempo de codificar todas las instrucciones en estas dos semanas, así que lo
primero que tenemos que hacer es escoger un subset de instrucciones sobre las que vamos a trabajar. Para este proyecto, las instrucciones que deberán codificar serán las siguientes:

<table>
	<tr>
		<th colspan="3">Operaciones Entre Registros de 64 Bits</th>
	</tr>
	<tr>
		<td>Instruccion</td>
		<td>Formato</td>
		<td>Interpretacion</td>
	</tr>
	<tr>
		<td>ADD</td>
		<td>ADD xd, xn, xm</td>
		<td>xd = xn + xm</td>
	</tr>
	<tr>
		<td>ADD</td>
		<td>ADD xd, xn, imm</td>
		<td>xd = xn + imm</td>
	</tr>
	<tr>
		<td>ADDS</td>
		<td>ADDS xd, xn, xm</td>
		<td>xd = xn + xm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>ADDS</td>
		<td>ADDS xd, xn, imm</td>
		<td>xd = xn + imm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>SUB</td>
		<td>SUB xd, xn, xm</td>
		<td>xd = xn - xm</td>
	</tr>
	<tr>
		<td>SUB</td>
		<td>SUB xd, xn, imm</td>
		<td>xd = xn - imm</td>
	</tr>
	<tr>
		<td>SUBS</td>
		<td>SUBS xd, xn, xm</td>
		<td>xd = xn - xm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>SUBS</td>
		<td>SUBS xd, xn, imm</td>
		<td>xd = xn - imm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>AND</td>
		<td>AND xd, xn, xm</td>
		<td>xd = xn & xm</td>
	</tr>
	<tr>
		<td>AND</td>
		<td>AND xd, xn, imm</td>
		<td>xd = xn & imm</td>
	</tr>
	<tr>
		<td>ANDS</td>
		<td>ANDS xd, xn, xm</td>
		<td>xd = xn & xm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>ANDS</td>
		<td>ANDS xd, xn, imm</td>
		<td>xd = xn & imm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>ORR</td>
		<td>ORR xd, xn, xm</td>
		<td>xd = xn | xm</td>
	</tr>
	<tr>
		<td>ORR</td>
		<td>ORR xd, xn, imm</td>
		<td>xd = xn | imm</td>
	</tr>
	<tr>
		<td>EOR</td>
		<td>EOR xd, xn, xm</td>
		<td>xd = xn ^ xm</td>
	</tr>
	<tr>
		<td>EOR</td>
		<td>EOR xd, xn, imm</td>
		<td>xd = xn ^ imm</td>
	</tr>
	<tr>
		<td>LSL</td>
		<td>LSL xd, xn, xm</td>
		<td>xd = xn << xm</td>
	</tr>
	<tr>
		<td>LSR</td>
		<td>LSR xd, xn, xm</td>
		<td>xd = xn >> xm</td>
	</tr>
	<tr>
		<td>ASR</td>
		<td>ASR xd, xn, xm</td>
		<td>xd = xn >> xm (sign extended)</td>
	</tr>
	<tr>
		<td>MOV</td>
		<td>MOV xd, imm {, LSL #&lt;shamt&gt; }</td>
		<td>xd = imm << shamt (Llena con 0's lo demas)</td>
	</tr>
	<tr>
		<td>MOVN</td>
		<td>MOVN xd, imm {, LSL #&lt;shamt&gt;}</td>
		<td>xd = ~ imm << shamt (Llena con 0's lo demas)</td>
	</tr>
	<tr>
		<td>MOVK</td>
		<td>MOVK xd, imm {, LSL #&lt;shamt&gt;}</td>
		<td>xd = imm << shamt (Deja los demas bits intactos)</td>
	</tr>
	<tr>
		<td>CBZ</td>
		<td>CBZ xd, my_label</td>
		<td>Si (xd == 0), saltar a my_label</td>
	</tr>
	<tr>
		<td>CBNZ</td>
		<td>CBNZ xd, my_label</td>
		<td>Si (xd != 0), saltar a my_label</td>
	</tr>
	<tr>
		<td>B.EQ</td>
		<td>B.EQ my_label</td>
		<td>Si (Z == 1), saltar a my_label</td>
	</tr>
	<tr>
		<td>B.NE</td>
		<td>B.NE my_label</td>
		<td>Si (Z == 0), saltar a my_label</td>
	</tr>
	<tr>
		<td>B.HS</td>
		<td>B.HS my_label</td>
		<td>Si (C == 1), saltar a my_label</td>
	</tr>
	<tr>
		<td>B.LO</td>
		<td>B.LO my_label</td>
		<td>Si (C == 0), saltar a my_label</td>
	</tr>
	<tr>
		<td>B.MI</td>
		<td>B.MI my_label</td>
		<td>Si (N == 1), saltar a my_label</td>
	</tr>
	<tr>
		<td>B</td>
		<td>B my_label</td>
		<td>Saltar a my_label</td>
	</tr>
	<tr>
		<td>BL</td>
		<td>BL my_label</td>
		<td>Saltar a my_label, x30 = PC</td>
	</tr>
	<tr>
		<td>LDR</td>
		<td>LDR xt,=my_label</td>
		<td>Carga en xt la dirección de my_label</td>
	</tr>
	<tr>
		<td>LDR</td>
		<td>LDR xt,[xn,imm]</td>
		<td>Carga en xt lo que hay en la dirección xn con offset imm</td>
	</tr>
	<tr>
		<td>STR</td>
		<td>STR xt,[xn,imm]</td>
		<td>Guarda xt en la dirección xn con offset imm </td>
	</tr>
</table>


