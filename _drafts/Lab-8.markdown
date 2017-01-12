---
layout: post
title:  "Laboratorio 8"
date:   2017-01-09
category: lab
description: >
    Llegó el momento de utilizar instrucciones SIMD y practicar loop unrolling.
---

#### Ejercicio 1: SIMD

Como hay una gran gama de instrucciones intrínsecas SIMD, queremos que ustedes aprendan como encontrar las que ustedes necesitar para realizar sus cosas.

Esta es una manera de encontrar la información necesaria:

1. Vayan a la pagina de [Intel](http://software.intel.com/en-us/avx/), busquen “Intel Intrinsics Guide”
2. En la parte izquierda van a ver la cantidad de tecnologías diferentes
3. Pueden buscar filtrando por tecnología y en el buscador de arriba de la página

Hagan su mejor esfuerzo para interpretar la nueva sintaxis y la terminología. Encuentren las intrínsecas de 128-bits para las siguientes operaciones SIMD:

1. Cuatro divisiones en punto flotante en precisión simple. (i.e. float NO double)
2. 16 operaciones max sobre enteros de 8-bits con signo (i.e. char)
3. Shift aritmético a la derecha de 8 enteros de 16-bits con signo (i.e. short)

**Escriban sus respuestas en un archivo de texto**

***

#### Ejercicio 2: Leyendo código SIMD

En este ejercicio van a considerar loa vectorización de una multiplicación de matrices de 2x2 en precisión double:

![fig1](/assets/img/labs/matmul.png)

Esto lleva a la siguientes operaciones aritméticas:

```shell
C[0] += A[0]*B[0] + A[2]*B[1];
C[1] += A[1]*B[0] + A[3]*B[1];
C[2] += A[0]*B[2] + A[2]*B[3];
C[3] += A[1]*B[2] + A[3]*B[3];
```

Les dimos el código sseTest.c que implementa estas operaciones en una manera SIMD.
Las siguientes instrucciones intrínsecas fueron utilizadas:

|      __m128d _mm_loadu_pd( double *p )     |  returns vector (p[0], p[1])  |
|      __m128d _mm_load1_pd( double *p )     |  returns vector (p[0], p[0])  |
| __m128d _mm_add_pd( __m128d a, __m128d b ) | returns vector (a0+b0, a1+b1) |
| __m128d _mm_mul_pd( __m128d a, __m128d b ) |  returns vector (a0b0, a1b1)  |
| void _mm_storeu_pd( double *p, __m128d a ) |    stores p[0]=a0, p[1]=a1    |

Compilen sseTest.c en código assembler de x86 y córranlo:

```shell
$ make sseTest.s
```

Encuentren el ciclo for en sseTest.s y identifiquen en que se convirtió cada instrucción intrínseca. ¿El ciclo en sseTest.s realmente existe?

**Escriban sus respuestas en un archivo de texto y comenten sseTest.s para que su auxiliar pueda verificar que si entendieron**

***

#### Ejercicio 3: Escribiendo código SIMD

para el ejercicio 3, van a vectorizar el siguiente código para ganar aproximadamente una mejora en velocidad de 4x sobre una implementación no tan buena que se muestra aquí:

```c
static int sum_naive(int n, int * a) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    return sum;
}
```

Van a encontrar las siguientes instrucciones intrínsecas útiles:

|          __m128i _mm_setzero_si128( )          |         returns 128-bit zero vector         |
|      __m128i _mm_loadu_si128( __m128i *p )     |  returns 128-bit vector stored at pointer p |
|  __m128i _mm_add_epi32( __m128i a, __m128i b ) | returns vector (a0+b0, a1+b1, a2+b2, a3+b3) |
| void _mm_storeu_si128( __m128i *p, __m128i a ) |     stores 128-bit vector a at pointer p    |


comiencen con sum.c, Utilicen instrucciones SSE intrínsecas para implementar la función sum_vectorized().

Para compilar su código, corran el siguiente comando:

```shell
$ make sum
```

***

#### Ejercicio 4: Loop Unrolling

Ustedes pueden obtener más mejoras en el perfomance! Cuidadosamente haciéndole unroll al código que crearon en el ejercicio anterior. Esto debería de llevarlos por un incremento de un factor de 2 en la perfomance. Como un ejemplo de loop unrolling, consideren la función sum_unrolled() que les damos:

```c
static int sum_unrolled(int n, int * a) {
    int sum = 0;

    // unrolled loop
    for (int i = 0; i < n / 4 * 4; i += 4) {
        sum += a[i+0];
        sum += a[i+1];
        sum += a[i+2];
        sum += a[i+3];
    }

    // tail case
    for (int i = n / 4 * 4; i < n; i++) {
        sum += a[i];
    }

     return sum;
}
```

Siéntanse libres de verificar el articulo de [Wikipedia](http://en.wikipedia.org/wiki/Loop_unrolling) que habla sobre loop unrolling para más información

En sum.c, copien su código de sum_vectorized() en sum_vectorized_unrolled() y hagan un unroll 4 veces.

Para compilar su código y correrlo, corran el siguiente comando:

```shell
$ make sum
```
