---
layout: post
title:  "Laboratorio 7"
date:   2017-01-08
category: lab
description: >
    En esta ocasión ustedes van a ganar experiencia y entendimiento corriendo MapReduce. Se van a familiarizar con Apache Spark y utilizar Spark localmente.
---

#### Un poco de información

**Spark**

En este laboratorio los vamos a introducir a un cluster computing framework llamado Spark. Existen varios más, pero para este curso utilizaremos solo este ya que, en el se basa el proyecto 2, es rápido y se programa en Python (todo es más fácil con Python).

**Eviten utilizar variables globales**

Cuando estén usando Spark, eviten el uso de variables globales. Esto mata el propósito de tener múltiples tareas corriendo en paralelo y crea embotellamientos cuando múltiples tareas tratan de acceder a la misma variable global. Como resultado, la mayoría de algoritmos van a ser implementados sin el uso de variables globales. Si es necesario, en Spark, pueden hacer uso de broadcast variables, sin embargo, para este laboratorio no las vamos a necesitar.

**Como correr Spark vía Command Line**

Para este laboratorio y en el proyecto les vamos a proveer un script que los va a ayudar a correr sus archivos de Spark, pero cuando creen sus propios archivos (o usen Spark fuera de la clase, que la verdad deberían para aprovechar su computadora al 100%), van a necesitar saber como correr Spark vía command line. Para nuestra versión de Spark (que es 1.6), para correr su archivo de Spark x.py (similar a como corren los archivos de Python, python x.py), solo tienen que correr el siguiente comando:

```shell
$ spark-submit x.py # Corre el archivo spark x.py
```

Si sus archivos de Spark toman argumentos (como la mayoría de archivos que les proveímos), el comando va a ser similar, pero le van añadir cualquier cantidad de argumentos que necesiten, asi:

```shell
# Corre el archivo de spark x.py y le pasa los argumentos arg1 arg2
$ spark-submit x.py arg1 arg2
```

Spark incluye un interprete que corre con Python y les va dejar testear cualquier comando de Spark ahí mismo. El interprete de Spark también permite recibir archivos de Spark (le pasan los archivos con la bandera --py-files) y entonces va a cargar los archivos que están en el mismo directorio donde se esta ejecutando). Si están buscando solo correr el interprete, el comando es el siguiente:

```shell
$ pyspark # Corre el interprete de Spark.
```

Si ustedes quieren precargar algunos archivos (digamos a.py, b.py, c.py), pueden correr el siguiente comando:

```shell
# Corre el interprete de Spark
# y ahora pueden importar cosas de a, b y c.
$ pyspark –py-files a.py, b.py, c.py
```

**Tips Rápidos para hacer debugging en Spark**

Si alguna vez se encuentran preguntándose porqué su output es raro o alguna cosa no sirve en sus archivos de Spark, recuerden estos pocos rápidos tips!

* Hagan uso de la función take! La función take puede correr en cualquier objeto RDD (cualquier objeto que estén tratando de paralelizar o correr cualquier función de transformación/acción en el (van a leer de esto después)). Esta función toma un argumento N, que es un entero y va a returnar los primeros N elementos dentro de su objeto RDD. Para más información acerca de esto, vean la documentación de take.
* Ustedes también pueden probar sus funciones (map, reduce, etc) dentro del interprete de Spark (pyspark, mencionado arriba). Simplemente importen la función que quieren probar en pyspark (explicado arriba) y asi van a ser capaces de correr la funcion y verificar si su output es el esperado!.

**Documentación, y Recursos adicionales**

* Un quickstart programming guide para Spark (hagan click al tab de Python para ver código de Python (no scala, no java)) esta disponible aquí.
* La versión de Spark que vamos a usar es la 1.6 y el link para el API documentation está disponible aquí.

***

#### Ejercicio 1: LineCount

Para el primer ejercicio ustedes van a contar el numero de lineas que tiene el quijote. Su implementación debería de ir en linecount.py. Dentro del archivo van a encontrar información útil para saber lo que tienen que hacer.

Para correr su codigo simplemente:

```shell
$ make run-linecount
```

Esto les va a generar una carpeta llamada linecount-out, y su output va a estar en part-00000 verifiquen que se parezca a linecount-expected que esta en la carpeta de archivos. El key puede que no sea igual, pero el numero tiene que ser igual.

***

#### Ejercicio 2: WordCount

Para este ejercicio van a implementar un contador de palabras, esto lo van a implementar en **wordcount.py**. Este va a tomar un archivo de texto, lo va a convertir en un RDD (objeto de Spark paralelizable) y le va a aplicar MapReduce. Ustedes tienen que implementar las funciones de map y reduce. En el archivo que tienen que modificar van a encontrar información para implementarlo. El proceso general de wordcount se mira algo asi:

![fig1](/assets/img/labs/wordcount.png)

Ustedes tienen que lograr algo similar al ejemplo de arriba.

Para ver su respuesta:

```shell
$ make run-wordcount
```

Esto les va a generar una carpeta llamada wordcount-out, y su output va a estar en part-00000 verifiquen que se parezca a wordcount-expected que esta en la carpeta de archivos.

***

#### Ejercicio 3: Sort

En este ejercicio lo unico que tienen que hacer es copiar su codigo de wordcount y modificar una linea que indicamos en el archivo sort.py para que el output salga ordenado alfabeticamente.

Para correr su codigo:

```shell
$ make run-sort
```

Esto les va a generar una carpeta llamada sort-out, y su output va a estar en part-00000 verifiquen que se parezca a sort-expected que esta en la carpeta de archivos.
