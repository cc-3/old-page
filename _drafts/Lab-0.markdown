---
layout: post
title:  "Laboratorio 0"
date:   2017-01-01
category: lab
description: >
    En este laboratorio van a verificar si tienen las "habilidades" necesarias de programación para este curso. Crearan una cuenta de github, aprenderán a utilizar git y realizarán unos ejercicios en Java.
---

#### Ejercicio 1.1: Fibonacci

Escriban una función que, dado un número n, retorne el enésimo número de la serie de Fibonacci. La función está dada por el código de abajo:

```java
// Retorna el enesimo numero de Fibonacci. Asuman que n >= 0.
public static int fibonacci(int n) {

    // Su codigo aqui

}
```

La serie de Fibonacci está definida por lo siguiente:

```
Fib0 = 0
Fib1 = 1
Fibn = Fibn-1 + Fibn-2        

Donde Fibn es el n-esimo numero de Fibonacci.
```

La lista de los primeros 10 números de Fibonacci son los siguientes:

```
Fib0 = 0
Fib1 = 1
Fib2 = 1
Fib3 = 2
Fib4 = 3
Fib5 = 5
Fib6 = 8
Fib7 = 13
Fib8 = 21
Fib9 = 34
```
***

#### Ejercicio 1.2: Zipper

Escriban una función que dado dos arreglos, cada uno ordenado de menor a mayor, retorne un nuevo arreglo que contenga todos los elementos de ambos arreglos ordenados de menor a mayor. Por ejemplo, si los arreglos de entrada son los siguientes:

```java
entrada_1 = {1, 4, 7, 8, 8 , 9}
entrada_2 = {2, 4, 6, 8}
```

La salida debería de ser un arreglo que contenga los elementos en el siguiente orden:

```java
    salida = {1, 2, 4, 4, 6, 7, 8, 8, 8, 9}
```

La función está dada por el siguiente código:

```java
// Deben asumir que first y second no son null
public static int[] zipper(int[] first, int[] second) {

    // Su codigo aqui

}
```
***

#### Ejercicio 1.3: Permutación

Escribe una función que, dado un string de letras minúsculas, y un entero de 1 al 25, devuelva un nuevo string con el mensaje permutado la cantidad indicada de espacios.

Por ejemplo, si el mensaje recibido es “abcdefg”y el número es 3, ‘a’ ahora se correría y se volvería ‘d’ , ‘b’ se volvería ‘e’ , ‘c’ se volvería ‘f’ , y así sucesivamente, así que el nuevo mensaje sería “defghij”. Utiliza el alfabeto inglés (NO INCLUYAS LA LETRA ‘ñ’).

La función está tiene que llevar la siguiente firma:

```java
// Asuma que todos los parametros son validos
public static String permutation(String message, int spaces) {

    // Su codigo aqui

}
```
