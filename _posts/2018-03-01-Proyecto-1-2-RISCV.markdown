---
layout: post
title:  "Proyecto 1: Desensamblador de RISCV PARTE 2"
date:   2018-03-01
category: proyecto
description: >
    Parte 2 del proyecto 1
permalink: /:categories/:title.html
---

# Parte 2
Su segunda tarea es completar el emulador implementando los métodos `execute_instruction()`. `execute()`'s, `store()` y `load()` del archivo `part2.c`.

Esta parte consistirá en implementar la funcionalidad de cada instrucción. Por favor implemente las funciones descritas a continuación (todas en `part2.c`).


 * `execute_instruction()` - ejecuta la instrucción proporcionada como parámetro. Ésta debería modificar los registros apropiados, realizar las llamadas a memoria necesarias, y actualizar el program counter para apuntar a la siguiente instrucción a ejecutar.

 * `execute()`'s - varios archivos de ayuda para ser llamados en ciertas condiciones para ciertas instrucciones. Es su decisión usar estas funciones, pero éstas le ayudarán de gran manera a organizar el código.

 * `store()` - toma una dirección, un tamaño, un valor y almacena los primeros (tamaño) bytes del valor dado en la dirección dada. Cuando el parámetro `check_align` sea `1` se validarán las restricciones de alineación. Se incluyó este parámetro para obligar a las instrucciones a estar alineadas por palabras de memoria (word-aligned). Cuando implemente el `store` y `load`, este parámetro debe ser 0 dado que RISC-V no hace cumplir las restricciones de alineación.

 * `load()` - toma una dirección y un tamaño, y retorna los siguientes (tamaño) bytes empezando en la dirección dada. El `check_align` funciona de la misma forma que en `store()`.

Le hemos provisto con un self-checking assembly test que prueba varias de las instruciones, sin embargo este test no es exhaustivo y no prueba todas las instrucciones. A continuación se ejemplifica cómo ejecutar los test (el output es de una solución correcta).

We have provided a simple self-checking assembly test that tests several of the instructions. However, the test is not exhaustive and does not exercise every instruction. Here's how to run the test (the output is from a working processor).

```bash
$ make part2
gcc -Wall -Werror -Wfatal-errors -O2 -o riscv utils.c part1.c part2.c riscv.c
simple_execute TEST PASSED!
multiply_execute TEST PASSED!
random_execute TEST PASSED!
-----------Execute Tests Complete-----------
```

Lo más probable es que usted tenga errores, entonces pruebe el modo de rastreo (descrito en la parte 1) u otros modos de debugging descritos en la sección de Framework en la parte 1.

Le hemos provisto con unos cuantos tests más y la posibilidad de escribir test propios. Como en la parte 1, usted tendrá que crear archivos `.input`. Sin embargo para la parte 2, usted tendrá que nombrar su archivo solución con un `.trace`.

Cree el nuevo archivo de ensamblador en el directorio `riscvcode` (utilice `riscvcode/simple.input` como plantilla). Agregue el nombre base del test a la lista de `ASM_TESTS` en el `Makefile`. Para realizar esto solo agregue `[test_name]` al final de la línea 4.
Ahora compile su test de ensamblador, y luego ejecútelo escribiendo el siguiente comando:
```bash
make [test_name]_execute
```

Usted puede, y en efecto debe, escribir sus propios test para probar instrucciones específicas y sus casos corner. Además usted debe compilar y probar su código después de cada grupo de instrucciones implementadas. De lo contrario será muy difícil probar su proyecto si espera hasta el final.


Al completar esta parte usted solo deberia haber modificado los archivos `part1.c`, `part2.c` y `utils.c`, debe realizar commit de todos los cambios realizados y enviar el link a su repositorio por medio del GES.
