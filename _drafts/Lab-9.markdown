---
layout: post
title:  "Laboratorio 9"
date:   2017-01-10
category: lab
description: >
    En este Laboratorio trabajarán con OpenMP y conocerán el concepto de thread level parallelism.
---

#### Referencias adicionales

* [Hands On Introduction to OpenMP](http://openmp.org/mp-documents/omp-hands-on-SC08.pdf)
* [Official OpenMP Tutorial Listing](http://openmp.org/wp/resources/#Tutorials)

***

#### Introducción a OpenMP

**Basics**

En este laboratorio vamos a tomar ventaja de los múltiples cores de las computadoras del laboratorio. OpenMP es un framework de programación paralela para C/C++ y Fortran. En los últimos años a ganado mucha atención, especialmente después de que las computadoras traen multiples cores. Es simple y tiene buena performance. En este lab vamos a ver algunas de sus características, pero los links en las referencias adicionales les dan más información y tutoriales de este framework.

Hay muchos tipos de paralelismo y patrones para explotarlos. OpenMP escoge un modelo “nested fork-join”. Por defecto, un programa en OpenMP es un programa normal secuencial, excepto por las regiones que el programador explícitamente declara para que se ejecuten en paralelo. En la región paralela, el framework crea (forks) un set de threads. Estos threads ejecutan la mismas instrucciones, solo en diferentes porciones de los datos. En el final de la región paralela, el framework espera que todos los threads terminen (join) antes de dejar la región paralela y continuar secuencialmente.

![fig1](/assets/img/labs/forkjoin.jpg)

OpenMP usa “shared memory”, esto significa que todos los threads pueden acceder a la misma dirección de memoria. La alternativa a esto es “distributed memory”, que es preferido en los clusters donde los datos explícitamente son movidos entre direcciones. Muchos programadores encuentran el shared memory más fácil de programar desde que no se tienen que preocupar de mover sus datos, pero es mas difícil de implementar en hardware en una manera escalable. Más adelante en el lab vamos a declarar memoria local al thread (solo la puede acceder el thread que la creo) para propósitos de performance, pero el framework de provee la flexibilidad de que los threads compartan memoria sin ningún esfuerzo del programador.

##### Ejemplo Hello World

Para este lab, vamos a utilizar C para seguir ganando experiencia en este lenguaje. OpenMP es un framework con una interfaz en C, y no es algo que sea parte del lenguaje. La mayoría de las características de OpenMP son directivas que se le pasan al compilador. Consideren la siguiente implementación del Hello World (hello.c):

```c
int main() {
    #pragma omp parallel
    {
        int thread_ID = omp_get_thread_num();
        printf(" hello world %d\n", thread_ID);
    }
}
```

Este programa va a tomar el numero de threads por defecto y cada uno de ellos va imprimir “hello world” y también el numero de thread que es. El #pragma le dice al compilador que el resto de lineas es una directiva, y en este caso es omp parallel. Omp declara que es para OpenMP y parallel dice que el siguiente bloque de código (lo que esta dentro de {}) puede ejecutarse en paralelo. Pruebenlo:

```shell
$ make hello
$ ./hello
```

Noten que los números no están numéricamente ordenados y no salen en el mismo orden si corren hello varias veces. Esto es porque con una región paralela (omp parallel), el programador garantiza que las operaciones se pueden hacer en paralelo, y no hay orden entre los threads. Tampoco ganamos nada si la variable thread_ID es local a cada thread. En general con OpenMP, las variables declaradas afuera de un bloque omp parallel tienen una copia y son compartidas a través de todos los threads, mientras que las variables declaradas dentro de un bloque omp parallel tienen una copia privada para cada thread.

***

#### Ejercicio 1: Suma de Vectores

La suma de vectores es un código inherentemente paralelo, así que lo hace bueno para el primer ejercicio. La función v_add adentro de v_add.c va a retornar el arreglo que es la suma de 2 vectores x, y casilla por casilla. Un primer intento de esto puede verse así:

```c
void v_add(double* x, double* y, double* z) {
    #pragma omp parallel
    {
        for(int i=0; i<ARRAY_SIZE; i++)
            z[i] = x[i] + y[i];
    }
}
```

pueden correr esto (make v_add seguido de ./v_add) y el framework de prueba automáticamente va a tomar el tiempo y va a variar el numero de threads. Van a ver que lo hace bastante mal a medida de que incrementamos el numero de threads. Este problema es que cada thread esta ejecutando todo el codigo con un bloque omp parallel, significando que si tenemos 8 threads, realmente estamos sumando los vectores 8 veces. Para ganar velocidad cuando aumentamos el numero de threads, necesitamos que cada thread haga menos trabajo y diferente, no la misma cantidad como antes.

![fig2](/assets/img/labs/decomp.jpg)

Su tarea es modificar v_add para que sea mas rapido. La mejor manera de hacer esto, es decrementar la cantidad de trabajo que hace cada thread. Para guiarlos en este proceso, dos funciones útiles en OpenMP son:

```shell
int omp_get_num_threads();
int omp_get_thread_num();
```

la función omp_get_num_threads() va a retornar cuantos threads hay en un bloque omp parallel, y omp_get_thread_num() va a retornar el ID del thread.

Dividan el trabajo en cada thread a través de dos diferentes métodos (escriban diferente código para cada uno de los métodos):

* Primero, que cada thread se ocupe de hacer sumas adyacentes: i.e. el Thread 0 va a sumar los elementos en el index 0, Thread 1 va a sumar los elementos en el index 1, etc. Este metodo no va a ser muy eficiente. Se va encontrar con un problema conocido como “false sharing”.
* Segundo, si hay N threads, dividan el vector en N pequeños bloques, y hagan que cada thread solo sume ese pequeño bloque como la figura de arriba.

Para este ejercicio, les pedimos que manualmente dividan el trabajo a través de los threads. Sin embargo, los diseñadores de OpenMP hicieron una directiva for para automáticamente dividir el trabajo independientemente. Aquí esta la función reescrita utilizando esto. Ustedes NO van a usar esta directiva en su solución para este ejercicio (Ejercicio 1).

```c
void v_add(double* x, double* y, double* z) {
    #pragma omp parallel
    {
        #pragma omp for
        for(int i=0; i<ARRAY_SIZE; i++)
            z[i] = x[i] + y[i];
    }
}
```

***

#### Ejercicio 2: Producto punto

La siguiente interesante operación es el producto punto entre 2 vectores. Implementar esto no es muy diferente de v_add, pero el reto es como sumar todos los productos en la misma variable (reduction). Todos los threads van a tratar de leer y escribir a la misma dirección simultáneamente. Una solución es usar una “critical section”. El código en una “critical section” puede ser ejecutada un thread a la vez en cualquier tiempo. Así, teniendo una “critical section” naturalmente previene que múltiples threads traten de leer y escribir a los mismos datos. Una implementación burda va a proteger la suma con una “critical section”, como (dotp.c):

```c
void v_add(double* x, double* y, double* z) {
    #pragma omp parallel
    {
        #pragma omp for
        for(int i=0; i<ARRAY_SIZE; i++)
            z[i] = x[i] + y[i];
    }
}
```

Prueben el código (make dotp y ./dotp). Noten como la performance va empeorando cuando el numero de threads aumenta. Poniendo todo el trabajo de la reducción en una critical section, hacemos que todo el trabajo se haga un thread a la vez (que no es la idea del paralelismo). Vean si pueden solucionar este problema.

Primero, traten de arreglar el código sin utilizar el keyword Reduction en OpenMP. Hint: traten de reducir el numero de veces que un thread suma a la variable global_sum.

Después cuando les funcione, traten de arreglarlo utilizando el keyword Reduction de OpenMP (busquenlo en google para más información). La perfomance es mejor que en el caso de arreglarlo manualmente? Por qué?
