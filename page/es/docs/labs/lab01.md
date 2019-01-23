# Lab 1 - Punteros en C y GDB

## Objetivos

* Aprender cómo compilar y ejecutar un programa en C.
* Examinar diferentes tipos de control de flujo en C.
* Introducirlos al depurador de C
* Conseguir experiencia práctica utilizando GBD para depurar programas en C.
* Ganar más confianza al trabajar con punteros.

##Preparación
Visiten este [link](https://classroom.github.com/a/R92ylAB1). Aquí encontrarán todos los archivos necesarios para completar este lab. En esta página, encontrarán un botón que dice "Accept assignment". Al presionar este botón, se creará automáticamente un repositorio en Github llamado cc-3/lab1-c-gdb-<USUARIO>. Noten que el "dueño" de este repositorio es un usuario llamado `cc-3`, y su usuario es únicamente el sufijo del nombre del repo. De esta forma, nos encargamos de tener acceso siempre a su código, en caso existan copias o cualquier otro tipo de trampa. Sepan de una vez que, si encontramos plagio en sus laboratorios, su nota será AUTOMÁTICAMENTE 0,  sin posibilidad de cambiarla. De repetirse nuevamente este acontecimiento, el staff del curso organizará una reunión con ustedes y sus directores de carrera para contarles lo ocurrido.

Después de realizar esto, en la máquina virtual (o sus propias computadoras) abran una terminal en el directorio que prefieran, y ejecuten el siguiente comando:
```shell
git clone https://github.com/cc-3/lab1-c-gdb-<SU USUARIO DE GITHUB>
```

## Compilando y ejecutando un programa de C
En este laboratorio, estaremos usando el programa `gcc` para compilar programas en c. La manera más sencilla de ejecutar `gcc` es la siguiente:
```shell
gcc program.c
```
Esto compila el archivo `program.c` y crea un archivo ejecutable llamado `a.out`. Si tienen experiencia en Java, pueden más o menos considerar a `gcc` como el equivalente en C de `javac`. Este archivo se puede ejecutar con el siguiente comando:
```shell
./a.out
```
El archivo ejecutable es `a.out`, así que, ¿Qué rayos es eso de el punto y diagonal? La respuesta: cuando quieren ejecutar un ejecutable, es necesario preponer una ruta de archivo para distinguirlo de un comando como `python`. El punto se refiere al "directorio actual". De paso, dos puntos (..) se referirían al directorio que está un nivel arriba.




----fin-----
