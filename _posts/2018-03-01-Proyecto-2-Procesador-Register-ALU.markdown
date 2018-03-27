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

[ARCHIVOS BASE](https://classroom.github.com/g/DbO-uyrW)

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

# Arithmetic Logic Unit (ALU)

La segunda tarea consiste en construir un ALU que soporte todas las operaciones que nuestro ISA necesita (estas operaciones descritas con más detalle a continuación). Una regla para simplificar las cosas: Nuestro procesador de RISC-V tratará el overflow como MIPS hace con las operaciones sin signo, es decir, el overflow se ignora por completo.

En alu.circ tenemos un esqueleto con tres entradas:

Nombre | Ancho en bits | Descripción
--- | --- | ---
X | 32 | Dato para usarse como X en la operación.
Y | 32 | Dato para usarse como Y en la operación.
Switch | 4 | Selecciona que operación se va a realizar.

Y dos salidas:
Nombre | Ancho en bits | Descripción
Equal | 1 | Resultado de X == Y
Result | 32 | Resultado de la operación del ALU.

A continuación la lista de operaciones a implementar, incluyendo sus valores de Switch. Se sugiere usar los bloques ya existentes en Logisim en lugar de construir nuevos.

Valor de switch | Instrucción
--- | ---
0 |	sll: Result = X << Y
1 |	srl: Result = (unsigned) X >> Y
2 |	add: Result = X + Y
3 |	and: Result = X & Y
4 |	or: Result = X | Y
5 |	xor: Result = X^Y
6 |	slt: Result = (X < Y) ? 1 : 0 Signed
7 |	mult: Result = X\*Y[31:0]
8 |	mulh: Result = X\*Y[63:32]
9 |	div: Result =(unsigned) X / Y
10 | rem: Result = X % Y

NOTA: El circuito multiplicador que ya existe en Logisim funciona con signo (cuando opera con números de 32-bits). NO se espera que implementen la multiplicación desde cero, usen este.

NOTA: Equal debe entregar como resultado X == Y. No importa que se pida en Switch, este siempre hace comparación de igualdad.

NOTA: El ALU debe coincidir con lo que la armazón (harness) alu_harness.circ pide. Mismas instrucciones que para el Register File en caso que muevan algo.

# Notas sobre Logisim

Si Logisim les da algún problema extrano, REINICIEN LOGISIM Y VUELVAN A CARGAR SU CIRCUITO. No pierdan tiempo buscando errores si no han hecho esto. Si reiniciar no ha resuelto el problema, allí si ya les corresponde revisar su circuito.

Logisim tiene un Reference, en la pestana Help lo encontrarán y les dice las especificaciones de cada componente.

Do NOT gate the clock! (esto no tiene una traducción directa). Los clocks tienen que llegar directo a los circuitos, ni en CC3 ni en un curso donde usen hardware deberían colocar compuertas antes que la senal de reloj entre al componente.

Si están usando varias ventanas de Logisim tengan mucho cuidado cuando hagan copy-paste de una ventana a otra. Asegurense que sí se copió el circuito completo que querían, y que funcione bien después de pegarlo.

Cuando importen otro archivo (Project -> Load Library -> Logisim Library...), este aparecerá como un folder en el panel de la izquierda. Los archivos esqueleto deberían ya tener importado todo lo necesario.

Cambiar los atributos antes de colocar un componente cambia el default. Si quieren colocar varios pines de 32 bits (por ejemplo), habría que cambiarlo antes de colocar el primero. Si solo quieren cambiar un valor para un componente, primero lo colocan y luego cambian.

Cuando cambiaan los inputs y outputs de un subcircuito que ya colocaron en main, Logisim automáticamente anade o remueve puertos según los cambios que hagan. Esto muchas veces afecta el tamano o posición del subcircuito. Si ya habían cables conectados, Logisim intentará moverlos, pero no siempre lo hace bien. Se recomienda que si van a cambiar los inputs y outputs de un circuito, primero desconecten todos los cables que este pueda tener en main, o lo eliminen del main y lo vuelvan a colocar después de cambiarlo.

Los cables rojos significan que algo está mal conectado. Algunos casos pueden no ser tan obvios, revisen bien todas las conexiones cercanas.
<!--- PENDIENTE AGREGAR IMAGEN --->

Logisim tiene algunas herramientas de análisis combinacional (nos puede construir mapas de Karnaugh o circuitos completos con solo darle una tabla :D). Esta herramienta les puede ser útil en algún momento de sus vidas, pero la recomendación es no usarla en CC3. Recuerden que durante los exámenes tendrán que hacer mapas o circuitos sin acceso a su computadora.

# Testing

Para esta parte se incluye un script para correr algunas pruebas en el ALU y Register File. El archivo se llama `run_sanity_check.sh`. Ejecutar este archivo realizará una copia de nuestro ALU y Register File hacia el directorio de testing y correrá dos tests para cada uno (estos tests también están en ese directorio). Su ALU y Register File serán automáticamente colocados en los harnesses y sus outputs se compararán.

Si un test falla y quieren saber que ocurrió, pueden ir al folder de testing y abrir el harness correspondiente a ese test. Click derecho en el Register File o ALU y eligen "view main". Ahora pueden ver el estado actual del Register File o ALU con los inputs que se le están dando en ese momento.

Los tests son muuuy simples. Revisen el archivo TESTING INSTRUCTIONS para ver cómo pueden hacer sus propios tests. Básicamente, quieren colocar valores en las unidades de memoria para probar todos los comportamientos distintos de sus componentes.

Por ejemplo, podemos hacer un test al hacer otro .circ similar a los que se proveen (alu-add.circ o regfile-insert.circ). Luego modificamos la unidad de memoria en el .circ nuevo y le colocamos distintos inputs y vamos verificando que el output sea el esperado. Para los sanity tests, se compara el output a los archivos .out de referencia. Los archivos .out tienen valores de salida para cada periodo de reloj a lo largo del cual se ejecuta el test. No es buena idea probar de esta manera, mejor observen manualmente los outputs de los circuitos.

NOTA: El autograder requiere poder ejecutar .sh y Python 2.7 (usen Linux, no se les dará soporte en esto si usan Windows).
