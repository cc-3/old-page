# Lab 3 - RISC-V

## Objetivos

* Practicar, corriendo y debuggeando código ensamblador RISC-V.
* Escribir funciones en RISC-V con el procedimiento correcto de llamadas a funciones.
* Tener una idea de como traducir código en C a RISC-V.

## Lecturas

![PH](/img/PH.jpg)

* P&amp;H: 2.12

## Preparación

Para comenzar con el laboratorio primero tienen que tener todos los archivos base, estos se encuentran [aquí](www.google.com). Recuerden que deben
aceptar la asignación de **GitHub Classroom** y se les creará automáticamente un repositorio con una extensión que termina con su usuario de GitHub.  
Cuando ya se haya creado el repositorio, pueden ejecutar los siguientes comandos abriendo una terminal (<kbd>CTRL</kbd> <kbd>+</kbd> <kbd>T</kbd> ):

```shell
git clone <link del repositorio>
```

> **NOTA**: Tienen que reemplazar <link del repositorio> con el link del repositorio que se creo.


## Introducción a Lenguaje Ensamblador RISC-V

Los siguientes ejercicios utilizan un ensamblador y simulador de RISC-V desarrollado por nuestro auxiliar **Andres Castellanos**. El simulador se llama **V-Sim** y pueden descargarlo [aquí](https://www.riscvsim.com).

<p align="center">
  <img src="/img/labs/lab03/vsim.png"  alt="V-Sim"/>
</p>

### Cosas básicas en V-Sim:

A continuación les vamos a dar una pequeña guía de V-Sim, para mas información visiten la página de documentación en [https://www.riscvsim.com](https://www.riscvsim.com).

* Pueden crear archivos, editarlos y borrarlos desde la pestaña "Editor".
* Los programas empiezan en la etiqueta global `main`, es decir que tienen que definir una etiqueta llamada `main` y declararla como global.

```asm
.globl main
main:
  li a0, 10
  ecall
```

* Las etiquetas terminan con dos puntos como ven en el ejemplo anterior.
* Los comentarios comienzan con el simbolo "#" o ";".
* NO PUEDEN poner mas de una instrucción por linea.
* Cuando hayan terminado de editar las instrucciones que conforman su código, guarden y presionen <kbd>F3</kbd> para preparar la ejecución.
* Los programas siempre tienen que terminar con un `ecall` y como argumento 10 en `a0`. Esto le indica al programa que tiene que terminar. Las instrucciones `ecall` son análogas a los "System Calls" (llamadas al sistema) y nos permite hacer cosas como imprimir a consola o reservar memoria dinámica.

## Ejercicio 1: Familiarizándote con V-Sim

Para este ejercicio ustedes van a familiarizarse con V-Sim corriendo un programa sencillo de RISC-V y luego contestaran unas preguntas.

1. Abran una terminal (<kbd>CTRL</kbd><kbd>+</kbd><kbd>T</kbd>) y dirijanse a la carpeta del repositorio que clonaron.
2. Abran el modo GUI de V-Sim ejecutando en la terminal `vsim`.
3. Desde el editor abran el archivo llamado **ex1.s** que esta en la carpeta **ex1**.
4. En la barra de herramientas de V-Sim, vayan a settings y asegúrense de que **Assemble Only Selected Tab** esté seleccionado con un cheque verde.
5. Presionen <kbd>F3</kbd>. Esto va a preparar el código para que pueda ser ejecutado y simulado. Si hacen click a la pestaña "Editor", su simulación
se va a reiniciar.
6. En el simulador, para ejecutar la siguiente instrucción, presionen el botón que dice "step".
7. Para regresar un paso atras, presionen el botón que dice "backstep".
8. Para correr todo el programa hasta que termine, presionen el botón que dice "go".
9. Para volver a empezar el programa nuevamente, presionen el botón que dice "reset".
10.  Para ver el contenido de los 32 registros en la parte derecha del simulador hay una pestaña que dice `RVI` y la consola esta en la parte de abajo.
11. Para ver el contenido de la memoria, en el mismo lugar que los registros hay una pestaña que dice `Memory`, pueden navegar a diferentes secciones de la memoria haciendo click derecho encima de la tabla que muestra el estado de la memoria.

### Preguntas

Ahora que ya han corrido su primer programa de RISC-V y que ganaron experiencia con V-Sim pueden contestar las siguientes preguntas en el archivo **ex1.txt** que se encuentra en la carpeta **ex1**.

1. ¿Qué significan las directivas .data, .word, .text, es decir, para qué las usas? Pista: Piensa acerca de las 4 secciones de memoria.
    * A) Son como etiquetas sirven para hacer referencia a cosas, con .data apuntamos hacia los datos con .word hacia palabras de 32 bits y con .text hacia texto y todo esto en memoria.
    * B) .data le indica al ensamblador que guarde los siguientes elementos en la sección estática de la memoria, .word que guarde una palabra de 32 bits en memoria y .text que estamos en la sección de texto y entonces deberíamos escribir instrucciones de ensamblador.
    * C) .data es para guardar datos en la sección de datos de la memoria, .word es para guardar palabras de 32 bits en la sección de palabras de la memoria, .text es para guardar texto ascii en la sección de texto de la memoria.
    * D) .data y .word no son directivas de ensamblador, y .text siempre esta por defecto.
2. Corran por completo el programa. ¿Qué número da como "output"?
3. ¿Qué representa el numero que da como output el programa?
    * A) Numero aureo
    * B) Factorial de 9
    * C) Fibonnaci de 9
    * D) Factorial de 10
4.  ¿En qué dirección de memoria (en hexadecimal) está almacenado "n"? Pista: Mira el contenido de los registros.
5. Sin utilizar la pestaña "Editor", haz que el programa calcule el 13º número (tomando en cuenta que el índice empieza en 0) de la sucesión de fibonacci, modificando manualmente el valor de un registro. Encontrarán útil de primero correr línea por línea el código. Si prefieren ver los valores en decimal, cambien esto haciendo click derecho sobre la tabla de registros y presionando "Decimal Display Mode". ¿Qué registro modificaron?

Un archivo válido que sigue el formato esperado por el autograder se ve de la siguiente manera:

```shell
1:A
2:0
3:A
4:0xbacacafe
5:zero
```

## Ejercicio 2: Traduciendo de C a RISC-V

Desde V-Sim abran el archivo **ex2.s** que esta en la carpeta **ex2** y desde algun editor de texto de su preferencia abran **ex2.c** que esta en la misma carpeta. El código ensamblador que se provee (archivo ex2.s) es una traducción del programa escrito en C (archivo ex2.c) pero en RISC-V. Su tarea es encontrar/explicar los siguientes componentes de este archivo escrito en lenguaje ensamblador en el archivo de texto llamado **ex2.txt**.

### Preguntas

1. ¿Cuál es el registro que representa la variable `k`?.
2. ¿Cuáles son los registros que actuan como punteros a los arreglos `source` y `dest` (separados por coma)?.
3. ¿De que numero de línea a que numero línea se encuentra el loop (separado por comas)?.
4. ¿En que numero de línea se copia el contenido de `source` a `dest`, es decir donde se puede observar `dest[k] = source[k]`?.
5. ¿Cómo son manipulados los punteros en el código?
    * A) En cada iteración se le suma k  a cada puntero, que es el equivalente en C a `arreglo[k]`.
    * B) En cada iteración se le suma k * 4 a cada puntero, que es equivalente en C a `arreglo[k]`.
    * C) En cada iteración se le hace corrimiento logico a la derecha a cada puntero, que es equivalente en C a `arreglo[k]`.
    * D) En cada iteración se le suma +1 a cada puntero, que es equivalente en C a `arreglo[k]`.

Un archivo válido que sigue el formato esperado por el autograder se ve de la siguiente manera:

```shell
1:zero
2:zero,sp
3:1,10
4:8
5:D
```

## Ejercicio 3: Factorial.

En este ejercicio, tienen que implementar la función de factorial en RISC-V que toma un solo parámetro entero $n$ y retorna $n!$. Pueden encontrar un esqueleto de esta función en el archivo **factorial.s** que se encuentra en la carpeta **ex3** del repositorio que clonaron. Ustedes solo necesitan agregar las instrucciones bajo la etiqueta `factorial`, y el argumento que se pasa a la función va en el registro `a0`. Pueden resolver este problema ya sea de forma recursiva o iterativa. Asegúrense de que su función retorne de forma apropidada lo siguiente $3! = 6$, $7! = 5040$ y $8! = 40320$.

## Ejercicio 4:  List Map

Para este ejercicio van a utilizar el archivo **list_map.s** que se encuentra en la carpeta **ex4**. En este ejercicio, van a completar una implementación de "map" con listas encadenadas en RISC-V. La función se simplificará en mutar la lista en cuestión, es decir tomara una lista encadenada
como entrada y va a retornar una nueva lista con los valores modificados. Nuestro procedimiento de "map" toma dos parámetros, el primer parámetro será la dirección del nodo "head" de una lista encadenada cuyos valores son enteros de 32 bits. Entonces, en C, la estructura se define como:

```c
struct node {
  int value;
  struct node *next;
};
```

El segundo parámetro sera la dirección de una función que toma un entero como argumento y retorna un entero. Usaremos la instrucción "jalr" de RISC-V para llamar a esta función  con los valores de cada nodo de la lista.

Nuestra función "map" irá hacia abajo de la lista recursivamente, aplicando la función a cada valor de la lista y almacenando el valor retornado al nodo correspondiente. En C, la función será algo como esta:

```c
void map(struct node *head, int (*f)(int))
{
  if(!head) { return; }
  head->value = f(head->value);
  map(head->next,f);
}
```

Si no habían visto el tipo de declaración `int (*f)(int)` antes, no se preocupen demasiado. Significa basicamente que `f` es un puntero a una función de en C, `f` puede ser usado exactamente como cualquier otra funcion. Les sera util acudir al green card de RISC-V que pueden encontrar [aqui](asd) para completar este ejercicio.

Hay exactamente 9 espacios (8 en "map" y 1 en "main") en el código que se provee en donde dice "YOUR_INSTRUCTION_HERE". Reemplacen esos espacios con las instrucciones de su implementación de map, y escriban una simple llamada a "map" con "square" como argumento de la función. Hay comentarios en el código que explican que debería hacer o cumplir cada instrucción. Cuando hayan rellenado los espacios con las instrucciones correctas, pueden correr el código pulsando en <kbd>F3</kbd> y debería de mostrar lo siguiente:

```shell
9 8 7 6 5 4 3 2 1 0
81 64 49 36 25 16 9 4 1 0
```

La primera línea es la lista original, y la segunda es la lista modificada después de que se aplicó la función "map".

## Calificación

Cuando hayan terminado su laboratorio o crean que estan listos para obtener su nota, pueden subir su laboratorio al autograder utilizando:

```shell
./submit <TOKEN>
```

> **NOTA**: Tienen que reemplazar <TOKEN> por el  token que les da la página [https://dashboard.cc-3.site/](https://dashboard.cc-3.site/)

Luego cuando haya sido calificado, pueden ver su resultado en [https://dashboard.cc-3.site/](https://dashboard.cc-3.site/).
