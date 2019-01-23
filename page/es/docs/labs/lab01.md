# Lab 1 - Punteros en C y GDB

## Objetivos

* Aprender cómo compilar y ejecutar un programa en C.
* Examinar diferentes tipos de control de flujo en C.
* Introducirlos al depurador de C
* Conseguir experiencia práctica utilizando GBD para depurar programas en C.
* Ganar más confianza al trabajar con punteros.



## Lecturas

![PH](/img/PH.jpg)

* P&amp;H: 2.4

##Preparación
<como conseguir los archivos necesarios?>. Aquí encontrarán todos los archivos necesarios para completar este lab. Más abajo, encontrarán cómo hacer esto.

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
