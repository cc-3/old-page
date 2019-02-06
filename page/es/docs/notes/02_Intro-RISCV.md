# Introducción a RISC V

Estos son algunos de los términos más importantes de este tema:
- ISA (probablemente uno de los términos mas importantes del curso): Es el *pegamento que une el hardware con el software*. *Una especie de "contrato" que nos dice lo que sí podemos hacer porque tiene un soporte por el hardware*. El **ISA** o **Instruction Set Architecture** es el set de instrucciones reales soportadas por el procesador sobre el que estamos trabajando.
- RISC: Reduced Instruction Set Computer
	- Un ejemplo de procesadores RISC son los procesadores MIPS, ARM y RISC-V.
	- Este tipo de procesadores utiliza muchos regitros (32 registros de 32 bits cada uno, por ejemplo)
	- Se caracteriza por tener pocas instrucciones, siendo todas de un tamaño fijo (32 bits, por ejemplo)
	- Existen pocas instrucciones para acceder a memoria, (2 basicamente: **lw** y **sw**)
	- La base de los procesadores RISC es soportar pocas instrucciones, pero hacerlas muy eficientemente
- CISC: Complex Instruction Set Computer
	- x86 x86_64 (Intel)
	- Este tipo de procesadores utiliza pocos regitros
	- Soporta una cantidad de instrucciones mucho mayor a los procesadores RISC, y muchas de estas instrucciones no son de un tamaño fijo
	-  La base de los procesadores CISC es soportar la mayor cantidad de instrucciones posibles para darle multiples opciones a los desarrolladores 

## ¿Qué es RISC-V?
- RISC-V es la quinta versión de procesadores RISC diseñador por Berkeley
- De licencia libre
- Los registros son ¡muy! rápidos (y caros) y se encuentran dentro del procesador
- Tiene un formato rigido: *operacion registro_destino registro_fuente1 registro_fuente2*
- Esta es la distribución de registros utilizada en procesadores RISC-V (nombrados del x0 al x31):

| Registros| Nombre | Función |
|-----|----|---|
| x0  | ZERO | Alambrado a tierra. x0 siempre contiene el valor 0x00000000 |
| x1  | RA | Return Address: Contiene la dirección de retorno de la función actual |
| x2  | SP  | Stack Pointer: Es un puntero a la cabeza del Stack |
| x3   | GP  | Global Pointer: Es un puntero a la sección global de Data |
| x4   | TP  | Thread Pointer: No lo utiilizaremos en este curso, pero cabe mencionar su existencia |
| x5-x7   | t0-t2  | Temporaries: Registros de proposito general que no se conservan en llamadas a funciones |
| x8   | s0/fp  | Saved Register (Frame Pointer): Registro *seguro*, se debe conservar su valor entre llamadas. El frame pointer contiene la dirección justo antes de la llamada a una función. Sirve para regresar el stack a su posición original al regresar de una función |
| x9   | s1  | Saved Register: Registro *seguro* de propósito general, se debe conservar su valor entre llamadas |
| x10-x11   | a0-a1  | Function Arguments & Return Values: Registros utilizados para enviar argumentos en las llamadas a funciones. Tambien son usados como valor de retorno de las funciones |
| x12-x17   | a2-a7  | Function Arguments: Registros utilizados para enviar argumentos en las llamadas a funciones |
| x18-x27   | s2-s11  | Saved Registers: Registros *seguros* de propósito general, se debe conservar su valor entre llamadas |
| x28-x31   | t3-t6  | Temporaries: Registros de proposito general que no se conservan en llamadas a funciones |

## Algunos Ejemplos en RISC-V

#### Convertir un ciclo a Ensamblador en RISC-V

~~~C
int a[20];
int sum = 0;
for(int i = 0; i <20;i++){
    sum+=a[i];
}
~~~

~~~Assembler
# Asumimos A = x8
    addi x5, x0, 0      # sum = 0
    addi x6, x0, 0      # i = 0
    addi x28, x0, 20    # x28 = 20
Condition:
    blt x6, x28, For    # Evaluamos la condición antes de empezar el ciclo
    j EndFor            # Si es falsa terminamos el ciclo
For:
    lw x7, 0(x8)
    add x5, x5, x7      # sum+=A[i]
    addi x8, x8, 4      # A++ ¿Por qué +4?
    addi x6, x6, 1      # i++
    j Condition
EndFor:
~~~