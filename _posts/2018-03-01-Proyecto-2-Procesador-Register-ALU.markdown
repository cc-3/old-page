---
layout: post
title:  "Proyecto 2: Procesador: Register file y ALU"
date:   2018-03-27
category: proyecto
description: >
    Parte introductoria del proyecto 2
permalink: /:categories/:title.html
---

# Introducción

En este proyecto utilizaremos Logisim para implementar un procesador de 32-bits cuyo ISA es un subset de las instrucciones de RISC-V. Algunos componentes del proyecto serán más sencillos que los componentes de hardware verdaderos para evitar realizar trabajo repetitivo.

Nuestro ISA utiliza 32 registros de 32 bits cada uno y una memoria cuyas direcciones son de 32 bits.

En esta introducción al proyecto trabajaremos el Register File y el ALU. A continuación algunos detalles importantes que debemos leer antes de iniciar.
<!--- PENDIENTE: DAR FORMATO --->
  * Pueden utilizar cualquier bloque ya existente en Logisim para el proyecto.
  * Guarden constantemente. Realicen commits y hagan push al menos una vez por cada día que trabajen.
  * Logisim es un excelente simulador pero ocasionalmente tiene errores, entonces hagamos caso a la indicación anterior. Guarden constantemente...
  * Trabajemos de la misma forma que en un proyecto de software: Construyamos el proyecto pieza por pieza y realicemos pruebas antes de unir un bloque con otros. Podemos construir todos los subcircuitos adicionales que necesitemos, siempre y cuando sigamos las reglas específicas que cada parte nos da (más de esto a continuación).
  * Se incluyen algunos tests. Solo se debe correr el script ./run-sanity-test.sh (esto seguramente tendran que hacerlo en Linux, se requiere Python 2.7 instalado que la mayoría de distribuciones traen ya por defecto).
  * Necesitaremos más tests! Cada equipo debería hacer sus propios tests adicionales. En la sección de *Testing* hay algunas indicaciones de cómo hacer pruebas adicionales para el ALU.

Finalmente las dos indicaciones más importantes:
  * Se les daran algunos armazones (harnesses) a los cuales sus circuitos se conectaran. ASEGURENSE QUE SÍ SE ADAPTAN DE FORMA CORRECTA, TODOS LOS TESTS FALLARAN SI NO LO HACEN.
  * En el camino nos hemos encontrado con algunos problemas de git merge si ambos miembros del equipo estaban trabajando en el mismo archivo; a veces git los resolvía automáticamente y a veces no. En Logisim es garantizado que git NO RESOLVERÁ ESTO DE FORMA CORRECTA, entonces si trabajamos en equipo NO DEBEMOS MODIFICAR EL MISMO ARCHIVO AL MISMO TIEMPO.
  
# Obteniendo los archivos

Utilizaremos Github Classroom. No necesitan crear su propio repo ni agregar a cc3-grades, solo hacen click en el link, crean su grupo y listo. Sobre este repo harán sus commit y push.

<!--- PENDIENTE: COLOCAR LINK --->

# Register File

Como aprendimos en clase, RISC-V tiene 32 registros. En el proyecto solo implmentaremos 9 (abajo se indica cuales) para evitar realizar trabajo repetitivo. Todas nuestras senales (rs1, rs2, rd) siguen siendo de 5-bits, pero solo se estarán usando los registros indicados.

El register file debe poder leer y escribir a los registros que se especifiquen según la instrucción, sin afectar o modificar a cualquier otro registro. Existe una excepción: El registor cero está alambrado a tierra y su valor no puede ser cambiado por ningún motivo.

Los registros que utilizaremos son los siguientes:

Registro por número | Registro por nombre
--- | ---
x0 | zero
x1 | ra
x2 | sp
x5 | t0
x6 | t1
x8 | s0
x9 | s1
x10 | a0
x11 | a1

En el archivo regfile.circ encuentran el esqueleto de un register file. Este tiene seis entradas:

Nombre | Ancho en bits | Descripción
---  | --- | ---
Clock | 1 | Senal de reloj. Aqui se recibirá una senal de reloj "non gated", es decir se recibe la senal directa sin ser afectada por ANDs, NOTs o cualquier compuerta.
Write Enable | 1 | Indica si se debería escribir a registro en el siguiente flanco de subida del reloj.
Read Register 1 | 5 | Registro a leer y cuyo valor será enviado a Read Data 1.
Read Register 2 | 5 | Registro a leer y cuyo valor será enviado a Read Data 2.
Write Register | 5 | Determina cual registro será modificado en el siguiente flanco de subida (asumiendo que Write Enable = 1).
Write Data | 32 | Los 32 bits de datos a guardarse en el registro en el siguiente flanco de subida (asumiendo que Write Enable = 1).

El register file tiene las siguientes salidas:

Nombre | Ancho en bits | Descripción
--- | --- | ---
Read Data 1 | 32 | Datos que se están leyendo, según el registro que Read Register 1 pidió.
Read Data 2 | 32 | Datos que se están leyendo, según el registro que Read Register 2 pidió.
s0 Value | 32 | Valor de s0 (salida para DEBUG/TEST).
s1 Value | 32 | Valor de s1 (salida para DEBUG/TEST).
t0 Value | 32 | Valor de t0 (salida para DEBUG/TEST).
t1 Value | 32 | Valor de t1 (salida para DEBUG/TEST).
a0 Value | 32 | Valor de a0 (salida para DEBUG/TEST).
ra Value | 32 | Valor de ra (salida para DEBUG/TEST).
sp Value | 32 | Valor de sp (salida para DEBUG/TEST).

Las salidas para DEBUG/TEST están presentes porque son registros de uso frecuente (por ejemplo, tienen un trabajo importante en las llamadas a funciones). Se utilizarán solo para pruebas del autograder. En un register file de verdad estas salidas no existirían. Para el proyecto deben estar presentes y funcionar bien para facilitar la calificación

Pueden modificar regfile.circ como deseen, pero las salidas deben cumplir con el comportamiento que se indica. El register file debe coincidir con el armazón (harness) que se les provee en regfile-harness.circ. Deben ser cuidadosos de no reordenar los inputs o outputs. Si necesitan más espacio, pueden moverlos mientras sean cuidadosos de mantener el posicionamiento relativo que estos tienen. Para verificar que nuestros cambios no rompan nada, podemos abrir regfile-harness.circ y revisar que no existan errores allí y todo funcione bien.

HINTS: (1) Cuidado con los muxes. Si estos tienen un enable ese debería estar activo (o mejor aún, buscamos en la ayuda de Logisim cómo quitar esa funcionalidad). (2) Tri-estado? Three-state? En CC3 no debemos pensar en estados de alta impedancia (qu'est-ce que c'est?) entonces lo mejor es deshabilitar el uso de three-state.

