---
layout: post
title:  "Proyecto extra: Intérprete de Brainfuck"
date:   2018-05-15
category: proyecto
description: >
    En este proyecto pondrán a prueba su comprensión sobre punteros implementando un intérprete para el lenguaje Brainfuck.
---

#### Acerca de Brainfuck

Brainfuck es un lenguaje de programación esotérico notable por su extremo minimalismo. El lenguaje utiliza únicamente ocho símbolos y un par de punteros.

Punteros:
* Puntero a instrucciones: Cada vez que se ejecuta una instrucción se avanza al siguiente caracter.
* Puntero a datos: Se tiene un arreglo infinitamente grande donde se colocan los datos del programa. Este puntero se mueve gracias a las instrucciones > y <

Instrucciones:
* \>   mueve el puntero de datos a la siguiente casilla
* <   mueve el puntero de datos a la casilla anterior
* \+   aumenta el valor del dato de la casilla actual
* \-   disminuye el valor del dato de la casilla actual
* ,   lee un caracter y lo guarda en la casilla actual
* .   imprime el caracter que se encuentre en la casilla actual
* [   indica el inicio de un ciclo, cuando se encuentra este símbolo se consulta el contenido de la casilla actual, si esta casilla contiene un valor distinto a cero se continua normalmente, si contiene un cero se salta hasta el caracter ] correspondiente
* ]   indica el final de un ciclo, cuando se encuentra este símbolo se consulta el contenido de la casilla actual, si esta casilla contiene un cero se salta hacia el caracter [ correspondiente, si contiene un valor distinto a cero se continua normalmente

[Más información](https://esolangs.org/wiki/Brainfuck)

#### Tarea a realizar

Debe implementar la función interprete() que opere las ocho instrucciones del lenguaje.

```C
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned char data[1000] = {0};
unsigned char* inst = datos;

int main () {

  // Escribir un programa de Brainfuck puede ser dificil...
  // Agregar lectura de archivos y obtener desde allí el programa

  // Este programa de prueba incluye ciclos anidados
  // Le funcionó? Debería imprimir la letra "Q"
  interprete("++++++++[->++++++++++[->+<]<]>>+.");
  
}

void interprete () {

  // Implementar esta función para que las ocho instrucciones funcionen
  // Los ciclos pueden ser engañosos, tengan cuidado!
  
}
```

Puntaje:
* 10 pts: el intérprete lee archivos con el código de Brainfuck
* 10 pts: aceptar programas en varias líneas e ignorar comentarios
* 40 pts: las ocho instrucciones (incluyendo ciclos simples) funcionan
* 25 pts: ciclos anidados funcionan
* 15 pts: realice un programa en Brainfuck calcule el mismo resultado que el código siguiente (sumatoria), este programa debe poder ejecutarse en su intérprete

```C
#include <stdio.h>

int main () {
	printf("%i", sumatoria(5));
}

int sumatoria (int fin) {
	int res;
	int num;

	for (res = 0, num = 0; num <= fin; num++) {
		res += num;
	}

	return res;
}
```

#### Qué pasa con los ciclos?

Las instrucciones [ y ] van emparejadas, cuando encuentre alguna debe saltar hacia la correcta. Si encuentra un fragmento de código [ etc [ etc ] etc ], cómo sabe hacia dónde debe saltar con cada símbolo? Debe llevar el control acerca de a cuántos ciclos ha ingresado para poder moverse hacia el lugar correcto.

#### Entrega

Cree un repositorio privado (como hizo en el lab 0), comparta este repositorio con el usuario cc3-grades, y suba al GES link del repositorio en la fecha indicada.

Este proyecto se estaría calificando en la misma fecha que el proyecto final, por lo tanto no se pueden utilizar slip days.
