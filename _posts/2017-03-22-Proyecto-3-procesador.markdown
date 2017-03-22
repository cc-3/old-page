---
layout: post
title:  "Proyecto 3: ArmV8 Processor"
date:   2017-03-01
category: proyecto
description: >
    El objetivo de este proyecto es que ustedes logren implementar una versión funcional de un procesador ARMv8, con un subset de
    instrucciones reducido. Tambien queremos que entiendan realmente como una computadora interpreta estas instrucciones 
    para realizar alguna tarea. 
permalink: /:categories/:title.html
---

### Preámbulo:

Logisim es un pequeño programa escrito en JAVA que nos permite simular componentes basicos de electrónica digital; compuertas,
registros, sumadores, y otras cosas por el estilo. Para este proyecto, ustedes van a diseñar un procesador ARMv8 basados en el set
de instrucciones que codificamos en el proyecto pasado. Tomen en cuenta que no es necesario que hayan terminado el proyecto 
anterior para poder realizar este, pero si lo terminaron, y logran terminar este, podrán ensamblar sus instrucciones con su
segundo proyecto, y ver como se ejecutan con el este.

Hemos establecido 4 tipos de instrucciones en ARMv8; entre registros (R), con valor inmediato (I), saltos condicionales e 
incondicionales (B), y también haremos la distinción de las operaciones a memoria como LDR y STR (que les pondremos... M).
Su procesador debe ser capaz de ejecutar estas instrucciones como lo haría un procesador ARMv8.

Deben asignarse un grupo en GitHub classroom dando click an este 
<a href="https://classroom.github.com/group-assignment-invitations/6d48153b311e637dd3b352885db65dc1">link</a>, 
y tomando en cuenta lo siguiente: <b>Deben mandar un correo con los integrantes de su grupo a efrainh12@galileo.edu antes 
del fin de semana previo a la fecha de entrega, de lo contrario su proyecto estará calificado sobre 50 puntos.</b>

### Qué deben implementar:

Su procesador debe estar dividido en diferentes módulos, o unidades. Cada una de ellas se encargara de una tarea. 
Estas son las unidades que deben implementar:

1. <b>Memory Manager</b>: Contendrá la memoria RAM para lectura/escritura de instrucciones y datos. Para facilitar la implementación,
   ustedes podrán tener dos memorias (una de datos y una de instrucciones), y dejaremos como puntos extra el implementar el
   procesador utilizando únicamente una memoria RAM.

2. <b>Register File</b>: Todos los registros entre los cuales se realizaran las operaciones. (X0 ~ X30, SP, y las banderas Z,N,C,O irán
   Aquí también).

3. <b>Program Counter</b>: Se encargará de llevar un conteo de la siguientes instrucción que toca ejecutar.

4. <b>ALU (Unidad Arimetico Logica)</b>: encargada de todos los procesos de este tipo.
    
5. <b>Instruction Fetcher/Decoder</b>: para decodificar el tipo de instrucción que deben ejecutar (Tipo R, Tipo B o Tipo I, Tipo M).
   Esta es probablemente la parte más importante y difícil de implementar, porque se encarga de controlar todos los demás bloques
   de su procesador.
    
6. <b>Jump Controller</b>: Este moduló debe controlar cuando un programa salta a otra instrucción y cuando no, y debe 
decir a donde tiene que saltar.

### Toys:

Existe una librería para Logisim llamada CS316 que agrega algunos elementos extra (Pantallas LCD, Teclado, etc.) que 
puede usar para su proyecto. Para instalarla solo deben importar el .jar que viene en el repositorio base en
Project/Load Library/JAR Library, y cuando solicite el nombre de la clase deben escribir edu.cornell.cs316.Components 
Esta librería también contiene un Register File, tome en cuenta que este componente <b>no lo podrá utilizar</b>; usted debe crear 
su propia unidad. Exceptuando esto, usted es libre de utilizar cualquier otro componente para su proyecto. 

### Indicaciones Extra:

Los componentes como sumadores, registros, etc., que tiene Logisim llegan a un máximo de 32 bits. Parte de su trabajo 
consiste en crear componentes que soporten 64 bits utilizando dos componentes de 32 bits (verán más de esto en el 
laboratorio de esta semana).

En su procesador, en la memoria de instrucciones, la primer instrucción debe estar en la dirección 0x00000000, y en la memoria de
data, el primer valor deberá también empezar en la dirección 0x00000000. El Stack, por otra parte, se encontrara en la memoria de
datos, y empezara en la dirección 0xFFFFFFFF. Si ustedes deciden utilizar solo una memoria, entonces las instrucciones empezaran
donde mismo, al igual que el Stack, y los datos deberán empezar en 0x00080000.

Lo más complicado del proyecto es unir todos los componentes de la manera correcta; tomen en cuenta esto para emplear correctamente 
su tiempo.

### Timeline Sugerida:

Esta vez, les escribimos la Timeline sugerida desde un inicio, para no atrasarnos nosotros en recordarles que se están atrasando:

<table style="text-align: center;">
	<tr>
		<th>
			Fecha Inicio - Fecha Fin
		</th>
		<th>
			Actividad
		</th>
	</tr>
	<tr>
		<td>
			22 de Marzo - 23 de Marzo
		</td>
		<td>
			Leer las Instrucciones
		</td>
	</tr>
	<tr>
		<td>
			24 de Marzo - 26 de Marzo
		</td>
		<td>
			Register File y 
			ALU implementadas (Instrucciones R y I)
		</td>
	</tr>
	<tr>
		<td>
			27 de Marzo - 28 de Marzo
		</td>
		<td>
			Program Counter Implementado
		</td>
	</tr>
	<tr>
		<td>
			29 de Marzo - 1 de Abril
		</td>
		<td>
			Memory Manager Implementado (Instrucciones M)
		</td>
	</tr>
	<tr>
		<td>
			2 de Abril - 3 de Abril
		</td>
		<td>
			Jump Controller Implementado (Instrucciones B)
		</td>
	</tr>
	<tr>
		<td>
			4 de Abril - 7 de Abril
		</td>
		<td>
			Instruction Fetcher/Decoder Implementado
		</td>
	</tr>
	<tr>
		<td>
			7 de Abril - 10 de Abril
		</td>
		<td>
			Verdadero Instruction Fetcher/Decoder Implementado
		</td>
	</tr>
	<tr>
		<td>
			11 de Abril - 18 de Abril
		</td>
		<td>
			Debugging del general (pero principalmente del Instruction Fetcher/Decoder)
		</td>
	</tr>
</table>

### Entrega:

Para la entrega del proyecto, ustedes deben mandar un correo como especificamos más arriba en este documento. Deben especificar 
los integrantes del grupo (máximo dos) y su sección. Deben trabajar en el repositorio de GitHub Classroom que les asignamos y 
deben subir el link del repositorio al GES antes de la fecha de entrega. Si no cumplen con estos requisitos, tendrán una nota de 
0 en el proyecto. La entrega será presencial únicamente para aquellas personas que saquen una nota muy buena en el proyecto.

### Puntos Extra:

Esta es una lista de cosas que pueden hacer por puntos extra; si consideran que pueden hacer otra cosa que no mencionamos aquí,
consúltenlo antes con nosotros para asegurar que lo que quieren hacer es merecedor de creditos adicionales:

1. Utilizar únicamente una memoria
2. Agregarle pantalla y desplegar cosas de alguna manera
3. Agregar soporte para instrucciones entre registros "W"
4. Agregar teclado y leer los datos de alguna manera
5. Cargar el valor 0xFFFFFFFF al SP automáticamente en el primer ciclo del reloj (cuando lo estén implementado entenderán esto).
6. Agregar pipeline
7. Implementar RET Xd (que es la verdadera codificacion del RET)

Algo muy importante; A pesar de que algunas de estas cosas se vean sencillas de hacer, con excepción de la ultima, la mayoria no 
lo son del todo. Les sugerimos que antes de pensar en puntos extra, terminen lo requerido del proyecto. 

### Set de Instrucciones:

Su procesador debe soportar un subset del set de instrucciones que codificamos en el proyecto anterior. Aquí les adjuntamos 
un copy paste del proyecto anterior, menos un par de instrucciones que no implementaremos:

<table>
	<tr>
		<th colspan="3">Operaciones Entre Registros de 64 Bits</th>
	</tr>
	<tr>
		<td>Instrucción</td>
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
		<td>ANDS</td>
		<td>ANDS xd, xn, xm</td>
		<td>xd = xn & xm (Modifica Banderas)</td>
	</tr>
	<tr>
		<td>ORR</td>
		<td>ORR xd, xn, xm</td>
		<td>xd = xn | xm</td>
	</tr>
	<tr>
		<td>EOR</td>
		<td>EOR xd, xn, xm</td>
		<td>xd = xn ^ xm</td>
	</tr>
	<tr>
		<td>LSLV</td>
		<td>LSLV xd, xn, xm</td>
		<td>xd = xn << xm</td>
	</tr>
	<tr>
		<td>LSRV</td>
		<td>LSRV xd, xn, xm</td>
		<td>xd = xn >> xm</td>
	</tr>
	<tr>
		<td>ASRV</td>
		<td>ASRV xd, xn, xm</td>
		<td>xd = xn >> xm (sign extended)</td>
	</tr>
	<tr>
		<td>RORV</td>
		<td>RORV xd, xn, xm</td>
		<td>xd = xn rotado a la derecha según xm</td>
	</tr>
	<tr>
		<td>MOV</td>
		<td>MOV xd, imm</td>
		<td>xd = imm << shamt (Llena con 0's lo demas)</td>
	</tr>
	<tr>
		<td>MOVN</td>
		<td>MOVN xd, imm</td>
		<td>xd = ~ imm << shamt (Llena con 0's lo demas)</td>
	</tr>
	<tr>
		<td>MOVK</td>
		<td>MOVK xd, imm </td>
		<td>xd = imm << shamt (Deja los demas bits intactos)</td>
	</tr>
	<tr>
		<td>CBZ</td>
		<td>CBZ xd, my_label</td>
		<td>Si (xd == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>CBNZ</td>
		<td>CBNZ xd, my_label</td>
		<td>Si (xd != 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.EQ</td>
		<td>B.EQ my_label</td>
		<td>Si (Z == 1), salta a my_label</td>
	</tr>
	<tr>
		<td>B.NE</td>
		<td>B.NE my_label</td>
		<td>Si (Z == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.HS</td>
		<td>B.HS my_label</td>
		<td>Si (C == 1), salta a my_label</td>
	</tr>
	<tr>
		<td>B.LO</td>
		<td>B.LO my_label</td>
		<td>Si (C == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.MI</td>
		<td>B.MI my_label</td>
		<td>Si (N == 1), salta a my_label</td>
	</tr>
	<tr>
		<td>B.PL</td>
		<td>B.PL my_label</td>
		<td>Si (N == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.VS</td>
		<td>B.VS my_label</td>
		<td>Si (V == 1), salta a my_label</td>
	</tr>
	<tr>
		<td>B.VC</td>
		<td>B.VC my_label</td>
		<td>Si (V == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.HI</td>
		<td>B.HI my_label</td>
		<td>Si (C == 1) & (Z == 0), salta a my_label</td>
	</tr>
	<tr>
		<td>B.LS</td>
		<td>B.LS my_label</td>
		<td>Si (C == 0) | (Z == 1), salta a my_label</td>
	</tr>
	<tr>
		<td>B.GE</td>
		<td>B.GE my_label</td>
		<td>Si (N == V), salta a my_label</td>
	</tr>
	<tr>
		<td>B.LT</td>
		<td>B.LT my_label</td>
		<td>Si (N != V), salta a my_label</td>
	</tr>
	<tr>
		<td>B.GT</td>
		<td>B.GT my_label</td>
		<td>Si (Z == 0) & (N == V), salta a my_label</td>
	</tr>
	<tr>
		<td>B.LE</td>
		<td>B.LE my_label</td>
		<td>Si (Z == 1) | (N !=V), salta a my_label</td>
	</tr>
	<tr>
		<td>B</td>
		<td>B my_label</td>
		<td>Salta a my_label</td>
	</tr>
	<tr>
		<td>BL</td>
		<td>BL my_label</td>
		<td>Salta a my_label, x30 = PC</td>
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
	<tr>
		<td>RET</td>
		<td>RET</td>
		<td>Salta a la dirección especificada en x30</td>
	</tr>
</table>

Con <b>la misma codificacion del proyecto anterior</b>, excepto por LDRB y STRB immediate; estos no los implementaremos:

<table style="text-align: center;">
	<tr>
		<th colspan="32">ADD(S) y SUBS(S) IMMEDIATE (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="1">30</td>
		<td colspan="1">29</td>
		<td colspan="5">28-24</td>
		<td colspan="2">23-22</td>
		<td colspan="12">21-10</td>
		<td colspan="5">9-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="1">op</td>
		<td colspan="1">S</td>
		<td colspan="5">10001</td>
		<td colspan="2">shift</td>
		<td colspan="12">imm(12)</td>
		<td colspan="5">Rn</td>
		<td colspan="5">Rd</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4">ADD(S) y SUBS(S) IMMEDIATE (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td><td>S</td><td>shift</td>
	</tr>
	<tr>
		<td>ADD Xd, Xn, Imm</td><td>0</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>ADDS Xd, Xn, Imm</td><td>0</td><td>1</td><td>00</td>
	</tr>
	<tr>
		<td>SUB Xd, Xn, Imm</td><td>1</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>SUBS Xd, Xn, Imm</td><td>1</td><td>1</td><td>00</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">ADD(S) y SUBS(S) REGISTERS (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="1">30</td>
		<td colspan="1">29</td>
		<td colspan="5">28-24</td>
		<td colspan="2">23-22</td>
		<td colspan="1">21</td>
		<td colspan="5">22-16</td>
		<td colspan="6">15-10</td>
		<td colspan="5">9-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="1">op</td>
		<td colspan="1">S</td>
		<td colspan="5">01011</td>
		<td colspan="2">shift</td>
		<td colspan="1">0</td>
		<td colspan="5">Rm</td>
		<td colspan="6">imm6</td>
		<td colspan="5">Rn</td>
		<td colspan="5">Rd</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="5">ADD(S) y SUBS(S) REGISTERS (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td><td>S</td><td>shift</td><td>imm6</td>
	</tr>
	<tr>
		<td>ADD Xd, Xn, Xm</td><td>0</td><td>0</td><td>00</td><td>000000</td>
	</tr>
	<tr>
		<td>ADDS Xd, Xn, Xm</td><td>0</td><td>1</td><td>00</td><td>000000</td>
	</tr>
	<tr>
		<td>SUB Xd, Xn, Xm</td><td>1</td><td>0</td><td>00</td><td>000000</td>
	</tr>
	<tr>
		<td>SUBS Xd, Xn, Xm</td><td>1</td><td>1</td><td>00</td><td>000000</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">AND(S), ORR y EOR REGISTERS (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="1">30</td>
		<td colspan="1">29</td>
		<td colspan="5">28-24</td>
		<td colspan="2">23-22</td>
		<td colspan="1">21</td>
		<td colspan="5">20-16</td>
		<td colspan="6">15-10</td>
		<td colspan="5">9-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="1">op</td>
		<td colspan="1">S</td>
		<td colspan="5">01010</td>
		<td colspan="2">shift</td>
		<td colspan="1">N</td>
		<td colspan="5">Rm</td>
		<td colspan="6">imm6</td>
		<td colspan="5">Rn</td>
		<td colspan="5">Rd</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="6">AND(S), ORR y EOR REGISTERS (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td><td>S</td><td>shift</td><td>N</td><td>imm6</td>
	</tr>
	<tr>
		<td>AND Xd, Xn, Xm</td><td>0</td><td>0</td><td>00</td><td>0</td><td>000000</td>
	</tr>
	<tr>
		<td>ORR Xd, Xn, Xm</td><td>0</td><td>1</td><td>00</td><td>0</td><td>000000</td>
	</tr>
	<tr>
		<td>EOR Xd, Xn, Xm</td><td>1</td><td>0</td><td>00</td><td>0</td><td>000000</td>
	</tr>
	<tr>
		<td>ANDS Xd, Xn, Xm</td><td>1</td><td>1</td><td>00</td><td>0</td><td>000000</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">LSLV, LSRV, ASRV y RORV REGISTERS (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="1">30</td>
		<td colspan="1">29</td>
		<td colspan="8">28-21</td>
		<td colspan="5">20-16</td>
		<td colspan="6">15-10</td>
		<td colspan="5">9-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="1">op</td>
		<td colspan="1">S</td>
		<td colspan="8">11010110</td>
		<td colspan="5">Rm</td>
		<td colspan="6">opcode</td>
		<td colspan="5">Rn</td>
		<td colspan="5">Rd</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4">LSLV, LSRV, ASRV y RORV REGISTERS (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td><td>S</td><td>opcode</td>
	</tr>
	<tr>
		<td>LSLV Xd, Xn, Xm</td><td>0</td><td>0</td><td>001000</td>
	</tr>
	<tr>
		<td>LSRV Xd, Xn, Xm</td><td>0</td><td>0</td><td>001001</td>
	</tr>
	<tr>
		<td>ASRV Xd, Xn, Xm</td><td>0</td><td>0</td><td>001010</td>
	</tr>
	<tr>
		<td>RORV Xd, Xn, Xm</td><td>0</td><td>0</td><td>001011</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">MOV, MOVN y MOVK IMMEDIATE (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="1">30</td>
		<td colspan="1">29</td>
		<td colspan="6">28-23</td>
		<td colspan="2">22-21</td>
		<td colspan="16">20-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="1">op</td>
		<td colspan="1">S</td>
		<td colspan="6">100101</td>
		<td colspan="2">hw</td>
		<td colspan="16">imm16</td>
		<td colspan="5">Rd</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4">MOV, MOVN y MOVK IMMEDIATE (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td><td>S</td><td>hw</td>
	</tr>
	<tr>
		<td>MOVN Xd, imm</td><td>0</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>MOV Xd, imm</td><td>1</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>MOVK Xd, imm</td><td>1</td><td>1</td><td>00</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">CBZ y CBNZ (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="6">30-25</td>
		<td colspan="1">24</td>
		<td colspan="19">23-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="1">1</td>
		<td colspan="6">011010</td>
		<td colspan="1">op</td>
		<td colspan="19">imm19</td>
		<td colspan="5">Rt</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="2">CBZ y CBNZ (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td>
	</tr>
	<tr>
		<td>CBZ Xt, my_label</td><td>0</td>
	</tr>
	<tr>
		<td>CBNZ Xt, my_label</td><td>1</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">B.cond (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="6">31-25</td>
		<td colspan="1">24</td>
		<td colspan="19">23-5</td>
		<td colspan="1">4</td>
		<td colspan="5">3-0</td>
	</tr>
	<tr>
		<td colspan="6">0101010</td>
		<td colspan="1">o1</td>
		<td colspan="19">imm19</td>
		<td colspan="1">o0</td>
		<td colspan="5">cond</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> B.cond (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>o0</td><td>o1</td><td>cond</td>
	</tr>
	<tr>
		<td>B.EQ my_label</td><td>0</td><td>0</td><td>0000</td>
	</tr>
	<tr>
		<td>B.NE my_label</td><td>0</td><td>0</td><td>0001</td>
	</tr>
	<tr>
		<td>B.HS my_label</td><td>0</td><td>0</td><td>0010</td>
	</tr>
	<tr>
		<td>B.LO my_label</td><td>0</td><td>0</td><td>0011</td>
	</tr>
	<tr>
		<td>B.MI my_label</td><td>0</td><td>0</td><td>0100</td>
	</tr>
	<tr>
		<td>B.PL my_label</td><td>0</td><td>0</td><td>0101</td>
	</tr>
	<tr>
		<td>B.VS my_label</td><td>0</td><td>0</td><td>0110</td>
	</tr>
	<tr>
		<td>B.VC my_label</td><td>0</td><td>0</td><td>0111</td>
	</tr>
	<tr>
		<td>B.HI my_label</td><td>0</td><td>0</td><td>1000</td>
	</tr>
	<tr>
		<td>B.LS my_label</td><td>0</td><td>0</td><td>1001</td>
	</tr>
	<tr>
		<td>B.GE my_label</td><td>0</td><td>0</td><td>1010</td>
	</tr>
	<tr>
		<td>B.LT my_label</td><td>0</td><td>0</td><td>1011</td>
	</tr>
	<tr>
		<td>B.GT my_label</td><td>0</td><td>0</td><td>1100</td>
	</tr>
	<tr>
		<td>B.LE my_label</td><td>0</td><td>0</td><td>1101</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">B, BL (Codificación General)</th>
	</tr>
	<tr>
		<td colspan="1">31</td>
		<td colspan="5">30-26</td>
		<td colspan="26">25-0</td>
	</tr>
	<tr>
		<td colspan="1">op</td>
		<td colspan="5">00101</td>
		<td colspan="26">imm26</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="2"> B, BL (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>op</td>
	</tr>
	<tr>
		<td>B my_label</td><td>0</td>
	</tr>
	<tr>
		<td>BL my_label</td><td>1</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">LDR y STR(Codificación General)</th>
	</tr>
	<tr>
		<td colspan="2">31-30</td>
		<td colspan="3">29-27</td>
		<td colspan="1">26</td>
		<td colspan="2">25-24</td>
		<td colspan="2">23-22</td>
		<td colspan="12">21-10</td>
		<td colspan="5">9-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="2">size</td>
		<td colspan="3">111</td>
		<td colspan="1">V</td>
		<td colspan="2">01</td>
		<td colspan="2">opc</td>
		<td colspan="12">imm12</td>
		<td colspan="5">Rn</td>
		<td colspan="5">Rt</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> LDR y STR (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>size</td><td>V</td><td>opc</td>
	</tr>
	<tr>
		<td>STR Xt,[Xn,#imm]</td><td>11</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>LDR Xt,[Xn,#imm]</td><td>11</td><td>0</td><td>01</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th>RET (Codificación Ultra Especifica)</th>
	</tr>
	<tr>
		<td>11010110010111110000001111000000</td>
	</tr>
</table>

