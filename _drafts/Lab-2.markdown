---
layout: post
title:  "Laboratorio 2"
date:   2017-01-03
category: lab
description: >
    Para este laboratorio ustedes aprenderán como compilar y correr un programa en C, también van a examinar diferentes tipos de control de flujo en C y por último mirar la representación interna de los números.
---
#### Compilando y Corriendo un programa en C

En este laboratorio, vamos a utilizar el compilador gcc desde el command line para compilar programas hechos en C. La manera mas simple de correr gcc es la siguiente:

```shell
$ gcc program.c
```

Esto compila program.c en un archivo ejecutable llamado a.out. Este archivo se puede correr con el siguiente comando.

```shell
$ ./a.out
HOLA MUNDO !!!
```

gcc tiene varias opciones que se le pueden mandar vía command line, las cuales esperamos exploren. En este lab, sin embargo, ustedes van a utilizar únicamente -o, que es usado para especificar el nombre del archivo ejecutable que gcc crea. Usando -o, ustedes van a utilizar los siguientes comandos para compilar program.c en un archivo ejecutable llamado program, y después correrlo.

```shell
$ gcc -o program program.c
$ ./program
HOLA MUNDO !!!
```

***

#### Ejercicio 1: Un programa simple en C


En este ejercicio, vamos a ver un ejemplo de definiciones macro. Las macro pueden ser un tema algo confuso, pero en la manera general en que trabajan es que antes de que un archivo de C es compilado, todos los nombres de las constantes macro son remplazadas exactamente con el valor que se les asigno. En este ejercicio, vamos a usar las definiciones macro exclusivamente como variables constantes. Aquí definimos NOMBRE_DE_CONSTANTE para referirnos a un valor literal (una literal entera). Noten que solo hay un espacio separando el nombre del valor.


```c
#define  NOMBRE_DE_CONSTANTE valor_literal
```

Ahora, miren el código que está en eccentric.c. Van a ver 4 diferentes tipos de control de flujo en C. Primero compilen y corran el programa para ver que hace. Jueguen con los valores de las constantes de las cuatro macro: V0 a V3. Vean como cambiándolas, cambia la salida del programa. Modificando estos únicos 4 valores, hagan un programa que reproduzca la siguiente salida:

```shell
$ gcc -o eccentric eccentric.c
$ ./eccentric

Berkeley eccentrics:
====================
Happy Happy Happy
Yoshua

Go BEARS!
```

Hay muchas combinaciones de valores que pueden dar esta salida. Ustedes deben considerar el menor numero de valores diferentes de V0 a V3 que pueden dar la misma salida. El máximo es 4 cuando todas estas constantes son diferentes unas de las otras.

***

#### Ejercicio 2: Bit Operations

Para este ejercicio, ustedes van a completar bit_ops.c implementado las siguientes 3 funciones de manipulación de bits. Ustedes van a querer utilizar operaciones tales como and (&amp;), or , xor (^), not (~), left shiffts (<<), y right shiffts (>>). Procuren no usar ningún ciclo o alguna estructura de control de flujo.

```c
// Retorna el n-esimo bit de x.
// Asuman que 0 <= n <= 31
unsigned get_bit(unsigned x,
                 unsigned n);

// Cambia el n-esimo bit del valor de x a v
// Asuman que 0 <= n <= 31, y v es 0 o 1
void set_bit(unsigned * x,
             unsigned n,
             unsigned v);

// Invierte el n-esimo bit del valor de x.
// Asuman que 0 <= n <= 31
void flip_bit(unsigned * x,
              unsigned n);
```

Una vez que hayan completado estas funciones, pueden compilar y correr su código usando lo siguiente:

```shell
$ gcc -o bit_ops bit_ops.c
$ ./bit_ops
```

Esto va a imprimir los resultados de unas pocas pruebas.

***

#### Ejercicio 3: Bit Analysis

Para este ejercicio, ustedes van a completar bit_count.c definiendo y implementando una función que analice los bits de un entero. Ustedes necesitan definir una función que dado un entero x sin signo, determine lo siguiente:

* Cuantos bits “1” hay en x
* La posición mas alta de un bit “1” en x
* La posición mas baja de un bit “1” en x

Van a asumir enteros de 32 bit, así que las posiciones validas van de 0 a 31. Si todos los bits son 0, ambas posiciones son -1 indicando que no hay bits de 1.

**En su implementación no pueden usar structs.**

Una vez que hayan declarado e implementado esta función, pueden compilar y correr su codigo utilizando lo siguiente.

```shell
$ gcc -o bit_count bit_count.c
$ ./bit_count 0x801
      NUMBER: 2049
        BITS: 2
   HIGHEST 1: 11
    LOWEST 1: 0
```

Noten que el programa toma una entrada, que es el numero que va a ser analizado. Prueben con varios números para ver que su programa este correcto.

#### Ejercicio 4: Abriendo archivos en C

En este ejercicio vamos a iniciar con la primera parte de su proyecto (para los que decidan hacer el editor de texto). 

En su carpeta de trabajo, ustedes tienen el archivo <b>editor.c</b>. Deben implementar el método main(int argc, char* argv[]) , donde <b>argc</b> es la longitud de los parámetros de con los que se 
manda a llamar al método main, y <b>argv</b> es un areglo de <i>char*</i> (el equivalente en C a Strings) que son los parámentros en sí (tomen en cuenta que el primer elemento de argv 
siempre es el nombre del ejecutable). 

Su programa debe tener dos modos de ejecución; en el primero debe mandar como parametro el nombre del archivo a leer, y en el segundo debe leer del usuario el nombre del archivo a ejecutar.
Asumiendo que existe en su directorio el archivo <b>hola.txt</b>, su programa se puede ejecutar de las siguientes formas:

```shell
$ ./editor hola.txt
hola mundo
```

```shell
$ ./editor
>>Nombre del archivo: hola.txt
hola mundo
```

Al implentar el segundo modo de ejecución, ustedes se daran cuenta que deberan manejar dinamicamente la memoria. Si aún no han leido el libro de <i>K&R</i>, probablemente querran usar Google
para investigar un poco de la función <b>malloc()</b>. Ademas de <b>malloc</b>, que sirve para reservar memoria, existe <b>realloc</b> que sirve para (si, lo adivinaron) realocar memoria. Sin
embargo, para este laboratorio <b>NO PUEDEN USAR realloc()</b>, por lo que deben implementar el método <b>expand(char* string, int currSize, int newSize)</b> que recibe un arreglo de caracteres
de longitud <i>currSize</i> y la nueva longitud (asumimos que newSize > currSize), y devuelve un arreglo de caracteres de longitud <i>newSize</i> con los datos guardados en el arreglo original. 
Deben liberar la memoria ocupada por el puntero <b>string</b> dentro de este método (probablemente deban leer un poo de la función <b>free()</b> si aun no lo han hecho).