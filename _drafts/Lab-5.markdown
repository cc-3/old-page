---
layout: post
title:  "Laboratorio 5"
date:   2017-01-06
category: lab
description: >
    Aquí ganarán mas práctica en llamadas a funciones en MIPS y también aprenderán a manipular punteros.
---

#### Ejercicio 1: Listas

Este ejercicio usa el archivo **listmanips.s**

En este ejercicio, ustedes van a implementar una función map en MIPS. Su función va ser simplimente cambiar una lista in-place, es decir, sin la necesidad de crear y retornar una nueva lista con los valores modificados. Su procedimiento “map” va a tomar dos parámetros. El primer parámetro va a ser la dirección del head de una linked-list que sus valores son enteros de 32-bits. Así que el struct en C estaría definido de la siguiente manera:

```c
struct node {
      int value;
      struct node * next;
};
```

El segundo parámetro va a ser la dirección de la función que toma como parámetro un entero y devuelve un entero. Van a utilizar jalr para llamar a esta función con la lista.

Su función “map” recursivamente va ir bajando en la lista visitando cada nodo, aplicando la función a cada valor de la lista y guardando el valor retornado en esa posición. En C, esto se miraría algo así:



```c
void map(struct node * head, int (* f)(int)) {
    if(!head) { return; }
    head->value = f(head->value);
    map(head->next,f);
}
```

Si nunca habían visto este tipo de declaración (* f)(int), no se preocupen. Básicamente significa que f es un puntero hacia una función, que en C es utilizada como cualquier otra función.

Van a necesitar usar una instrucción que tal vez no hayan visto antes, para implementar esto: jalr. jalr casi lo mismo que jr, solo que esta instrucción salta a una dirección que esta guardada en un registro y guarda la dirección de la siguiente instrucción (esto es PC + 4) en $ra. Así que si no quieren utilizar jal, pueden usar jalr para llamar a una función así:

```shell
# Quiero llamar a la funcion garply pero sin usar jal

# Asi que yo cargo la direccion de garply en el registro ($t0)
la $t0 garply
# y despues utilizo jalr para hacer jump and link register
jalr $t0      
```

Hay 7 lugares (6 en map y 1 en main) en el codigo que les dimos que dicen “YOUR_INSTRUCTION_HERE”. Remplacen estas instrucciones para finalizar la implementación de map, y hagan que el programa llame a map con square como la función que se pasa en los argumentos. Cuando hayan terminado de completar todo, al correr el código les debería generar la siguiente salida:

```shell
List Before: 9 8 7 6 5 4 3 2 1 0
List After: 81 64 49 36 25 16 9 4 1 0
```

***

#### Ejercicio 2: Prologo y Epilogo

Añadan el prologo y el epilogo al código en nchoosek.s que calcula nCr = n!/(r!(n-r)!) que en teoria combinatoria es un método de selección de varios elementos o símbolos de un grupo más grande o un conjunto de datos, donde no importa un orden. Esta función esta en su calculadora y es nCr.

***

#### Ejercicio 3: First 1 Pos


Escriban 2 versiones de una función llamada first1pos (usando first1pos.s) que, dado un valor en el registro $a0, retorne en el registro $v0 la posición del bit más significativo en el registro $a0. Si $a0 tiene como valor el 0, guarden -1 en el registro $v0. Esta permitido que modifiquen $a0 en el proceso de buscar la posición. Las posiciones van de 0 (el bit menos significativo) a 31 (el bit mas significativo).

Una de sus soluciones repetidamente tiene que hacer shift a $a0, verificando el “bit de signo” en cada shift. La otra solución debería utilizar un mask con valor 0x80000000 y repetidamente hacer un shift a la derecha para verificar cada bit en $a0.
