# Proyecto 1: C y RISC-V

## Objetivos

* Mejorar sus habilidades de programación en C.
* Conocer algunos de los detalles de RISC-V.
* Prepararse para lo que viene más adelante en el curso.

## Requisitos de Conocimiento

Para realizar este proyecto ustedes tienen que tener claros algunos conceptos, de lo contrario será bastante difícil e incómodo empezar a trabajar. Les recomendamos que antes de empezar estén totalmente seguros que dominan al 100% los siguientes puntos:

* Operaciones binarias en C (`xor`, `or`, `and`, etc).
* Operaciones aritméticas con signo y sin signo en C.
* Type casting en C.
* Control de flujo en C (`switch`, `if`, etc).
* Funciones en C.
* Entender qué son las estructuras (`struct`) en C.
* Entender cómo funcionan las uniones (`union`) en C.
* Uso correcto de `printf`.
* Entender la estructura del set de instrucciones de RISC-V.
* Programar en lenguaje ensamblador RISC-V.

Si alguno de estos temas ustedes creen que no lo tienen claro al 100%, por favor no duden en ir a consultar los libros y material correspondiente del curso, por ejemplo **K&amp;R** es indispensable. En [Lecturas Recomendadas](#lecturas-recomendadas) pueden encontrar algunas lecturas que tocan los puntos antes mencionados y otras cosas que les pueden servir también, nunca está demás tener un poco más de información.

## Lecturas Recomendadas

![RISCV Book](/img/RVB.jpg)
![KR](/img/KR.jpg)
![PH](/img/PH.jpg)

* Guía Práctica de RISC-V: 2
* K&amp;R: 6
* P&amp;H: B-43


## Introducción

En este proyecto ustedes deben de crear un emulador el cual pueda ejecutar un subconjunto de instrucciones de **RISC-V**. Ustedes se van a encargar de hacer un programa que decodifique y ejecute varias instrucciones de RISC-V. Considérenlo como una versión miniatura de [V-Sim](https://www.riscvsim.com).


## RISC-V Green Card

Aquí hay dos **RISC-V Green Cards** que pueden consultar y así tener más herramientras que les pueden ayudar a completar el proyecto, la primera tiene información acerca de los _opcodes_ y otros campos de cada uno de los diferentes formatos de instrucción, por lo que esta sería su mejor opción.

<p align="center">
  <a href="http://inst.eecs.berkeley.edu/~cs61c/fa17/img/riscvcard.pdf" target="_blank"><img src="/img/berkeleyGC.png" alt="Berkeley Green Card" /></a>
  <a href="https://www.cl.cam.ac.uk/teaching/1617/ECAD+Arch/files/docs/RISCVGreenCardv8-20151013.pdf" target="_blank"><img src="/img/cambridgeGC.png" alt="Cambridge Green Card" /></a>
</p>


## Preparación

**Antes de comenzar asegúrense de que hayan <span style="color: red">leído y comprendido</span> todas las instrucciones del proyecto de principio a fin**. Si tienen alguna pregunta pueden consultar la sección de preguntas frecuentes para ver si ya ha sido resuelta, de lo contrario por favor diríjanse a **Slack** y pregunten en los canales correspondientes.

Para comenzar con el proyecto primero tienen que tener todos los archivos base, estos se encuentran [aquí](#). Tienen permitido trabajar en parejas o de forma individual, por lo que al aceptar la asignación les preguntará si desean crear un grupo nuevo o unirse a uno ya existente. Si crean un grupo nuevo, ingresen un nombre que represente al grupo y que no esté ya en los grupos existentes.

![Create group](/img/projs/proj01/classroom1.png)

Si desean unirse a un grupo ya creado, tienen que buscar el nombre del grupo y pulsar el botón que dice **join**

![Join group](/img/projs/proj01/classroom2.png)

**Tienen que tener mucho cuidado al unirse a un grupo ya existente, ya que esto no se puede cambiar después, además lo consideraremos como <span style="color: red">PLAGIO</span>, ya que al hacer esto pueden tener acceso al repositorio del otro miembro del grupo.**

Ya sea que se unan o creen un nuevo grupo al finalizar el proceso les creará automáticamente un repositorio con una extensión que termina con su nombre de grupo. Ya habiendo hecho todo eso, pueden ejecutar los siguientes comandos abriendo una terminal (<kbd >CTRL</kbd> <kbd>+</kbd> <kbd>T</kbd>):

```shell
git clone <link del repositorio>
```

> **NOTA**: Tienen que reemplazar <link del repositorio\> con el link del repositorio que se creó.


## Estructura del Proyecto

Cuando hayan clonado el repositorio, se van a encontrar con los siguientes archivos:

```shell
Makefile
part1.c  
part2.c  
README.md  
riscv.c  
riscvcode/
riscv.h  
submit  
types.h  
utils.c  
utils.h
```

Los únicos archivos que pueden modificar son:

* `part1.c`: Este es el archivo que van a modificar en la parte 1 del proyecto.
* `utils.c`: Archivo auxiliar que contendrá varias funciones de ayuda para la parte 1 y 2 del proyecto.
* `part2.c`: Este es el archivo que van a modificar en la parte 2 del proyecto.


**Ustedes <span style="color: red">NO</span> pueden crear otros archivos ni crear archivos de cabecera `.h`. Si necesitan agregar funciones de ayuda, por favor colóquenlas en los archivos C correspondientes (`utils.c`, `part1.c`, `part2.c`). Si ustedes no siguen estas recomendaciones, su código no va a compilar en el autograder y obtendrán 0 como nota**.


Otros archivos que necesitan consultar detenidamente para entender el proyecto:

* `type.h`: Archivo de cabecera que tiene los tipos de datos que ustedes van a utilizar.
* `Makefile`: Para compilar y probar su código.
* `riscvcode/*`: Archivos para hacer algunas pruebas.
* `utils.h`: Archivo que contiene el formato de las instrucciones a ser utilizadas en la parte 1 del proyecto.


Archivos que no es necesario que los revisen, pero si son curiosos:

 * `riscv.h`: tiene declaraciones de funciones que se utilizan en la parte 1 y 2 del proyecto.
 * `riscv.c`: programa encargado de probar la parte 1 y 2 del proyecto, el simulador como tal.


## El emulador de RISC-V

Los archivos proporcionados en el repositorio que crearon con GitHub Classroom son la base para un emulador de RISC-V. Primero ustedes deberán agregar código en **_part1.c_** y **_utils.c_** para imprimir las instrucciones en ensamblador correspondientes al código de máquina (binario). Una vez realizaron esto, ustedes completarán el programa agregando código en el archivo **_parte2.c_** para ejecutar cada instrucción (incluyendo los accesos a memoria). Su simulador debe de ser capaz de entender cada una de las instrucciones siguientes ya codificadas en código de máquina (binario), nosotros ya les damos una tabla de los tipos de instrucciones que debe de ser capaz de manejar su emulador.

**Es muy <span style="color: red">IMPORTANTE</span> que ustedes lean y entiendan las definiciones encontradas en _types.h_ antes de empezar su proyecto. Si tiene alguna duda, o encuentran algo que no entiendan respecto a las mismas consulten el capítulo 6 de K&R, que habla sobre estructuras, bitfields y uniones**.


### Set de Instrucciones

El set de instrucciones que su emulador debe soportar esta listado a continuación. Toda la información acá es copiada desde [RISC-V green card](http://inst.eecs.berkeley.edu/~cs61c/fa17/img/riscvcard.pdf), como ayuda adicional pueden utilizar la hoja proporcionada anteriormente.


#### Tipo R

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

#### Tipo I
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
    <th colspan="4"> INTRUCCIONES TIPO I (OPCODE 0x67) </th>
  </tr>
  <tr>
    <td>INSTRUCCIÓN</td>
    <td>FUNCT3</td>
    <td>FUNCT7/IMM</td>
    <td>OPERACIÓN</td>
  </tr>
  <tr>
  <td><font color="#ff0000"> jalr</font></td>
    <td>0x0</td>
    <td></td>
    <td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">PC</font> + <font color="#00ff00">4</font> <br><font color="#ff0000">PC</font><- <font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] + <font color="#ff00ff">imm</font></td>
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
    <td rowspan="3">(Transfiere el control al Sistema Operativo) <br><font color="#0000ff">a0</font> = <font color="#ff00ff">1</font> imprime el valor contenido en <font color="#0000ff">a1</font> como entero. <br><font color="#0000ff">a0</font> = <font color="#ff00ff"> 10</font>  es exit o un indicador de final de código.<br>
  </td>
     </tr>
</table>

#### Tipo S
<table>
  <tr>
    <th colspan="7">FORMATO DE UNA INSTRUCCIÓN DE TIPO S </th>
  </tr>
  <tr>
    <td>S-TYPE</td>
    <td><font color="#ff00ff">imm[11:5]</font></td>
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

#### Tipo SB
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
    <td>if(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] == <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) <br> <font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">offset</font>, 1b'0}</td>
  </tr>
  <tr>
    <td><font color="#ff0000">bne</font>  <font color="#0000ff">rs1</font>, <font color="#0000ff">rs2</font>, <font color="#ff00ff">offset</font></td>
    <td>0x1</td>
    <td></td>
    <td>if(<font color="#ff0000">R</font>[<font color="#0000ff">rs1</font>] != <font color="#ff0000">R</font>[<font color="#0000ff">rs2</font>]) <br> <font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">offset</font>, 1b'0}</td>
  </tr>
</table>

#### Tipo U
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
    <th colspan="4"> INTRUCCIONES TIPO U (OPCODE 0x17) </th>
  </tr>
  <tr>
    <td>INSTRUCCIÓN</td>
    <td>FUNCT3</td>
    <td>FUNCT7/IMM</td>
    <td>OPERACIÓN</td>
  </tr>
  <tr>
    <td><font color="#ff0000">auipc</font> <font color="#0000ff">rd</font>, <font color="#ff00ff">offset</font></td>
    <td></td>
    <td></td>
    <td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">PC</font> + {<font color="#ff00ff">offset</font>, 12b'0}
  </td>
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
    <td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- {<font color="#ff00ff">offset</font>, 12b'0}
  </td>
  </tr>
</table>

#### Tipo UJ
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
    <td><font color="#ff0000">R</font>[<font color="#0000ff">rd</font>]<- <font color="#ff0000">PC</font> + <font color="#00ff00">4</font> <br><font color="#ff0000">PC</font><- <font color="#ff0000">PC</font> + {<font color="#ff00ff">imm</font>, 1b'0}</td>
  </tr>
</table>

Al igual que la arquitectura RISC-V normal, el sistema RISC-V que están implementando es little-endian. Esto significa que cuando se le da un valor compuesto de múltiples bytes, el byte menos significativo se almacena en la dirección más baja. Consulten la página **B-43** de **P&amp;H** (4ª edición) para obtener información sobre endianness.

### Estructura del Código

El código base que les fue proporcionado funciona de la siguiente manera:

1.  Lee los programas en código de máquina que se encuentran en la memoria (Empezando en la dirección `0x01000`). Para "ejecutar" el programa este es pasado como un parámetro en la línea de comandos. Cada programa tiene 1 MiB de memoria y la unidad mínima de direccionamiento son los bytes.
2. Todos los registros de RISC-V son inicializados en 0 y el program counter (`pc`) hacia la dirección `0x01000`. Las únicas excepciones a las inicializaciones antes mencionadas son el stack pointer (`sp`) que tiene un valor inicial de `0xEFFFF` y el global pointer (`gp`) que tiene un valor inicial de `0x03000`. En el contexto de su emulador, el global pointer hace referencia a la sección estática de su memoria. Los registros y el program counter están definidos en el **_Processor struct_** definido en **_types.h_**.
3. Se definieron banderas con las cuales puede manejar la interacción con el usuario. Dependiendo de la opción especificada en la línea de comandos, el simulador mostrará un _dissassembly dump_ (`-d`) o se ejecutará el programa. Habrá más información sobre las opciones de línea de comandos más adelante.

Lo que prosigue es que entra al flujo de simulación principal, el cual ejecuta una única instrucción repetitivamente hasta que la simulación se completa. La ejecución de una instrucción realiza las siguientes tareas:

1. Trae una instrucción desde la memoria, usando el `pc` como dirección (_fetch_).
2. Examina el opcode/funct3 para determinar que instrucción es (_decode_).
3. Ejecuta la instrucción y actualiza el `pc` (_execute_).

### Opciones en la línea de comandos

* `-i`: Corre el simulador en modo interactivo (_interactive_), es decir que se ejecutará una instrucción a la vez al presionar <kbd>enter</kbd>. Cada instrucción es mostrada en su forma desensamblada.
* `-t`: Corre el simulador en modo rastreo (_trace_), en donde cada instrucción es ejecutada y es mostrada al usuario.
* `-r`: Indica al simulador que imprima el contenido de los 32 registros después de que es ejecutada cada instrucción. Esta opción es más útil cuando se combina con la opción `-i`.
* `-d`: Indica al simulador que desensamble el programa completo y que termine sin ejecutarlo.

En la parte 2, ustedes deberán implementar los siguientes métodos:

* El **_execute_instruction()_**.
* Los diferentes **_executes_**.
* El **_store()_**.
* El **_load()_**.

Para cuando ustedes hayan terminado la implementación de todos los métodos, el simulador será capaz de manejar todas las instrucciones de la tabla anterior.

## Parte 1

Su primera tarea es implementar un desensamblador al completar el método **_decode_instruction()_** en el archivo **_part1.c_** junto a otras funciones.

El objetivo de esta parte, es que dada una instrucción en código de máquina ustedes deberán traducirla a su instrucción en lenguaje ensamblador RISC-V (e.g. `add x1, x2, x3` ). Para esta parte, ustedes no harán referencia a los registros por nombre sino por su número (como está definido en **RISC-V Green Card**). Cuando impriman las instrucciones revisen las constantes definidas en **_utils.h_** ya que estas le pueden ser de ayuda. Más detalles sobre los requisitos a continuación.

### Requisitos Parte 1

1. Imprimir el nombre de la instrucción. Si la instrucción tiene argumentos, impriman un tab (`\t`).
2. Imprimir todos los argumentos, siguiendo el orden y formato dado en la columna de **INSTRUCCIÓN** de las tablas mostradas anteriormente.
    * Los argumentos son generalmente separados por coma (`lw`/`sw`, usan también paréntesis), pero no están separados por espacios.
    * Ustedes encontrarán de ayuda revisar el archivo **_utils.h_**.
    * Los registros que son argumentos de la instrucción son impresos con una `x` seguido del número de registro, en decimal. (e.g. `x0` o `x31`)
    * Todos los inmediatos deben mostrarse como un número decimal con signo.
    * Los corrimientos (e.g. para `slli`) se imprimen como números decimales sin signo (e.g. 0 a 31).
3. Imprimir un salto de línea (`\n`) al final de cada instrucción.
4. Se estará utilizando un autograder para calificar esta tarea. Si su output difiere del nuestro debido a errores de formato, no obtendrán nota.
5. Nosotros les proveemos ciertas pruebas. Sin embargo, dado que estas pruebas solo cubren un subconjunto de todos los escenarios posibles, pasar estas pruebas no significa que su código esté libre de errores. Ustedes deberán identificar todos los casos y probarlos.

Para completar la funcionalidad de la parte 1, deben de completar lo siguiente:

* La función **_decode_instrucction()_** en **_part1.c_**.
* Los diferentes **_writes_** en **_part1.c_**.
* Los diferentes **_prints_** en **_part1.c_**.
* Los diferentes **_gets_** en **_utils.c_**.
* La función **_bitSigner_** en **_utils.c_**.

Ustedes deben de correr el test brindado para su proyecto escribiendo el siguiente comando. Si ustedes pasan el test, verán en su consola el siguiente output.

```shell
make part1
gcc -g -Wall -Werror -Wfatal-errors -O2 -o riscv utils.c part1.c part2.c riscv.c
simple_disasm TEST PASSED!
multiply_disasm TEST PASSED!
random_disasm TEST PASSED!
---------Disassembly Tests Complete---------
```

### Probando la Parte 1

Los tests que se les dieron no evalúan todas las posibilidades, por eso mismo ustedes pueden (**deben**) crear sus propios archivos de prueba para comprobar su funcionamiento. Si ustedes desean correr un test en específico, pueden usar el siguiente comando para ello:

```
make [test_name]_disasm
```

Para crear sus propios archivos de prueba, primero necesitarán crear código de máquina. Para ello pueden ayudarse de V-Sim o hacerlo a mano. Si utilizan V-Sim tienen que crear un archivo `.s` y hacer un `dump` del código de máquina utilizando la bandera `-code` en la terminal:

```shell
vsim <archivo>.s -code <test_name>.input
```

Ustedes deben de poner las instrucciones en código de máquina en un archivo llamado `[test_name].input`
y colocar el archivo dentro de la carpeta `riscvcode/code`. Después, deben crear el archivo `[test_name].solution` el cual contendrá las instrucciones que se espera obtener; y colocar el archivo en la carpeta `riscvcode/ref`. Vean las pruebas proporcionadas como ejemplos de este tipo de archivos. Para integrar sus pruebas en el comando `make`, ustedes deben de modificar el archivo `Makefile`. En la línea 4 del archivo `Makefile`, donde dice `ASM_TESTS`, agregar `[test_name]` a la lista con espacios entre cada nombre de archivo:

```
SOURCES := utils.c part1.c part2.c riscv.c
HEADERS := types.h utils.h riscv.h

ASM_TESTS := simple multiply random test_name
```

Si su instrucción desensamblada no es igual a la esperada, ustedes obtendrán la diferencia entre el output esperado y el output que devolvieron. **Asegúrense de al menos pasar esta prueba antes de enviar la parte 1 al autograder**.

```shell
# Output Esperado
< 00001014: lui x8, 1048575
---
# Output Devuelto
> 00001014: Invalid Instruction: 0xfffff437
```

### Calificación Parte 1

**Recuerden que para la primera parte, solo deben modificar los archivos _part1.c_ y _utils.c_**, esto representa el 50% de su nota así que pueden enviar sus archivos al autograder para verificar su nota de esta parte haciendo:

```shell
./submit <TOKEN>
```

**Si están trabajando en pareja, <span style="color: red">AMBOS</span> miembros del grupo tienen que hacer el submit con su respectivo TOKEN**.

## Parte 2

Su segunda tarea es completar el emulador implementando los métodos **_execute_instruction()_**. **_execute()_**'s, **_store()_** y **_load()_** del archivo **_part2.c_**.


### Requisitos

Esta parte consistirá en implementar la funcionalidad de cada instrucción. Por favor implementen las funciones descritas a continuación (todas en **_part2.c_**).

* **_execute_instruction()_**: Ejecuta la instrucción proporcionada como parámetro. Ésta debería modificar los registros apropiados, realizar las llamadas a memoria necesarias, y actualizar el program counter para apuntar a la siguiente instrucción a ejecutar.

* **_execute()_**'s: Varias funciones de ayuda para ser llamadas en ciertas condiciones para ciertas instrucciones. Es su decisión usar estas funciones, pero éstas les ayudarán de gran manera a organizar el código.

* **_store()_**: Toma una dirección, un tamaño, un valor y almacena los primeros (tamaño) bytes del valor dado en la dirección dada. Cuando el parámetro `check_align` sea `1` se validarán las restricciones de alineación. Se incluyó este parámetro para obligar a las instrucciones a estar alineadas por palabras de memoria (word-aligned). Cuando implementen el `store` y `load`, este parámetro debe ser `0` dado que RISC-V no hace cumplir las restricciones de alineación.

* **_load()_**: Toma una dirección y un tamaño, y retorna los siguientes (tamaño) bytes empezando en la dirección dada. El `check_align` funciona de la misma forma que en `store()`.

### Probando la Parte 2

Les hemos provisto con un self-checking assembly test que prueba varias de las instruciones, sin embargo este test no es exhaustivo y no prueba todas las instrucciones. A continuación se ejemplifica cómo ejecutar los test (el output es de una solución correcta).

```shell
make part2
gcc -Wall -Werror -Wfatal-errors -O2 -o riscv utils.c part1.c part2.c riscv.c
simple_execute TEST PASSED!
multiply_execute TEST PASSED!
random_execute TEST PASSED!
-----------Execute Tests Complete-----------
```

Lo más probable es que ustedes tenga errores al empezar a realizar la parte 2, entonces prueben el modo de rastreo (_trace_) descrito en [Opciones en la linea de Comandos](#opciones-en-la-linea-de-comandos).

Les hemos provisto con unos cuantos tests más y la posibilidad de escribir test propios. Como en la parte 1, ustedes tendrá que crear archivos `.input`. Sin embargo para la parte 2, ustedes tendrá que nombrar su archivo solución con una extensión `.trace`.

Creen el nuevo archivo de ensamblador en el directorio `riscvcode` (utilicen `riscvcode/simple.input` como plantilla). Agreguen el nombre base del test a la lista de `ASM_TESTS` en el `Makefile`. Para realizar esto solo agreguen `[test_name]` al final de la línea 4.
Ahora compilen su test de ensamblador, y luego ejecútenlo escribiendo el siguiente comando:

```bash
make [test_name]_execute
```

Ustedes pueden, y en efecto deben, escribir sus propios test para probar instrucciones específicas y todos los posibles casos. Además ustedes deben compilar y probar su código después de cada grupo de instrucciones implementadas. De lo contrario será muy difícil probar su proyecto si esperan hasta el final.


### Calificación Parte 2

Al completar esta parte ustedes solo deberían haber modificado los archivos `part1.c`, `part2.c` y `utils.c`, deben realizar commit de todos los cambios realizados y enviar el link de su repositorio por medio del GES. Para obtener su nota completa pueden hacer:

```shell
./submit <TOKEN>
```

**Si están trabajando en pareja, <span style="color: red">AMBOS</span> miembros del grupo tienen que hacer el submit con su respectivo TOKEN**.

## Preguntas Frecuentes

### 1. ¿Cómo puedo empezar?

Lo mejor es revisar `types.h` y analizar la estructura `Instruction` para empezar a trabajar en la `parte1.c`, por ejemplo como acceder a cada campo de cada diferente tipo de instrucción y al opcode también. Por ejemplo para acceder al `opcode` pueden utilizar:

```c
instruction.opcode
```

siendo `instruction` una variable que representa una "instancia" de la estructura `Instruction`. Luego de esto pueden ver cómo accediendo a estos campos pueden decodificar la instrucción y así lograr imprimirla.

### 2. En mi máquina local saco 100% y en el autograder 0, ¿Por qué?

Al trabajar con uniones y estructuras de C y al utilizar la bandera `-O2` pueden pasar cosas muy raras, una de ellas es el [strict aliasing](https://cellperformance.beyond3d.com/articles/2006/06/understanding-strict-aliasing.html), por eso les recomendamos probar su código en la maquina virtual que les proporcionamos, así están totalmente seguros de que código funciona correctamente.

### 3. Me da Floating-point Exception (core dumped) al hacer algunas operaciones aritméticas, ¿Por qué?

Generalmente esto se da porque se divide por `0` o hay `overflow` utilizando variables enteras con signo. Por ejemplo

```c tab="Division por 0"
int x = 10;
int y = 0;
int z = x / y;
```

```c tab="Overflow"
int32_t x = 0x80000000;
int32_t y = 0xffffffff;
int32_t z = x / y;
```

La solución para la división por `0` es simplemente tienen que devolver `-1` como dice la especificación de RISC-V  y para el residuo devolver el primer argumento de la operación, en el caso de `overflow` la solución es castear las variables a un tipo con más bytes:

```c
int32_t z = (int32_t)((int64_t)x / (int64_t)y);
```

### 4. En la parte 1 el formato nunca es el esperado por las pruebas, ¿Por qué?

Seguramente no están utilizando el formato correcto, les recomendamos que utilicen las siguientes `macros` para imprimir las instrucciones que se encuentran en el archivo `utils.h`:

```c
#define RTYPE_FORMAT "%s\tx%d, x%d, x%d\n"
#define ITYPE_FORMAT "%s\tx%d, x%d, %d\n"
#define JALR_FORMAT "jalr\tx%d, x%d, %d\n"
#define MEM_FORMAT "%s\tx%d, %d(x%d)\n"
#define AUIPC_FORMAT "auipc\tx%d, %d\n"
#define LUI_FORMAT "lui\tx%d, %d\n"
#define JAL_FORMAT "jal\tx%d, %d\n"
#define BRANCH_FORMAT "%s\tx%d, x%d, %d\n"
#define ECALL_FORMAT "ecall\n"
```

### 5. ¿Puedo crear mis propias funciones?

Sí, siempre y cuando estas estén declaradas ya sea en `part1.c`, `part2.c` o `utils.c`, ya que son los únicos archivos que se envían al autograder. Sin embargo **<span style="color: red">NO</span> está permitido renombrar o eliminar las siguientes funciones**:

```c
/* archivo part1.c */
void decode_instruction(Instruction i);

/* archivo part2.c */
void execute_instruction(Instruction instruction, Processor* processor, Byte *memory);
void store(Byte *memory, Address address, Alignment alignment, Word value, int);
Word load(Byte *memory, Address address, Alignment alignment, int);
```

Ya que el simulador `riscv.c` espera que estas estén definidas.
