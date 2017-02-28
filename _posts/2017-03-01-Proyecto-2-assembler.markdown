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

### Preámbulo:

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
		<td colspan="2">Los siguientes carácteres son instrucciones. Las instrucciones se almacenaran la etiqueta <b>dot_text</b></td>
	</tr>
	<tr>
		<td>.data</td>
		<td colspan="2">Los siguientes carácteres son datos a almacenar. Los datos se almacenaran en la etiqueta <b>dot_data</b></td>
	</tr>
</table>

Las directivas <b>.text</b> y <b>.data</b> especifican secciones de memoria donde se guardaran las instrucciones y los datos de su programa (nosotros les daremos los punteros a estas areas). 
Ademas de esto, cuando codifiquemos los datos, vamos a utilizar la directiva <b>.asciz</b>, que representa una cadena de caracteres que termina el '\0'; esto significa que ustedes deben codificar
esa cadena de caracteres en la seccion <b>dot_data</b> y terminarla con '\0'.

Una vez establecido este subset de instrucciones y las directivas, vamos a hablar un poco de los registros y las banderas para los saltos. 

Los procesadores ARMv8 tienen 31 registros de proposito general. que van desde x0 hasta x30. Sin embargo, el registro x30 se utiliza para guardar la dirección de retorno 
de la función. Otro registro del procesador es XZR; este registro esta alambrado directamente a tierra, asi que su valor es constante e igual a 0. Aparte de eso, existe el registro SP, 
que es un registro aparte, y guarda la dirección del tope del stack.

<table style="text-align:center;">
	<tr>
		<th colspan="3">Registros del procesador</th>
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

Ademas de esto, los procesadores ARMv8 tienen un set de <b>banderas</b>, cada una de 1 bit unicamente. Las instrucciones que terminan en "S" modifican las banderas, y las instrucciones "B."
evaluan las banderas para confirmar si saltan o no. Por ejemplo, si x3 tiene el valor 5 y x8 tiene el valor 6, la operacion SUBS x0,x3,x5 modificara las bandeas de la siguiente forma:

<table style="text-align:center;">
	<tr>
		<th></th><th>Z (Zero)</th><th>N (Negative)</th><th>C (Carry)</th><th>O (Overflow)</th>
	</tr>
	<tr>
		<td>Antes</td><td>1</td><td>0</td><td>1</td><td>1</td>
	</tr>
	<tr>
		<td colspan="5">SUBS x0, x3, x5</td>
	</tr>
	<tr>
		<td>Despues</td><td>0 (no es zero)</td><td>1 (es negativo)</td><td>0 (no carry)</td><td>0 (no overflow)</td>
	</tr>
</table>

Hasta aquí termina el preámbulo. Si desean leer más sobre las directivas, los registros, y codificación de instrucciones aparte de la que les proveemos nosotros, pueden utilizar este 
<a href="https://drive.google.com/file/d/0B5xlmAbvK4yATVZQVkI2amprb28/view">link</a> al manual que también está colocado en el GES. Allí esta todo lo que necesitan para su proyecto y seguramente más.

### El Proyecto:

Pueden descargar los archivos base para este proyecto de GitHub Classroom utilizando este <a href="#">link</a> como en los laboratorios. En el repositorio encontraran el archivo 
<b>ensamblador.s</b>, que contiene un esqueleto para su proyecto. El esqueleto reserva espacio en el heap para codificar hasta 1000 instrucciones en el área de texto y 1000 caracteres en el área de 
data. Dentro de los argumentos que recibe el programa, deben enviar como parámetro el nombre (o path) de un archivo de texto que contendrá las instrucciones en lenguaje ARMv8 que van a codificar.
El programa lee cada linea del archivo, la guarda en un <b>buffer</b> de memoria temporal y la manda como parametro a la función <b>encode</b>, que ustedes deben implementar. La función encode debe leer
la instrucción, codificarla si es necesario, y guardarla en el área que le corresponde. Veamos un ejemplo:

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
ensamblar, una vez para ver todas las etiquetas y codificar el área de data, y una segunda para codificar las instrucciones en sí. Queda a su libertad como y donde implementar la tabla de 
Símbolos, pero deben tomar en cuenta que por cada llamada a <b>malloc</b>, deben hacer una llamada a <b>free</b>.

### Codificación: