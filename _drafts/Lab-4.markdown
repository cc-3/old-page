---
layout: post
title:  "Laboratorio 4"
date:   2017-01-05
category: lab
description: >
    En este laboratorio van a trabajar con dynamic memory allocation. y van a practicar con programas de Assembler utilizando MARS.
---

#### Introducción a Assembler y MARS

Los siguientes ejercicios utilizan un simulador de MIPS llamado MARS, que provee una buena interfaz gráfica de debbuging para el código. Pueden correr MARS en sus propias computadoras bajando el archivo jar en el siguiente [link](http://courses.missouristate.edu/kenvollmar/mars/MARS_4_5_Aug2014/Mars4_5.jar). Van a necesitar tener instalado Java en su computadora, o pueden utilizar (si no lo tienen instalado) esto para instalarlo (Únicamente en linux Ubuntu):

```shell
# Para ver si ya esta instalado
$ java -version
java version "1.7.0_91"

# Si no aparece lo de arriba
# Esto instala el java runtime environment y el compilador de java
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java8-installer -y
$ sudo apt-get install oracle-java8-set-default
```

Pueden correr MARS utilizando lo siguiente:

```shell
$ java -jar Mars4_5.jar
```

**Cosas básicas de Assembler:**

* Los programas de Assembler van en un archivo de texto con extensión (.s)
* Los programas deberían de llevar un label “main:” (similar a la función main() en C)
* Los programas deberían de terminar con “addi $v0, $zero, 10” seguido de un “syscall”.
* Las labels terminan con dos puntos (:)
* Los comentarios empiezan con numeral (#)
* No pueden poner mas de una instrucción por linea

***

#### Ejercicio 2: Acostumbrándose a usar MARS

**Para empezar:**

* Corran MARS (Como se les enseño arriba)
* Carguen lab4_ex2.s usando File-->Open
* Vean y editen el código en el tab “Edit”. Noten que el editor tiene highlighting y sugerencias de auto-completado
* Cuando estén listos, ensamblen su codigo usando Run-->Assemble (o presionando F3)
* Esto automáticamente los va a llevar al tab “Execute”, que es donde corren y pueden hacer debug a su programa
* Avancen en su programa linea por linea utilizando Run-->Step (o presionando F7)
* Deberían de tomarse el tiempo para familiarizarse con todo (como los atajos de teclado)

Para este ejercicio, van a calcular la serie de Fibonacci usando fib[0] = 0; fib[1] = 1; fib[n] = fib[n-1] + fib[n-2]
**Utilizando los siguientes pasos y guardando las respuestas a las preguntas. El menu de ayuda les puede servir (F1).**

1. ¿Qué significan las directivas .data, .word y .text? (Es decir, que ponen en cada sección)
2. ¿Cómo ponen un breakpoint en MARS? Pongan un breakpoint en la linea 14 y córranlo. ¿Cuál es dirección de la instrucción? ¿La linea 14 se ejecuta o no?
3. En el breakpoint, ¿Cómo continuan ejecutando su código? Corran el código completo
4. Encuentren la ventana “RUN I/O”. ¿Qué numero el programa saca? ¿Qué numero (n) de Fibonacci es ?
5. ¿En que dirección n es guardado en memoria? Prueben encontrar esto buscando en el Data Segment y Mirando el machine code (Text Segment)
6. Sin usar el editor, hagan que el programa calcule el 13° numero de Fibonacci, manualmente modificando la locación en memoria antes de ejecutarlo.
7. Lineas 19 y 21 usan la instrucción syscall. ¿Qué es y cómo se usa?

***

#### Ejercicio 3: Un programa corto en MIPS

Escriban un pedazo de código desde 0 que, dado un valor en $s0 o $s1, cumpla con lo siguiente:

```shell
    $t0 = $s0
    $t1 = $s1
    $t2 = $t0 + $t1
    $t3 = $t1 + $t2
    ...
    $t7 = $t5 + $t6
```

En otras palabras, para cada registro desde $t2 a $t7, guarden la suma de los 2 previos $t# registros. Los registros $s0 y $s1 contienen los valores iniciales. Pongan los valores iniciales de $s0 y $s1 manualmente usando MARS en vez de utilizando código. Finalmente, hagan que su código al final imprima el valor de $t7 como un entero (Hint: syscall)

**Guarden su código en un archivo llamado lab4_ex3.s.** No se olviden de usar una label “main:” y terminen su programa con “syscall 10”
