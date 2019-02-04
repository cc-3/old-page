# Introducción a RISC V
- ISA: pegamento que une el hardware con el software. Una especie de "contrato" que nos dice lo que sí podemos hacer porque tiene un soporte por el hardware.
- RISC: reduced instruction set computer
	- MIPS, ARM, RISC-V.
	- Muchos regitros (32 de 32 bits, por ejemplo)
	- Pocas instrucciones (tamaño fijo)
	- Pocas instrucciones para acceder a memoria, 2 basicamente (lw y sw)
- CISC: complex instruction set computer
	- x86 (Intel)
	- Pocos regitros (128, 256 bits)
	- Muchas instrucciones (tamaño variable)
	-  Puede haber una operación de suma que guarda en memoria, que suma de memorial, etc.

## ¿Qué es RISC-V?
- La quinta versión de procesadores RISC diseñador por Berkeley
- Licencia libre
- Registros:
	~~~
	x0 - x31 
	x0 está alambrado a tierra
	t registros temporales
	s registros "seguros"
	sp
	gp
	~~~
- Los registros son ¡muy! rápidos (y caros)
- Los registros están en el procesador
