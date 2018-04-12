---
layout: post
title:  "Proyecto 2: Procesador: Register file y ALU"
date:   2018-04-12
category: proyecto
description: >
    Parte introductoria del proyecto 2
permalink: /:categories/:title.html
---

# Introducción

En este proyecto utilizaremos Logisim para implementar un procesador de 32-bits cuyo ISA es un subset de las instrucciones de RISC-V. Algunos componentes del proyecto serán más sencillos que los componentes de hardware verdaderos para evitar realizar trabajo repetitivo.

En esta parte completaremos el procesador, e implementaremos un pipeline de dos etapas. Algunos detalles importantes:

  * Pueden utilizar cualquier bloque ya existente en Logisim para el proyecto.
  * Guarden constantemente. Realicen commits y hagan push al menos una vez por cada día que trabajen.
  * Logisim es un excelente simulador pero ocasionalmente tiene errores, entonces hagamos caso a la indicación anterior. Guarden constantemente...
  * Trabajemos de la misma forma que en un proyecto de software: Construyamos el proyecto pieza por pieza y realicemos pruebas antes de unir un bloque con otros. Podemos construir todos los subcircuitos adicionales que necesitemos, siempre y cuando sigamos las reglas específicas que cada parte nos da (más de esto a continuación).
  * Se incluyen algunos harnesses para probar algunos componentes, igual que en la primera fase.
  * Necesitaremos más tests! Cada equipo debería hacer sus propios tests adicionales.
  * La unidad de memoria es word-addressed, no byte-addressed. No tenemos instrucciones sh y sb.

Finalmente las tres indicaciones más importantes:
  * Se les daran algunos armazones (harnesses) a los cuales sus circuitos se conectaran. ASEGURENSE QUE SÍ SE ADAPTAN DE FORMA CORRECTA, TODOS LOS TESTS FALLARAN SI NO LO HACEN.
  * En el camino nos hemos encontrado con algunos problemas de git merge si ambos miembros del equipo estaban trabajando en el mismo archivo; a veces git los resolvía automáticamente y a veces no. En Logisim es garantizado que git NO RESOLVERÁ ESTO DE FORMA CORRECTA, entonces si trabajamos en equipo NO DEBEMOS MODIFICAR EL MISMO ARCHIVO AL MISMO TIEMPO.
  * Asegurense que todos los cambios estén en cpu.circ. Si necesitan modularizar, utilicen subcircuitos.

# Obteniendo los archivos

Utilizaremos Github Classroom. No necesitan crear su propio repo ni agregar a cc3-grades, solo hacen click en el link, crean su grupo y listo. Sobre este repo harán sus commit y push.

[ARCHIVOS BASE](https://classroom.github.com/g/PENDIENTE)

# Iniciando: Procesador

Se les provee un esqueleto del procesador en cpu.circ. Su procesador tendrá una instancia de su ALU y Register File, así como una unidad de memoria que ya se le provee. Ustedes son los responsables de construir el datapath y control completos, desde cero. Su procesador completo debe implementar el ISA que se detalla más abajo, usando un pipeline de dos etapas como también se detalla abajo.

Su procesador obtendrá su programa del harness run.circ. Su procesador tendrá un output llamado FETCH_ADDRESS que indica cuál instrucción queremos, esta dirección será entregada al harness y este nos dará una instrucción. La instrucción será recibida por el procesador y será ejecutada. Revisen run.circ para ver exactamente qué sucede.

El procesador tiene dos inputs que vienen del harness:

Input Name | Bit Width | Descripción
--- | --- | ---
INSTRUCTION | 32 | Aquí se recibe la instrucción que se obtuvo en la dirección identificada por FETCH_ADDRESS.
CLOCK | 1 | Input del reloj. Puede ser necesario estar enviando esta señal a varios subcircuitos. Esta señal no debe pasar por ninguna compuerta (NOT, AND, etc).

El procesador debe tener los siguientes outputs que entregará al harness:

Output Name | Bit Width | Descripción
--- | --- | ---
s0 | 32 | Contenido de s0, solo para pruebas.
s1 | 32 | Contenido de s1, solo para pruebas.
t0 | 32 | Contenido de t0, solo para pruebas.
t1 | 32 | Contenido de t1, solo para pruebas.
a0 | 32 | Contenido de a0, solo para pruebas.
ra | 32 | Contenido de ra, solo para pruebas.
sp | 32 | Contenido de sp, solo para pruebas.
FETCH_ADDRESS | 32 | Dirección que indica que instrucción queremos obtener del harness. En respuesta a esto el harness enviará alguna instrucción a través de INSTRUCTION.

Como en la parte 1, tengan cuidado al mover componentes y asegurense que los pines de input y output coincidan con el harness.

# Iniciando: Memoria

Se les provee una memoria ya implementada :D

Un resumen de sus inputs y outputs.

Nombre | Tipo | Bit Width | Descripción
--- | --- | --- | ---
A: ADDR | input | 32 | Dirección a leer o escribir en la memoria.
D: WRITE DATA | input | 32 | Valor a escribirse en la memoria.
En: WRITE ENABLE | input | 1 | En = 1 en las instrucciones que escriben, En = 0 en las demás.
Clock | input | 1 | Señal de reloj que viene desde cpu.circ.
D: READ DATA | output | 32 | Datos leídos en la dirección especificada.
