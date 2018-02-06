---
layout: post
title:  "Proyecto 1: Desensamblador de RISCV"
date:   2017-02-05
category: proyecto
description: >
    El objetivo de este proyecto es que ustedes puedan reforzar sus habilidades de programación en C aprendidas en clase y en las lecturas de K&amp;R y se familiarice con algunos de los detalles de RISC-V que lo prepararan para el resto del curso.
permalink: /:categories/:title.html
---

### Propósito:

En este proyecto ustedes deben de crear un emulador el cual pueda ejecutar un subconjunto de instruccioens de RISC-V. Ustedes se van a encargar de hacer un programa que decodifique y ejecute varias instrucciones de RISC-V. Considérenlo como una versión miniatura de [VENUS](http://www.kvakil.me/venus/)

Para completar este proyecto , ustedes van a encontrar útil usar el [RISC-V green card](https://www.cl.cam.ac.uk/teaching/1617/ECAD+Arch/files/docs/RISCVGreenCardv8-20151013.pdf)
***

### Getting Started
Antes de comenzar asegúrese que usted **leyó y comprendió** todas las instrucciones del proyecto. 

Para este proyecto ustedes van a necesitar obtener los archivos de **pj-2018**, ingrese al siguiente link de Github Classroom y cree su equipo.
[Github Classroom: Archivos base de proyecto](https://classroom.github.com/g/tHSVtq8v)

Los archivos que ustedes necesitan modificar y enviar son:

* *part1.c*: Este es el archivo que necesita para modificar la parte 1.
* *utils.c*: Este archivo puede contener varias funcioens de ayuda para la parte 1.
* *part2.c*: Este es el archivo que necesita para modificar la parte 2.

**Si ustedes agregan funciones extras, por favor colocarlas en los archivos C correspondientes. Si ustedes no siguen estas recomendaciones, es posible que su código no compile y no obtenga una nota.**	

Usted deberia consultar los siguientes archivos muy detenidamente.
* *type.h*: Archivo C header para los tipos de datos que usted va a utilizar.
* *Makefile*: Este archivo contiene todas las dependencias.
* *riscvcode/\**: Archivos para correr pruebas.
* *utils.h*: Este archivo contiene el formato de las instrucciones a ser utilizadas para la parte 1.

Estos son unos archivos que no es necesario que los revisen:
 * *riscv.h* 
 * *riscv.c*

**Su código va a ser probado en las computadoras del laboratorio, asegúrese de probarlo en estas computadoras antes de enviarlo así esta completamente seguro de su funcionamiento.**
    
### El emulador de RISC-V


Los archivos proporcionados en el kit de inicio son la base para un emulador RISC-V. Primero ustedes deberán agregar código en _part1.c_ y _utils.c_ para imprimir las instrucciones en ensamblador correspondientes al código de máquina (binario). Una vez realizaron esto, ustedes completaran el programa agregando código en el archivo _parte2.c_ para ejecutar cada instrucción (incluyendo los accesos a la memoria). Su simulador debe ser capaz de entender cada una de las instrucciones siguientes ya codificadas en código de maquina (binario), Nosotros ya les damos una tabla de los tipos de instrucciones que deben ser capaz de manejar en su emulador.


**Es muy importante que ustedes lean y entiendan las definiciones encontradas en _types.h_ antes de empezar su proyecto. Si tiene alguna duda, o encuentre algo que no entienda respecto a las mismas consulte el capítulo 6 de K&R.**


El set de instrucciones que su emulador debe soportar esta listado a continuación. Toda la información acá es copiada desde **RISC-V green sheet** como ayuda, adicional puede utilizar la hoja proporcionada anteriormente.


<table>
	<tr>
		<th colspan="7">FORMATO DE UNA INSTRUCCIÓN DE TIPO R </th>
	</tr>
	<tr>
		<td>R-TYPE</td>
		<td><font color="#ff0000">funct7</font></td>
		<td><font color="#0000ff">rs2</font></td>
		<td><font color="#0000ff">rs1</font></td>
		<td><font color="#ff0000">funct3</font></td>
		<td><font color="#0000ff">rd</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>7</td>
		<td>5</td>
		<td>5</td>
		<td>3</td>
		<td>5</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO R (OPCODE 0x33) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> add</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x0</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> mul</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x0</td>
		<td>0x01</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] * <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) [31:0]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> sub</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x0</td>
		<td>0x20</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] - <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> sll</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x1</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] << <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> mulh</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x1</td>
		<td>0x01</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] * <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) [63:32]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> slt</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x2</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] < <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) ? 1 : 0</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> xor</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x4</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] ^ <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> div</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x4</td>
		<td>0x01</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] / <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> srl</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x5</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] >> <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> sra</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x5</td>
		<td>0x20</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] >> <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> or</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x6</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] | <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> rem</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x6</td>
		<td>0x01</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] % <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
	<tr>
		<td> <font color="#ff0000"> and</font><font color="#0000ff"> rd</font>, <font color="#0000ff"> rs1</font>, <font color="#0000ff"> rs2</font></td>
		<td>0x7</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<-<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] & <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
</table>

<table>
	<tr>
		<th colspan="6">FORMATO DE UNA INSTRUCCIÓN DE TIPO I </th>
	</tr>
	<tr>
		<td>I-TYPE</td>
		<td><font color="#ff00ff">imm[11:0]</font></td>
		<td><font color="#0000ff">rs1</font></td>
		<td><font color="#ff0000">funct3</font></td>
		<td><font color="#0000ff">rd</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>12</td>
		<td>5</td>
		<td>3</td>
		<td>5</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO I (OPCODE 0x03) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000"> lb</font><font color="#0000ff"> rd,</font><font color="#ff00ff"> offset</font>(<font color="#0000ff">rs1</font>)</td>	
		<td>0x0</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- SignExt(Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff"> offset</font>, <font color="#00a680">byte</font>)) </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> lh</font><font color="#0000ff"> rd,</font><font color="#ff00ff"> offset</font>(<font color="#0000ff">rs1</font>)</td>	
		<td>0x1</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- SignExt(Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff"> offset</font>, <font color="#00a680">half</font>)) </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> lw</font><font color="#0000ff"> rd,</font><font color="#ff00ff"> offset</font>(<font color="#0000ff">rs1</font>)</td>	
		<td>0x2</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff"> offset</font>, <font color="#00a680">word</font>) </td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO I (OPCODE 0x13) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000"> addi</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x0</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> slli</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x1</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] << <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> slti</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x2</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- (<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] < <font color="#ff00ff"> imm</font>) ? 1 : 0</td>
	</tr>
	<tr>
		<td><font color="#ff0000"> xori</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x4</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] ^ <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> srli</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x5</td>
		<td>0x00</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] >> <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> srai</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x5</td>
		<td>0x20</td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] >> <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> ori</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x6</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] | <font color="#ff00ff"> imm</font> </td>
	</tr>
	<tr>
		<td><font color="#ff0000"> andi</font><font color="#0000ff"> rd,</font><font color="#0000ff"> rs1,</font><font color="#ff00ff"> imm</font></td>	
		<td>0x7</td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] & <font color="#ff00ff"> imm</font> </td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO I (OPCODE 0x73) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
	<td><font color="#ff0000"> ecall</font></td>	
		<td>0x0</td>
		<td>0x000</td>
		<td rowspan="3">(Transfiere el control al Sistema Operativo) <br><font color="#0000ff">a0</font> = <font color="#ff00ff">1</font> imprime el valor contenido en <font color="#0000ff">a1</font> como entero. </br><br> <font color="#0000ff">a0</font> = <font color="#ff00ff"> 10</font>  es exit o un indicador de final de código. <br>
	</td>
		 </tr>
</table>
<table>
	<tr>
		<th colspan="7">FORMATO DE UNA INSTRUCCIÓN DE TIPO S </th>
	</tr>
	<tr>
		<td>S-TYPE</td>
		<td><font color="#ff00ff">imm[11:]</font></td>
		<td><font color="#0000ff">rs2</font></td>
		<td><font color="#0000ff">rs1</font></td>
		<td><font color="#ff0000">funct3</font></td>
		<td><font color="#ff00ff">imm[4:0]</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>7</td>
		<td>5</td>
		<td>5</td>
		<td>3</td>
		<td>5</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO S (OPCODE 0x23) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000">sb</font> <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font>(<font color="#0000ff">rs1</font>)</td>
		<td>0x0</td>
		<td></td>
		<td>Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff">offset</font>)<- <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>][7:0]</td>
	</tr>
	<tr>
		<td><font color="#ff0000">sh</font> <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font>(<font color="#0000ff">rs1</font>)</td>
		<td>0x1</td>
		<td></td>
		<td>Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff">offset</font>)<- <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>][15:0]</td>
	</tr>
	<tr>
		<td><font color="#ff0000">sw</font> <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font>(<font color="#0000ff">rs1</font>)</td>
		<td>0x2</td>
		<td></td>
		<td>Mem(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff">offset</font>)<- <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="9">FORMATO DE UNA INSTRUCCIÓN DE TIPO SB </th>
	</tr>
	<tr>
		<td>SB-TYPE</td>
		<td><font color="#ff00ff">imm[12]</font></td>
		<td><font color="#ff00ff">imm[10:5]</font></td>
		<td><font color="#0000ff">rs2</font></td>
		<td><font color="#0000ff">rs1</font></td>
		<td><font color="#ff0000">funct3</font></td>
		<td><font color="#ff00ff">imm[4:1]</font></td>
		<td><font color="#ff00ff">imm[11]</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>1</td>
		<td>6</td>
		<td>5</td>
		<td>5</td>
		<td>3</td>
		<td>4</td>
		<td>1</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO SB (OPCODE 0x63) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000">beq</font> <font color="#0000ff">rs1</font>, <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font></td>
		<td>0x0</td>
		<td></td>
		<td>if(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] == <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) <br> <font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">offset</font>, 1b'0}</br></td>
	</tr>
	<tr>
		<td><font color="#ff0000">bne</font>  <font color="#0000ff">rs1</font>, <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font></td>
		<td>0x1</td>
		<td></td>
		<td>if(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] != <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) <br> <font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">offset</font>, 1b'0}</br></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4">FORMATO DE UNA INSTRUCCIÓN DE TIPO U </th>
	</tr>
	<tr>
		<td>U-TYPE</td>
		<td><font color="#ff00ff">imm[31:12]</font></td>
		<td><font color="#0000ff">rd</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>20</td>
		<td>5</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO U (OPCODE 0x37) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000">lui</font> <font color="#0000ff">rd</font>, <font color="#ff00ff">offset</font></td>
		<td></td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- {<font color="#ff00ff">offset</font>, 12b'0}</br></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="7">FORMATO DE UNA INSTRUCCIÓN DE TIPO UJ </th>
	</tr>
	<tr>
		<td>UJ-TYPE</td>
		<td><font color="#ff00ff">imm[20]</font></td>
		<td><font color="#ff00ff">imm[10:1]</font></td>
		<td><font color="#ff00ff">imm[11]</font></td>
		<td><font color="#ff00ff">imm[19:12]</font></td>
		<td><font color="#0000ff">rd</font></td>
		<td><font color="#ff0000">opcode</font></td>
	</tr>
	<tr>
		<td>Bits</td>
		<td>1</td>
		<td>10</td>
		<td>1</td>
		<td>8</td>
		<td>5</td>
		<td>7</td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="4"> INTRUCCIONES TIPO UJ (OPCODE 0x6F) </th>
	</tr>
	<tr>
		<td>INSTRUCCIÓN</td>
		<td>FUNCT3</td>
		<td>FUNCT7/IMM</td>
		<td>OPERACIÓN</td>
	</tr>
	<tr>
		<td><font color="#ff0000">jal</font> <font color="#0000ff">rd</font>, <font color="#ff00ff">imm</font></td>
		<td></td>
		<td></td>
		<td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">PC</font> + <font color="#00ff00">4</font> <br><font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">imm</font>, 1b'0}</br></td>
	</tr>
</table>

Al igual que la arquitectura RISC-V normal, el sistema RISC-V que está implementando es little-endian. Esto significa que cuando se le da un valor compuesto de múltiples bytes, el byte menos significativo se almacena en la dirección más baja. Consulte la página B-43 de P & H (4ª edición) para obtener información sobre endianness.

### Framework Code

El código base que les fue proporcionado funciona de la siguiente manera:


1.  Lee los programas en código de máquina que se encuentran en la memoria (Empezando en la dirección 0x01000). Para "ejecutar" el programa este es pasado como un parámetro en la línea de comandos. Cada programa tiene 1 MiB de memoria y la unidad mínima de direccionamiento son los bytes.
2. Todos los registros de RISC-V son inicializados en 0 y el program counter (PC) hacia la dirección 0x01000. Las únicas excepciones a las inicializaciones son el stack pointer (está en 0xEFFFF) y el global pointer (está en 0x03000). En el contexto de su emulador, el global pointer esta referenciado a la parte estática de su memoria. Los registros y el program counter son manejados por el _Processor struct_ definido en _types.h_.
3. Se definieron banderas con las cuales puede manejar la interacción con el usuario. Dependiendo de la opción especificada en la linea de comandos, el simulador mostrará un dissassembly dump (-d) o se ejecutará el programa. Más información sobre las opciones de linea de comandos más adelante. 

Lo que prosigue es que entra al flujo de simulación principal, el cual ejecuta una única instrucción repetitivamente hasta que la simulación se completa. La ejecución de una instrucción realiza las siguientes tareas:

1. Fetch de una instrucción desde la memoria, usando el PC como dirección.
2. Examina el opcode/funct3 para determinar que instrucción es.
3. Ejecuta la instrucción y actualiza el PC.

#### El simulador soporta las siguientes opciones en la línea de comandos.


* _-i_ corre el simulador en modo interactivo, es decir que se ejecutará una instrucción a la vez al presionar Enter. Cada instrucción es mostrada en su forma desensamblada.
* _-t_ corre el simulador en modo rastreo, en donde cada instrucción es ejecutada y es mostrada al usuario.
* _-r_ indica al simulador que imprima el contenido de los 32 registros después de que es ejecutada cada instrucción. Esta opción es más útil cuando se combina con la opción _-i_.
* _-d_ indica al simulador que desensamble el programa completo y que termine sin ejecutarlo.


En la parte 2, ustedes deberán implementar los siguientes métodos:

* El _execute_instruction()_
* Los diferentes _executes_
* El _store()_
* El _load()_


Para cuando ustedes hayan termina la implementación de todos los métodos, el simulador será capaz de manejar todas las instrucciones de la tabla anterior.


## Parte 1

**Su primera tarea es implementar un desensamblador al completar el método _decode_instruction() en el archivo _part1.c_ junto a otras funciones.**

El objetivo de esta parte, dada una instrucción en código de máquina ustedes deberán traducirla a su instrucción en lenguaje ensamblador RISC-V (e.g. `add x1, x2, x3` ).  Para esta parte, ustedes no harán referencia a los registros por nombre sino por su número (como esta definido en **RISC-V Green Card**).  Cuando Imprima las instrucciones revise las constantes definidas en _util.h_ ya que estas le pueden ser de ayuda. Más detalles sobre los requisitos a continuación.

1. Imprime el nombre de la instrucción. Si la instrucción tiene argumentos, imprima un tab (\t).
2. Imprime todos los argumentos, en el siguiente orden y formato dado en la columna de **INSTRUCCIÓN** de la tabla anterior.
	*	Los argumentos son generalmente separados por coma (`lw`/`sw`), usan también paréntesis), pero no están separados por espacios.
	*	Ustedes encontraran de ayuda revisar el archivo _utils.h_.
	*	Los registros que funcionan como argumentos son impresos con una `x` seguido del número de registro, en decimal. (e.g. `x0` o `x31`)
	*	Todos los inmediatos deben mostrarse como un número decimal con signo.
	*	Los corrimientos (e.g. para `sll`) se imprimen como números decimales sin signo (e.g. 0 a 31).
3. Imprime un salto de línea (\n) al final de cada instrucción.
4. Se estará utilizando un autograder para calificar esta tarea. Si su output difiere del nuestro debido a errores de formato, no recibirá crédito.
5. Nosotros les proveemos ciertas pruebas. Sin embargo, dado que estas pruebas solo cubren un subconjunto de todos los escenarios posibles, aprobar estas pruebas no significa que su código esté libre de errores. Ustedes deberán identificar todos los casos y probarlos.

Para implementar la funcionalidad, deben de completar lo siguiente:

* La función _decode_instrucction()_ en _part1.c_
* Los diferentes _writes_ en _part1.c_
* Los diferentes _prints_ en _part1.c_
* Los diferentes _gets_ en _utils.c_
* La función _bitSigner_ en _utils.c_

Ustedes deben de correr el test brindado para su proyecto escribiendo el siguiente comando. Si ustedes pasan el test, verán en su consola el siguiente output.

```shell
$ make part1
gcc -g -Wall -Werror -Wfatal-errors -O2 -o riscv utils.c part1.c part2.c riscv.c
simple_disasm TEST PASSED!
multiply_disasm TEST PASSED!
random_disasm TEST PASSED!
---------Disassembly Tests Complete---------
```

### Testing
Los test que se les dieron no evalúan todas las posibilidades, por ello ustedes pueden crear sus propios archivos de prueba para comprobar su funcionamiento. Si ustedes desean correr un test en específico, pueden usar el siguiente comando para ello

```
make [test_name]_disasm
```

Para crear sus propios archivos de prueba, primero necesitarán crear código de máquina. Para ello pueden ayudarse de Venus o hacerlo a mano. Ustedes deben de poner las instrucciones en código de máquina en un archivo llamado `[test_name].input`
y colocar el archivo dentro de la carpeta `riscvcode/code`. Después, deben crear el archivo `[test_name].solution` el cual contendrá las instrucciones que se espera obtener; y colocar el archivo en la carpeta `riscvcode/ref`. Vean las pruebas proporcionadas como ejemplos de este tipo de archivos. Para integrar sus pruebas en el comando `make`, ustedes deben de modificar el archivo `Makefile`. En la línea 4 del archivo `Makefile`, donde dice `ASM_TESTS`, agregar `[test_name]` a la lista con espacios entre cada nombre de archivo.:

```
SOURCES := utils.c part1.c part2.c riscv.c
HEADERS := types.h utils.h riscv.h

ASM_TESTS := simple multiply random test_name
```

Si su instrucción desensamblada no es igual a la espera, ustedes obtendrán la diferencia entre el output esperado y el output que devolvieron. **Asegúrese de al menos pasar esta prueba antes de enviar part1.c**

```shell
#Output Esperado
< 00001014: lui	x8, 1048575
---
#Output Devuelto
> 00001014: Invalid Instruction: 0xfffff437
```
**Para la primera parte, solo debe modificar los archivos _part1.c_ y _utils.c_**
