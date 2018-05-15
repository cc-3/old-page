---
layout: post
title:  "Proyecto 3: Map Reduce"
date:   2018-05-15
category: proyecto
description: >
    En proyecto van a convertir breadth-first-search (un algoritmo que visto en grafos al final de CC2) en un formato compatible con el framework de MapReduce (i.e. una función map y una función reduce) para resolver un puzzle.
---

#### Setup

Como siempre, hagan click en este [link](https://classroom.github.com/g/7-3CKK2U) para poder clonar los archivos necesarios para iniciar. Recuerden que tienen que subir su link al GES para poder tener su nota.

***

#### Información de Spark


##### Spark

En este proyecto utilizaran un cluster computing framework llamado Spark. Este framework nos da mas poder que las funciones map y reduce nativas de Python.

##### Como correr Spark vía Command Line:

Para este proyecto les vamos a proveer un script que los va a ayudar a correr sus archivos de Spark, pero cuando creen sus propios archivos (o usen Spark fuera de la clase, que la verdad deberían para aprovechar su computadora al 100%), van a necesitar saber como correr Spark vía command line. Para nuestra versión de Spark, para correr su archivo de Spark x.py (similar a como corren los archivos de Python, python x.py), solo tienen que correr el siguiente comando:

```shell
    $ spark-submit x.py # Corre el archivo spark x.py
```

Si sus archivos de Spark toman argumentos (como la mayoría de archivos que les proveímos), el comando va a ser similar, pero le van añadir cualquier cantidad de argumentos que necesiten, asi:

```shell
    $ spark-submit x.py arg1 arg2 # Corre el archivo de spark x.py y le pasa los argumentos arg1 arg2
```

Spark incluye un interprete que corre con Python y les va dejar testear cualquier comando de Spark ahí mismo. El interprete de Spark también permite recibir archivos de Spark (le pasan los archivos con la bandera --py-files) y entonces va a cargar los archivos que están en el mismo directorio donde se esta ejecutando). Si están buscando solo correr el interprete, el comando es el siguiente:

```shell
    $ pyspark # Corre el interprete de Spark.
```

Si ustedes quieren precargar algunos archivos (digamos a.py, b.py, c.py), pueden correr el siguiente comando:

```shell
    $ pyspark –py-files a.py, b.py, c.py # Corre el interprete de Spark y ahora pueden importar cosas de a,b y c.
```

##### Tips Rápidos para hacer debugging en Spark:

Si alguna vez se encuentran preguntándose porqué su output es raro o alguna cosa no sirve en sus archivos de Spark, recuerden estos pocos rápidos tips!

* Realicen pruebas en pyspark, hasta que sientan que ya casi está terminado todo usen spark-submit
* Hagan uso de la función take! La función take puede correr en cualquier objeto RDD (cualquier objeto que estén tratando de paralelizar o correr cualquier función de transformación/acción en el (van a leer de esto después)). Esta función toma un argumento N, que es un entero y va a returnar los primeros N elementos dentro de su objeto RDD. Para más información acerca de esto, vean la documentación de take.
* Ustedes también pueden probar sus funciones (map, reduce, etc) dentro del interprete de Spark (pyspark, mencionado arriba). Simplemente importen la función que quieren probar en pyspark (explicado arriba) y asi van a ser capaces de correr la funcion y verificar si su output es el esperado!.
* Documentación, y Recursos adicionales:

Un quickstart programming guide para Spark (hagan click al tab de Python para ver código de Python (no Scala, no Java)) esta disponible [aquí](http://spark.apache.org/docs/latest/programming-guide.html).

***

#### Problema a resolver: N-Puzzle  

Para este laboratorio ustedes van a resolver un PUZZLE, y en especifico la forma general de 15-puzzle que es n-puzzle. Si ustedes no conocen este juego, aquí hay un [link](http://mypuzzle.org/sliding) en donde pueden familiarizarse con el.

<img src="/assets/img/labs/puzzle.png" style="display: block;margin: 0 auto;">

Este puzzle tiene la característica de que uno puede llegar de cualquier posición (que claro esta es una configuración única del puzzle) hacia otra (aquí no hay callejones sin salida). Con esta característica es fácil construir un algoritmo que pueda generar todas las posiciones del juego y resolverlo.

##### Strongly Solving Puzzle

Ustedes van a escribir un breadth-first-solver que va empezar en la **SOLUCIÓN** (única) del juego y a partir de esta recorrer el grafo completo, tomando un registro de cada nueva posición del puzzle que se alcance, así como también de cuantos movimientos le tomo para llegar a esta posición (a esto le vamos a llamar level). El breadth-first-search original termina de buscar cuando encuentra una posición particular, ustedes sin embargo van a hacer un exhaustive search (i.e. recorrer TODO el grafo) y a esto se le llama strongly solving. Para hacer esto, vamos a mantener dos mappings (que en python van a representar diccionarios/hash tables).

* **pos_to_level**: dada una posición, ¿cuál es su nivel? (cuando terminen todo, este único mapping es el que les va a servir, porque esto lo van a escribir a un archivo de texto).
* **level_to_pos**: dado un nivel, ¿cuáles son todas sus posiciones? (Esto solo les va a servir en el proceso de resolver el puzzle, pero después de eso no lo van a necesitar).

Ustedes van a resolver la forma generalizada de 15-puzzle (n-puzzle), pero nosotros les vamos a dar el código que necesitan para este juego en particular. Como es la forma generalizada del puzzle, esto quiere decir que dado un alto y un ancho (i.e. filas y columnas) podemos formar un juego (e.g. 15-puzzle esta formado por 4 filas y 4 columnas). Para pequeños puzzle (pequeños valores de alto y ancho), debería ser fácil que ustedes puedan verificar si su output es correcto. Claro que pueden tratar con parámetros mas grandes, pero si tienen tiempo y espacio en el disco duro.

##### Breadth-First-Solver

Aquí hay un breadth-first-solver genérico escrito en Python. Toma como argumentos un puzzle y un **max_level**. El parámetro **max_level** es usado como un control de que tan lejos el algoritmo debería de llegar en cuanto a nivel (si se deja el valor -1, el algoritmo debería de visitar cada posición en el grafo del puzzle). El parámetro puzzle es un objeto que tiene 2 importantes métodos.

* **children()**- que retorna una lista de todas las posiciones cercanas.
* **solution()**- que retorna la única solución del puzzle.

```python
level_to_pos = {}
pos_to_level = {}

def solve(puzzle, max_level=-1):
    """BF visita el grafo del puzzle completamente, construyendo las estructuras level_to_pos y pos_to_level"""

    solution = puzzle.solution()
    level = 0
    level_to_pos[level] = [solution] ### el level 0 consiste en la solucion unica
    pos_to_level[solution] = level
    ### Mientras hayan posiciones en el level actual
    while level_to_pos[level] and (max_level==-1 or level < max_level):
        ### Aumentamos el level, por lo que el level actual cambia
        level += 1
        level_to_pos[level] = []
        ### Para cada posicion en el level anterior al actual (porque cambio)
        for position in level_to_pos[level-1]:
            ### Para cada hijo en esa posicion
            for child in position.children():
                ### Si es primera vez que se ha visto al hijo
                if child not in pos_to_level:
                    ### Actualizar los mappings
                    pos_to_level[child] = level
                    level_to_pos[level].append(child)
    del level_to_pos[level] ### El ultimo level siempre esta vacio, asi que lo borramos.
```

##### Empezando

El puzzle que vamos a resolver consiste en piezas enumeradas ordenadas aleatoriamente, faltando una de ellas. El objetivo del juego es poner las piezas en orden como se muestra en la figura de abajo, para el caso de ancho 3 y altura 3 (3x3).

<img src="/assets/img/labs/solving.png" style="display: block;margin: 0 auto;">

En la carpeta del archivos base encontrarán lo siguiente:

* **Makefile**: archivo que define configuraciones para correr su programa (tamaño del sliding puzzle y el nivel de paralelismo a utilizar). Miren este archivo para ver como se corren los programas en Spark. Tiene info de como pueden probarlo en sus compus. Tambien define como probar su codigo para ver si es correcto.
* **Sliding.py**: implementación del juego sliding-puzzle.
* **check.py**: script para verificar si su output es correcto (funciona con make check)
* **SlidingBfsReference.py**: el algoritmo bfs genérico antes mencionado. Pueden usar este codigo para verificar si su respuesta producida por MapReduce es correcta.
* **SlidingBfsSpark.py**: El archivo que tienen que modificar. (Aquí van a poner su solucion de MapReduce)
* **ref_out**: una carpeta que contiene una salida de referencia de lo que se espera en un juego de 2x2. y un resultado de hacer make check
* **expected**: una carpeta que contiene las respuestas correctas de todas las pruebas (small-puzzle-expected.txt, medium-puzzle-expected.txt y large-puzzle-expected.txt)

##### Su trabajo

Su tarea es implementar un MapReduce iterativo que sea capaz de resolver el Sliding puzzle general.

Como mencionamos arriba, el MapReduce que van a implementar va a tomar como entrada un ancho y un alto describiendo el Sliding puzzle. Usando la solución de ese puzzle, repetidamente va ir expandiendo el árbol del BFS, y generando un mapping entre cada posición y nivel en donde esta en el árbol del BFS. Nosotros representamos el Sliding puzzle como una tupla de strings de Python. Cada pieza se representa con un carácter del alfabeto y la pieza que hace falta con un guión. Después de correr su implementación de MapReduce, esperamos que su programa produzca un archivo de texto de la siguiente forma. (por ejemplo, para el caso de un sliding-puzzle de 2x2).

0 ('A', 'B', 'C', '-')<br>
1 ('A', '-', 'C', 'B')<br>
1 ('A', 'B', '-', 'C')<br>
2 ('-', 'A', 'C', 'B')<br>
2 ('-', 'B', 'A', 'C')<br>
3 ('B', '-', 'A', 'C')<br>
3 ('C', 'A', '-', 'B')<br>
4 ('B', 'C', 'A', '-')<br>
4 ('C', 'A', 'B', '-')<br>
5 ('B', 'C', '-', 'A')<br>
5 ('C', '-', 'B', 'A')<br>
6 ('-', 'C', 'B', 'A')<br>

##### Recomendaciones para empezar:

* Vean la implementación que esta en **SlidingBfsReference.py**, traten de entenderla y como es que funciona. Hagan una lluvia de ideas de como pueden traducir esto a un modelo compatible con el MapReduce framework.
* Su código no se tiene que ver en nada igual a la implementación que esta en el SlidingBfsReference.py
* En vez de los diccionarios pos_to_level y level_to_pos, van a tener que mantener la información en un Spark RDD que contenga pares (key, value).
* Lean la sección de “Notas de Spark” y revisen la documentación de Spark para estar familiarizados con las herramientas que pueden utilizar.
* Implementen una buena solución que sea razonablemente eficiente para por lo menos los casos de 2x2 y 3x3.
* Recuerden que deben utilizar varias funciones (No hagan todo en una).
* Antes de empezar a codear, verifiquen bien que es lo que le van a mandar a las funciones que definen (i.e. que key y que value quieren utilizar).
* No se olviden que la función de Reduce, generalmente agrupa el dataset por keys y Spark provee funciones para realizar esta tarea fácilmente en un RDD.

##### Para probar su algoritmo

**make run-small**

Esto va a probar su implementacion con un tablero de 2x2, y les va a generar un archivo llamado small-puzzle-out.txt.

**make run-medium**

Esto va a probar su implementacion con un tablero de 3x3, y les va a generar un archivo llamado medium-puzzle-out.txt.

**make run-large**

Esto va a probar su implementacion con un tablero de 5x2, y les va a generar un archivo llamado large-puzzle-out.txt.

**make check**

Esto va a probar su codigo con los tres tableros de arriba verificando si la respuesta es igual a la esperada. Esto les va a generar un archivo llamado resultados.txt, ese archivo tiene info de porque fallaron asi pueden ver más rapido que estan haciendo mal. Si tienen todo bien el resultado les deberia de salir algo asi:

```
Tablero de: 2x2
-----------------
Tiempo: 4.81 segundos
La cantidad de lineas de su respuesta es correcta
Su respuesta hace match con la nuestra (es igual)
All Ok


Tablero de: 3x3
-----------------
Tiempo: 12.97 segundos
La cantidad de lineas de su respuesta es correcta
Su respuesta hace match con la nuestra (es igual)
All Ok


Tablero de: 5x2
-----------------
Tiempo: 124.15 segundos
La cantidad de lineas de su respuesta es correcta
Su respuesta hace match con la nuestra (es igual)
All Ok
```

#### Entrega

La entrega de este proyecto se realizará después de terminados los exámenes finales. Favor estar atentos a Slack y su correo para ver fechas y horarios.
