---
layout: post
title:  "Proyecto 2: ArmV8 Assembler"
date:   2017-03-01
category: proyecto
description: >
    El objetivo de este proyecto es que ustedes desarrollen su habilidad trabajando en lenguaje ensamblador, y que logren entender como se codifica el set de instrucciónes, en este caso ARMv8 
    a un formato que su computadora puede entender y ejecutar.
permalink: /:categories/:title.html
---

### Preámbulo:

El set de instrucciónes ARMv8 es muy vasto (incluso tomando en cuenta que es una arquitectura RISC), y no nos daría tiempo de codificar todas las instrucciónes en estas dos semanas, así que lo
primero que tenemos que hacer es escoger un subset de instrucciónes sobre las que vamos a trabajar. Para este proyecto, las instrucciónes que deberán codificar serán las siguientes:

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
	<tr>
		<td>LDRB</td>
		<td>LDRB wt,[xn,imm]</td>
		<td>Carga en wt el byte menos significativo de la dirección xn con offset imm</td>
	</tr>
	<tr>
		<td>STRB</td>
		<td>STRB wt,[xn,imm]</td>
		<td>Guarda el byte menos significativo de wt en la dirección xn con offset imm </td>
	</tr>
	<tr>
		<td>RET</td>
		<td>RET</td>
		<td>Salta a la dirección especificada en x30</td>
	</tr>
	<tr>
		<th colspan="3">Directivas a tomar en cuenta</th>
	</tr>
	<tr>
		<td>.text</td>
		<td colspan="2">Los siguientes carácteres son instrucciónes. Las instrucciónes se almacenaran la etiqueta <b>dot_text</b></td>
	</tr>
	<tr>
		<td>.data</td>
		<td colspan="2">La siguiente informacion son datos a almacenar en la etiqueta <b>dot_data</b></td>
	</tr>
	<tr>
		<td>.asciz "STR"</td>
		<td colspan="2">Hay que guardar los carácteres en la etiqueta <b>dot_data</b>, deben agregar un '\0' al final</td>
	</tr>
	<tr>
		<td>.space #NUM</td>
		<td colspan="2">Hay que reservar espacio igual a la cantidad especificada en imm en la etiqueta <b>dot_data</b></td>
	</tr>
</table>

Las directivas <b>.text</b> y <b>.data</b> especifican secciones de memoria donde se guardaran las instrucciónes y los datos de su programa (nosotros les daremos los punteros a estas areas). 
Ademas de esto, cuando codifiquemos los datos, vamos a utilizar la directiva <b>.asciz</b>, o la directiva <b>.space</b>. Tomen en cuenta que para la directiva <b>.asciz</b>, ustedes deben  
terminar la cadena con '\0'.

Una vez establecido este subset de instrucciónes y las directivas, vamos a hablar un poco de los registros y las banderas para los saltos. 

Los procesadores ARMv8 tienen 31 registros de proposito general. que van desde x0 hasta x30. Sin embargo, el registro x30 se utiliza para guardar la dirección de retorno 
de la función. Otro registro del procesador es XZR; este registro esta alambrado directamente a tierra, asi que su valor es constante e igual a 0. Aparte de eso, existe el registro SP, 
que es un registro aparte, y guarda la dirección del tope del stack.

<table style="text-align:center;">
	<tr>
		<th colspan="8">Registros del procesador</th>
	</tr>
	<tr>
		<td>x0</td><td>x1</td><td>x2</td><td>x3</td><td>x4</td><td>x5</td><td>x6</td><td>x7</td>
	</tr>
	<tr>
		<td>x8</td><td>x9</td><td>x10</td><td>11</td><td>x12</td><td>x13</td><td>x14</td><td>x15</td>
	</tr>
	<tr>
		<td>x16</td><td>x17</td><td>x18</td><td>x19</td><td>x20</td><td>x21</td><td>x22</td><td>x23</td>
	</tr>
	<tr>
		<td>x24</td><td>x25</td><td>x26</td><td>x27</td><td>x28</td><td>x29</td><td>x30</td><td> </td>
	</tr>
	<tr>
		<td colspan="4">XZR</td><td colspan="4">SP</td>
	</tr>
</table>

Ademas de esto, los procesadores ARMv8 tienen un set de <b>banderas</b>, cada una de 1 bit unicamente. Las instrucciónes que terminan en "S" modifican las banderas, y las instrucciónes "B."
evaluan las banderas para confirmar si saltan o no. Por ejemplo, si x3 tiene el valor 5 y x8 tiene el valor 6, la operacion SUBS x0,x3,x5 modificara las bandeas de la siguiente forma:

<table style="text-align:center;">
	<tr>
		<th></th><th>Z (Zero)</th><th>N (Negative)</th><th>C (Carry)</th><th>O (Overflow)</th>
	</tr>
	<tr>
		<td>Antes</td><td>1</td><td>0</td><td>1</td><td>1</td>
	</tr>
	<tr>
		<td colspan="5" style="text-align:left">
			&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; MOV x3, #5 <br>
			&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; MOV x8, #6 <br>
			&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SUBS x0, x3, x8
		</td>
	</tr>
	<tr>
		<td>Después</td><td>0 (no es zero)</td><td>1 (es negativo)</td><td>0 (no carry)</td><td>0 (no overflow)</td>
	</tr>
</table>

Hasta aquí termina el preámbulo. Si desean leer más sobre las directivas, los registros, y codificación de instrucciónes aparte de la que les proveemos nosotros, pueden utilizar este 
<a href="https://drive.google.com/file/d/0B5xlmAbvK4yATVZQVkI2amprb28/view">link</a> al manual que también está colocado en el GES. Allí esta todo lo que necesitan para su proyecto y seguramente más.

### El Proyecto:

Pueden clonar acceder a los archivos base desde <b>Github Classroom</b> haciendo click en este 
<a href="https://classroom.github.com/group-assignment-invitations/6a109f71a1552bb9931d1b3dff52f4c9">link</a>.
Tomen en cuenta que un estudiante debe crear el grupo y otro debe unirse a este. La cantidad maxima de estudiantes por grupo es dos.


En el repositorio encontraran el archivo 
<b>ensamblador.s</b>, que contiene un esqueleto para su proyecto. El esqueleto reserva espacio en el heap para codificar hasta 1000 instrucciónes en el área de texto y 1000 caracteres en el área de 
data. Dentro de los argumentos que recibe el programa, deben enviar como parámetro el nombre (o path) de un archivo de texto que contendrá las instrucciónes en lenguaje ARMv8 que van a codificar.
El programa lee todas las lineas del archivo, la guarda en un <b>buffer</b> de memoria temporal y la manda como parametro a la función <b>encode</b>, que ustedes deben implementar. 
La función encode debe leer las instrucciónes, codificarla, y guardarla en el área que le corresponde. Veamos un ejemplo:

```shell
.text
   ADD x3, x5, x17
.data
   mensaje:   .asciz "Hello World from ARMv8..."
```

La primer llamada a <b>encode</b> debe recibir la primer linea: <i>.text</i> y concluir <i>esta linea indica que lo siguiente que viene es una instrucción</i>. Al leer la segunda linea: 
<i>ADD x3, x5, x17</i>, deberá codificar la instrucción con el formato que especificaremos mas abajo, y guardarla en el área de texto. Al leer la tercer linea <i>.data</i>, su programa deberá 
entender que la siguiente linea que va a leer la debe colocar en el área de data, y al leer la cuarta instrucción: <i>mensaje: .asciz "Hello World from ARMv8"</i>, su programa debe ir guardando 
cada carácter en el área de data, y terminar escribiendo el carácter '\0' al final. Tomen en cuenta que por cada instrucción codificada y carácter ingresado al área de texto y data, 
ustedes deben ver como avanzan el puntero hacia la siguiente posición sin perder la referencia a la posición inicial. 

### Tabla de Símbolos:

Para poder codificar los saltos y las direcciones de memoria correctamente, ustedes deben crear una tabla de símbolos. La tabla de símbolos resuelve el siguiente problema:

```shell
.data
   mensaje:   .asciz "Hello World from ARMv8..."
.text
   LDR x19,=mensaje
```

Para codificar la etiqueta mensaje y colocarla en el área de data no tenemos ningún problema, pero ¿Qué pasa cuando queremos cargar la dirección de esta etiqueta en x19? No tenemos ninguna 
referencia a donde en toda la sección de data empieza el mensaje. Probemos ahora manteniendo la tabla de símbolos:

<table style="text-align:center;">
	<tr>
		<th>Etiqueta</th>
		<th>Direccion</th>
	</tr>
	<tr>
		<td>mensaje</td>
		<td>0x0000000040008000</td>
	</tr>
</table>

Ya podemos codificar nuestra instrucción LDR porque sabemos en que dirección empieza el mensaje. Pero, ¿En donde termina? Es por esto que agregamos un '\0' al final de la cadena de caracteres,
para denotar el EOS (End of String). Para implementar la tabla de símbolos correctamente, seguramente ustedes tendrán que recorrer más de una vez todas las lineas de código del archivo a 
ensamblar, una vez para ver todas las etiquetas y codificar el área de data, y una segunda para codificar las instrucciónes en sí. Queda a su libertad como y donde implementar la tabla de 
Símbolos, pero deben tomar en cuenta que por cada llamada a <b>malloc</b>, deben hacer una llamada a <b>free</b>.

### Codificación:

Finalmente hemos llegado al proceso de codificacion de las instrucciónes. Si han llegado hasta esta parte sin al menos ojear la informacion de arriba, podria haber un ligero problema de comunicacion.
De cualquier forma, prosigamos con el formato de las instrucciónes codificadas.

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
		<td>B.TL my_label</td><td>0</td><td>0</td><td>1011</td>
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
		<th colspan="32">LDR label (Codificación Especifica)</th>
	</tr>
	<tr>
		<td colspan="8">31-24</td>
		<td colspan="19">23-5</td>
		<td colspan="5">4-0</td>
	</tr>
	<tr>
		<td colspan="8">01011000</td>
		<td colspan="19">imm19</td>
		<td colspan="5">Rt</td>
	</tr>
</table>

<br>
<br>

<table style="text-align: center;">
	<tr>
		<th colspan="32">LDR, STR, LDRB y STRB (Codificación General)</th>
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
		<th colspan="4"> LDR, STR, LDRB y STRB (Codificación Especifica)</th>
	</tr>
	<tr>
		<td>Instrucción</td><td>size</td><td>V</td><td>opc</td>
	</tr>
	<tr>
		<td>STRB Wt,[Xn,#imm]</td><td>00</td><td>0</td><td>00</td>
	</tr>
	<tr>
		<td>LDRB Wt,[Xn,#imm]</td><td>00</td><td>0</td><td>01</td>
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

### Timeline Sugerida:

La tradición en todos los proyectos es empezar el fin de semana antes de la entrega, pero para este proyecto no podrán hacer esto. Tienen la libertad de realizar el proyecto en el orden que 
quieran, pero este es el orden que nosotros les sugerimos que sigan para realizar el proyecto:

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
			1 de Marzo - 3 de Marzo
		</td>
		<td>
			Leer las Instrucciones
		</td>
	</tr>
</table>



### Indicaciones Adicionales:

En las instrucciones a codificar, nosotros solo enviaremos instrucciones en mayúscula, etiquetas en minúscula, registros en minúscula (<i>x</i> o <i>w</i>) y números en formato decimal 
precedidos por el caracter <i>#</i>(aunque no es difícil darle soporte a números en formato hex y binario). Siempre existirá la coma cuando sea necesario, pero puede haber N cantidad de espacios 
y tabs entre los caracteres de la Instrucción, así que será su trabajo ignorarlos. Tomando esto en cuenta, todas las instrucciones serán instrucciones validas escritas correctamente.

Ustedes pueden ensamblar sus instrucciones y leerlas con <b>readelf</b> como vieron en clase, para ver si su codificación es correcta, pero deben tomar en cuenta que readelf muestra las direcciones
bajas a la izquierda y altas a la derecha, y que el procesador utiliza <b>little endian</b> para la codificación.

Una herramienta extra que pueden utilizar, además del manual y Google, es <a href="https://www.onlinedisassembler.com/static/home/">esta</a> pagina, donde pueden desensamblar instrucciones en 
ARMv8 (AARCH64).

Al momento de codificar los branches (saltos), no importa si son condicionales o incondicionales, siempre son relativos, lo que significa que, si el branch dice que se debe saltar a una etiqueta
especificada 5 instrucciones adelante, el valor inmediato que ustedes codificaran es el número <b>5</b>, lo la dirección exacta de esa etiqueta.

Las especificaciones del proyecto son largas, pero el proyecto en si es más largo. Empiecen desde ya para poder terminar a tiempo. Si no empiezan a trabajar hasta el fin de semana antes de la entrega, 
no podrán conseguir mucho más que un segmentation fault en la línea 680.

### Entrega:

Para la entrega del proyecto, ustedes deben mandar un correo a <i>efrainh12@galileo.edu</i> especificando los integrantes del grupo (máximo dos) y su sección. Deben trabajar en el repositorio de 
GitHub Classroom que les asignamos y deben subir el link del repositorio al GES antes de la fecha de entrega. Si no cumplen con estos requisitos, tendrán una nota de 0 en el proyecto.