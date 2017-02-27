---
layout: post
title:  "Proyecto 1: ArmV8 Assembler"
date:   2017-03-01
category: proyecto
description: >
    El objetivo de este proyecto es que ustedes desarrollen su habilidad trabajando en lenguaje ensamblador, y que logren entender como se codifica el set de instrucciones, en este caso ARMv8 
    a un formato que su computadora puede entender y ejecutar.
permalink: /:categories/:title.html
---

### Preambulo:

El set de instrucciones ARMv8 es muy vasto (incluso tomando en cuenta que es una arquitectura RISC), y no nos daria tiempo de codificar todas las intrucciones en estas dos semanas, asi que lo
primero que tenemos que hacer es escoger un subset de instrucciones sobre las que vamos a trabajar. Para este proyecto, las instrucciones que deberan codificar seran las siguientes:

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
</table>


