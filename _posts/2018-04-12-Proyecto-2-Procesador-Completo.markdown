---
layout: post
title:  "Proyecto 2: Procesador de RISC-V completo"
date:   2018-04-12
category: proyecto
description: >
    Instrucciones para completar proyecto 2. Procesador de RISC-V con pipeline de dos etapas.
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

[ARCHIVOS BASE](https://classroom.github.com/g/l_ssEGqO)

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

# Pipelining

Su procesador tendrá un pipeline de dos etapas:

  * Instruction Fetch: Se obtiene una instrucción de la memoria.
  * Execute: La instrucción es decodificada, ejecutada y los resultados se guardan (ya sea memoria o registros). Aquí se combinan las etapas restantes de la ejecución normal de una instrucción en RISC-V.

Trabajar de esta manera elimina los data hazards pero los control hazards siguen presentes. 

Recordemos entonces los delay slots. Cuando se empieza a ejecutar un branch, las siguientes instrucciones empiezan a ingresar al pipeline. Si el branch sí realiza el salto, las instrucciones que ya se ingresaron no se van a ejecutar y deberán ser eliminadas. Es nuestra responsabilidad "sacar" estas instrucciones del pipeline cuando ya sepamos que se va a realizar el salto que corresponde a un branch o a un jump. Para eliminar estas instrucciones debemos reemplazarlas por un nop, y que sea el nop el que se siga ejecutando durante ese ciclo. Un nop se representa como 0x00000000. Para reemplazar una instrucción por un nop, debemos buscar cuál es el momento indicado para hacerlo y agregar un MUX en nuestro circuito para que el nop entre cuando la ejecución de la instrucción ya vaya a medias.

Para los branches, solo reemplazaremos las instrucción por un branch si el salto del branch sí se realizará. Para un jump, siempre reemplazamos la instrucción.

**Es obligatorio implementar estas dos fases de pipelining, serán penalizados en su nota si entregan un procesador con una sola etapa.** Si el pipelining les presenta problemas, se recomienda primero construir el procesador con una sola etapa para verificar que todo (decodificación de instrucciones, señales de control, ALU, memoria, etc.) funcione bien.

Algunos detalles a considerar, respóndalos de forma personal antes de empezar a implementar el pipelining:

  * Dónde y cuándo realizamos el aumento del Program Counter?
  * Tendrán las fases de fetch y execute el mismo o distintos valores de PC?
  * Necesitamos guardar el PC entre una etapa y otra? Que más podríamos guardar?
  * Quién nos dice si el salto se realizará o no?
  * Si queremos reemplazar una instrucción por un nop, cuál es el momento indicado?
  * Si estamos ejecutando un nop, qué dirección le enviaremos al harness? Funciona esto distinto a una instrucción normal?

Nota: Recuerden que al iniciar o resetear su simulación, Logisim pone en cero los registros. Tengan esto en cuenta si colocan algún registro entre la fase fetch y execute.

# Control

Las señales de control tienen un papel muy importante en el proyecto. Se sugiere volver a leer el capítulo 4 del libro para darse cuenta dónde podemos necesitar un MUX, y por lo tanto alguna señal de control.

Existen varias formas de implementar las señales de control. Por ejemplo, pueden construir una palabra de control y guardarla en una memoria ROM, o pueden construir un circuito que elija qué acción tomar basándose en algunos bits del opcode, func3 y func7 (recuerden el ejemplo de clase para beq, bne, blt, bge).

**Es obligatorio que sus componentes estén unidos y las señales de control necesarias estén implementadas.** Si en la calificación del proyecto solo tiene componentes sueltos (como el ALU y Reg File de la primera fase), y estos no se comunican entre sí, su nota será muy cercana a cero.

Consejo final: Modularicen! Creen los subcircuitos que sean necesarios, y diseñenlos bien antes de empezar a construirlos.

# Instruction Set Architecture

Las instrucciones a implementar son las siguientes:

|Instruction|Type|Opcode|Funct3|Funct7/IMM|Operation|
|--- |--- |--- |--- |--- |--- |
|add rd, rs1, rs2|R|0x33|0x0|0x00|R[rd] ← R[rs1] + R[rs2]|
|mul rd, rs1, rs2|R|0x33|0x0|0x01|R[rd] ← (R[rs1] * R[rs2])[31:0]|
|sub rd, rs1, rs2|R|0x33|0x0|0x20|R[rd] ← R[rs1] - R[rs2]|
|sll rd, rs1, rs2|R|0x33|0x1|0x00|R[rd] ← R[rs1] << R[rs2|
|mulh rd, rs1, rs2|R|0x33|0x1|0x01|R[rd] ← (R[rs1] * R[rs2])[63:32]|
|slt rd, rs1, rs2|R|0x33|0x2|0x00|R[rd] ← (R[rs1] < R[rs2]) ? 1 : 0 (signed)|
|xor rd, rs1, rs2|R|0x33|0x4|0x00|R[rd] ← R[rs1] ^ R[rs2]|
|div rd, rs1, rs2|R|0x33|0x4|0x01|R[rd] ← R[rs1] / R[rs2]|
|srl rd, rs1, rs2|R|0x33|0x5|0x00|R[rd] ← R[rs1] >> R[rs2]|
|or rd, rs1, rs2|R|0x33|0x6|0x00|R[rd] ← R[rs1] \| R[rs2]|
|rem rd, rs1, rs2|R|0x33|0x6|0x01|R[rd] ← (R[rs1] % R[rs2]|
|and rd, rs1, rs2|R|0x33|0x7|0x00|R[rd] ← R[rs1] & R[rs2]|
|lb rd, offset(rs1)|I|0x03|0x0||R[rd] ← SignExt(Mem(R[rs1] + offset, byte))|
|lh rd, offset(rs1)|I|0x03|0x1||R[rd] ← SignExt(Mem(R[rs1] + offset, half))|
|lw rd, offset(rs1)|I|0x03|0x2||R[rd] ← Mem(R[rs1] + offset, word)|
|addi rd, rs1, imm|I|0x13|0x0||R[rd] ← R[rs1] + imm|
|slli rd, rs1, imm|I|0x13|0x1|0x00|R[rd] ← R[rs1] << imm|
|slti rd, rs1, imm|I|0x13|0x2||R[rd] ← (R[rs1] < imm) ? 1 : 0|
|xori rd, rs1, imm|I|0x13|0x4||R[rd] ← R[rs1] ^ imm|
|srli rd, rs1, imm|I|0x13|0x5|0x00|R[rd] ← R[rs1] >> imm|
|ori rd, rs1, imm|I|0x13|0x6||R[rd] ← R[rs1] \| imm|
|andi rd, rs1, imm|I|0x13|0x7||R[rd] ← R[rs1] & imm|
|sw rs2, offset(rs1)|S|0x23|0x2||Mem(R[rs1] + offset) ← R[rs2]|
|beq rs1, rs2, offset|SB|0x63|0x0||if(R[rs1] == R[rs2]) then {PC ← PC + {offset, 1b'0}}|
|blt rs1, rs2, offset|SB|0x63|0x4||if(R[rs1] less than  R[rs2] (signed)) then {PC ← PC + {offset, 1b'0}}|
|bltu rs1, rs2, offset|SB|0x63|0x6||if(R[rs1] less than  R[rs2] (unsigned)) then {PC ← PC + {offset, 1b'0}}|
|lui rd, offset|U|0x37|||R[rd] ← {offset, 12b'0}|
|jal rd, imm|UJ|0x6f|||R[rd] ← PC  +  4, PC ← PC + {imm, 1b'0}|
|jalr rd,rs, imm|I|0x67|0x0||R[rd] ← PC  +  4, PC ← R[rs] + {imm}|

# Notas sobre Logisim

Si Logisim les da algún problema extrano, REINICIEN LOGISIM Y VUELVAN A CARGAR SU CIRCUITO. No pierdan tiempo buscando errores si no han hecho esto. Si reiniciar no ha resuelto el problema, allí si ya les corresponde revisar su circuito.

Logisim tiene un Reference, en la pestana Help lo encontrarán y les dice las especificaciones de cada componente.

Do NOT gate the clock! (esto no tiene una traducción directa). Los clocks tienen que llegar directo a los circuitos, ni en CC3 ni en un curso donde usen hardware deberían colocar compuertas antes que la senal de reloj entre al componente.

Si están usando varias ventanas de Logisim tengan mucho cuidado cuando hagan copy-paste de una ventana a otra. Asegurense que sí se copió el circuito completo que querían, y que funcione bien después de pegarlo.

Cuando importen otro archivo (Project -> Load Library -> Logisim Library...), este aparecerá como un folder en el panel de la izquierda. Los archivos esqueleto deberían ya tener importado todo lo necesario.

Cambiar los atributos antes de colocar un componente cambia el default. Si quieren colocar varios pines de 32 bits (por ejemplo), habría que cambiarlo antes de colocar el primero. Si solo quieren cambiar un valor para un componente, primero lo colocan y luego cambian.

Cuando cambiaan los inputs y outputs de un subcircuito que ya colocaron en main, Logisim automáticamente anade o remueve puertos según los cambios que hagan. Esto muchas veces afecta el tamano o posición del subcircuito. Si ya habían cables conectados, Logisim intentará moverlos, pero no siempre lo hace bien. Se recomienda que si van a cambiar los inputs y outputs de un circuito, primero desconecten todos los cables que este pueda tener en main, o lo eliminen del main y lo vuelvan a colocar después de cambiarlo.

Los cables rojos significan que algo está mal conectado. Algunos casos pueden no ser tan obvios, revisen bien todas las conexiones cercanas.

Logisim tiene algunas herramientas de análisis combinacional (nos puede construir mapas de Karnaugh o circuitos completos con solo darle una tabla :D). Esta herramienta les puede ser útil en algún momento de sus vidas, pero la recomendación es no usarla en CC3. Recuerden que durante los exámenes tendrán que hacer mapas o circuitos sin acceso a su computadora.

# Entrega

La entrega se realizará en la fecha indicada en el GES (domingo). **No se contestan dudas por ningún medio el día anterior y el día de la entrega; no dejen el proyecto a última hora.**
