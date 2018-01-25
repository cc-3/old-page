---
layout: post
title:  "Proyecto 4: MapReduce"
date:   2017-04-17
category: proyecto
description: >
    El objetivo del último proyecto de CC3 es que ustedes se familiaricen con el modelo de programación de MapReduce haciendo una aplicación que sea capaz de comprimir imágenes y videos utilizando DCT.
permalink: /:categories/:title.html
---

### Objetivo

El objetivo de este proyecto es que ustedes se familiaricen con el modelo de programación de MapReduce usando el framework de Apache Spark (que van a ver en un laboratorio). En la primer parte del proyecto ustedes van a tener la oportunidad de convertir un algoritmo secuencial de compresión de imágenes en un formato compatible con el framework de MapReduce (i.e. una función map, una función reduce y otras más). En la segunda parte se va a requerir que corran su implementación en un gran cluster de servidores de AWS EC2, para lograr abordar un mayor problema, pero más que eso para que aprendan como pueden utilizar AWS EC2 con Apache Spark.

Esperamos que haciendo este proyecto ustedes adquieran una habilidad de programación BASTANTE útil, además de que puedan poner en práctica lo aprendido en clase en el tema de data level parallelism (DLP).

#### Comenzando

Creen su repositorio de GitHub utilizando el siguiente link de **GitHub ClassRoom**: [link](https://classroom.github.com/group-assignment-invitations/8c9be748835d3e24e225a99c9af48148) con esto primero crearan su grupo de trabajo y segundo obtendran los archivos necesarios para hacer el proyecto.

#### GRUPOS

Por favor tienen que llenar este [Sheet](https://docs.google.com/spreadsheets/d/1x9nlE58BtS659zv3Xj_jAL30JtowkTdbsJI62kH8WOU/edit?usp=sharing) de google docs donde indiquen los integrantes del grupo (Nombre y Carnet), Seccion, y Nombre del grupo de GitHub es necesario que hagan esto para que la calificación sea más fácil y rápida. Recuerden que si no se anotan en este Sheet tienen 0 automaticamente.

#### Documentacion y Guia de Programación

Si no están familiarizados con Spark, pueden leer esta [guía de programación](http://spark.apache.org/docs/latest/programming-guide.html), especialmente tienen que ponerle atención a la sección que habla de los Resilient Distributed Datasets (RDDs) y las operaciones que se pueden hacer sobre un RDD.

Nota: cuando vean la guia de programación recuerden siempre ponerse en la pestaña que dice "Python"

La documentación de **Spark** es la siguiente: [Docs](http://spark.apache.org/docs/latest/)

#### Instalando Spark y Anaconda

Como tenemos que usar diferentes herramientas (librearias de Python) vamos a utilizar **Anaconda Python**. Anaconda instala todas las librerias necesarias de Python para este proyecto asi como el interprete más reciente de Python 2.7. Para instalar Anaconda solo tienen que hacer lo siguiente en una terminal

```shell
$ wget https://repo.continuum.io/archive/Anaconda2-4.3.1-Linux-x86_64.sh
$ bash Anaconda2-4.3.1-Linux-x86_64.sh
```

Cuando empiece el instalador ustedes le dan "yes" a todo y por ultimo tienen que hacer un source al .bashrc


```shell
$ source ~/.bashrc
```

Ya que tienen anaconda pueden probar lo siguiente y les deberia de dar el mismo resultado o parecido

```shell
$ python
Python 2.7.13 |Anaconda 4.3.1 (64-bit)| (default, Dec 20 2016, 23:09:15)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>>
```
ya teniendo eso lo que tienen que hacer es instalar todas las librearias utilizando anaconda

```shell
$ conda install pip
$ pip install pillow
$ conda install -c menpo opencv3=3.1.0
$ conda install -c menpo ffmpeg=3.1.3
$ pip install -i https://pypi.anaconda.org/pypi/simple moviepy
```

Con esto ya tienen todo lo necesario de python ahora toca instalar Spark si es que no lo tienen aun en sus computadoras para eso tienen que hacer lo siguiente:

```shell
# descargamos spark
$ wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
# hay que descomprimir el archivo
$ tar -xzvf spark-2.1.0-bin-hadoop2.7.tgz
# movemos la carpeta a home y le cambiamos de nombre a "spark"
$ mv spark-2.1.0-bin-hadoop2.7 ~/spark
# editamos el PATH en .bashrc
$ echo export\ PATH=~/spark/bin:\$PATH >> ~/.bashrc
# hacemos source al .bashrc
$ source ~/.bashrc
# listo ya tienen spark en sus computadoras con Ubuntu, para probar que funciona
$ spark-submit
```
Con esto si les salio todo bien ya tendrían todo lo necesario para trabajar en el proyecto


<img src="/assets/img/proj/python_terminal.png" style="display: block;margin: 0 auto;">

<img src="/assets/img/proj/spark_submit.png" style="display: block;margin: 0 auto;">

#### Background

Siempre han habido una gran gama de métodos de compresión de videos y esto se ha creado con el fin de adaptar los videos de una manera que sea más facil renderizarlos en dispositivos que no tienen tanto poder de computo y memoria. Nosotros vamos a implementar un esquema usando **Discrete Cosine Transform (DCT)** para comprimir videos. Esta compresión _"con perdidas"_ es usada habitualmente en conjunto con métodos de compresión _"sin perdidas"_ para comprimir archivos de videos. Para el propósito de este proyecto, nosotros solo nos vamos a enfocar en la parte de compresión _"con perdidas"_.

#### Compresión utilizando DCT

DCT ([Discrete Cosine Transformation](https://en.wikipedia.org/wiki/JPEG#Discrete_cosine_transform)) es una transformación usada en las imágenes que tienen formato JPEG y es comúnmente utilizada para diferenciar puntos de datos en términos de diferentes frecuencias, siendo así facil de descartar aquellos (puntos) que tienen una frecuencia muy alta y de esta manera podemos bajar la cantidad de espacio necesario para guardar la imagen. La idea detrás de esto es que los componentes que tienen una frecuencia muy alta en las imagenes no son reconocibles por el ojo humano debido a que se tiene una disminución de la sensibilidad en la percepción de dichas frecuencias (e.g ustedes pueden identificar una sombra de rojo como rojo, pero probablemente no tan facilmente puedan identificar el color ["American Rose"](https://en.wikipedia.org/wiki/Category:Shades_of_red) como algo distinto de rojo). Entonces, estos componentes que tienen una frecuencia alta, pueden ser descartados, y de hecho se descartan frecuentemente en la fase de post-edición, para guardar la imagen con una pequeña perdida en la calidad. Veamos un ejemplo de una imagen no comprimida y otra si:

##### Imagen No Comprimida

<img src="/assets/img/proj/test1.jpg" style="display: block;margin: 0 auto;">

##### Imagen Comprimida

<img src="/assets/img/proj/naive_QF33_test1.jpg" style="display: block;margin: 0 auto;">

Seguramente para ustedes NO hay diferencia !!!! y está comprimida en un 22% del tamaño original, para hacer imagenes JPEG (que ya estan comprimidas) no está nada mal...

#### Compresión de Videos

Los videos son típicamente representados como una secuencia de **frames**, y a estos frames son los que se le aplican los metodos de compresión _"con perdida" y "sin perdida"_, dentro de los métodos _"con perdida"_ en la práctica se utiliza **DCT**.

#### Matriz de Cuantización

La matriz de cuantización es la porción que realmente es utilizada durante la compresión _"con perdida"_ para quitar, cortar, descartar, etc las partes menos notables de una imagen. Como se menciono arriba, debido a que la percepción visual del ojo humano solo es capaz de percibir frecuencias bajas bastante bien, las frecuencias altas simplemente las podemos ignorar, descartar en este caso.

#### Python

Para este proyecto se requiere que tengan conocimientos de programación en el lenguaje **Python**, como este lenguaje es fácil de aprender y es casi como pseudocódigo no vamos a enseñarlo durante los periodos de clase ya que pueden aprenderlo siguiendo este tutorial que nosotros preparamos para ustedes: [TUTORIAL DE PYTHON](http://cc-3.github.io/tutorial/tutorial-python.html)

Si siguen el tutorial y lo entienden ya tendran todo lo que necesitan saber de python para concluir el proyecto a la perfección.

#### Herramientas

Como herramienta principal vamos a estar utilizando Spark MapReduce y python. Pero también los vamos a dejar (y les recomendamos bastante) que utilicen herramientas como [OpenCV](http://opencv.org/) y [NumPy](http://www.numpy.org/) (librerias de python que ya están optimizadas para el manejo de arreglos con multiples dimensiones). Tengan siempre en mente que el procesamiento de las imágenes (el algoritmo de procesamiento) no es el objetivo principal del proyecto asi que por estas razones los vamos a estar dejando utilizar este tipo de herramientas para simplificar algunos aspectos. El proyecto deberia de estar construido de tal manera que se note que estan familiarizados con estas herramientas pero no necesariamente (e.g. hay funciones de ayuda que pueden encontrar en helper_functions.py que ya hacen casi todo lo que necesita NumPy y OpenCV).

#### Algoritmo de Compresión

```python
def naive_compress(image):
    # Hace que la imagen tenga dimensiones que sean multiplos de 8
    image = truncate((None, image))[1]
    # cambiamos el espacio de color de la imagen a YCrCb
    Y, crf, cbf = convert_to_YCrCb(image)
    # guardamos cada canal en un arreglo
    channels = [Y, crf, cbf]
    # obtenemos el width y el height de la imagen
    height, width = np.array(image.shape[:2])
    # creamos una matriz donde vamos a guardar el resultado
    reimg = np.zeros((height, width, 3), np.uint8)
    # recorremos cada canal
    for idx, channel in enumerate(channels):
        # calculamos cuantos bloques tenemos para agarrar
        no_rows = channel.shape[0]
        no_cols = channel.shape[1]
        # creamos un arreglo del tamaño del canal
        dst = np.zeros((no_rows, no_cols), np.float32)
        no_vert_blocks = no_cols / b_size
        no_horz_blocks = no_rows / b_size
        # para cada bloque aplicamos la transformacion y la guardamos
        for j in range(no_vert_blocks):
            for i in range(no_horz_blocks):
                i_start = i * b_size
                i_end = (i + 1) * b_size
                j_start = j * b_size
                j_end = (j + 1) * b_size
                # agarramos un bloque
                cur_block = channel[i_start : i_end, j_start : j_end]
                # hacemos el dct de un bloque primero centrando los datos
                dct = dct_block(cur_block.astype(np.float32) - 128)
                # matriz de cuantizacion
                q = quantize_block(dct, idx==0, QF)
                # inversa
                inv_q = quantize_block(q, idx==0, QF, inverse = True)
                # inversa de la inversa
                inv_dct = dct_block(inv_q, inverse = True)
                # guardamos el resultado
                dst[i_start : i_end, j_start : j_end] = inv_dct
        # volvemos a los valores originales
        dst = dst + 128
        dst[dst>255] = 255
        dst[dst<0] = 0
        # ponemos el tamaño original
        dst = cv2.resize(dst, (width, height))
        # guardamos en el idx
        reimg[:,:,idx] = dst
    # devolvemos la imagen nuevamente cambiando el espacio de color
    return cv2.cvtColor(reimg, ycrbr2bgr)
```

todos los pasos de este proyecto y la compresión de imágenes JPEG están explicadas perfectamente en el siguiente [link](https://en.wikipedia.org/wiki/JPEG#Encoding). Para este proyecto vamos a olvidar la compresión _"sin perdida"_, asi que a lo único que le tienen que poner atención es a las partes de compresión _"con perdida"_. Los pasos principales son los siguientes:

1. Cargar un set de imágenes.
2. Convertir cada imagen del espacio de color BGR al [espacio de color YCbCr](http://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#void cvtColor(InputArray src, OutputArray dst, int code, int dstCn)).
3. Aplicar [DCT](http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=dct#cv2.dct) y [Cuantización](https://en.wikipedia.org/wiki/JPEG#Quantization) a un sub-bloque de 8x8 de cada parte de cada imagen.
4. Aplicar la [De-Cuantización](https://en.wikipedia.org/wiki/JPEG#Quantization) y la [Inversa DCT](http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=dct#cv2.dct) a un subbloque de 8x8.
5. Regresar cada bloque a su lugar correspondiente
6. Generar un set de imagenes procesadas

Las imágenes van a ser cargadas utilizando funciones de las librerias arriba mencionadas. Van a ser una lista de pares key value (id_imagen, imagen). Ustedes no se van a tener que preocupar sobre los detalles de como esto está hecho pero siempre pueden revisar el código base para tratar de entender. Dentro de la función run(images), hemos inicializado un RDD de Spark para ustedes.

#### Su tarea

La primer cosa que tienen que realizar es la de convertir todas sus imagenes al espacio de color YCbCr. Les damos una función de ayuda que convierte una imagen a color a YCbCr en helper_functions.py. Esta función devuelve 3 matrices, la primer matriz es el canal Y (iluminación) de la imagen de entrada, la segunda matriz y tercera son muestras de los canales cromáticos Cr y Cb. En este punto su RDD debería de tener un tamaño 3 veces mayor al numero de entradas.

Lo siguiente que tienen que hacer es crear los pequeños "sub-blocks" de 8x8 también llamados macroblocks para cada una de las matrices, y este tamaño de bloque es el que vamos a utilizar siempre para las transformaciones. Piensen que tienen que poner en su pares **key** y **value** para que puedan volver a poner los bloques de vuelta en su lugar más adelante. **Hint: Recuerden, ustedes pueden tener varias cosas en el key o en el value utilizando tuplas de python.**

Una vez de que tengan un RDD con todos los sub-blocks, tienen que aplicar las siguientes transformaciones en el siguiente orden: DCT (primero haciendo que el bloque tenga rango de pixeles entre [-128, 127] y no de [0, 255] como dice el algoritmo), Cuantización. De-Cuantización, Inversa DCT. La mayoria del codigo para estas transformaciones ya estan en **helper_functions.py**. Pongan todas sus energias en como pueden aplicar estas transformaciones a todos los sub-blocks de una manera más eficiente (claro siempre usando MapReduce no?). Cada una de las funciones toma un bloque como entrada y devuelve un bloque transformado. Como se menciono anteriormente, cuando ustedes aplican DCT, tienen que substraer de cada elemento del bloque 128 de antemano para asegurar que los valores de los pixeles esten dentro del rango [-128, 127] (cambiando de un rango inicial que es de [0, 255]). Entonces también tienen que sumar 128 a cada bloque despues de que aplican la inversa DCT.

Finalmente, queremos poner cada sub-block donde corresponde y obtener la imagen (comprimida) de regreso. Primero, tienen que asegurar que todos los elementos esten dentro del rango de pixeles de 0 a 255 (es el único rango valido para guardar imágenes). Entonces, piensen en como pueden combinar los bloques utilizando una función reduc y despues escriban una función mapper de función que llene la matriz con el sub-block correcto. Van a encontrar la función de NumPy [np.zeros((num_rows, num_cols)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html), dtype='uint8') útil como un punto de partida para la matriz que quieren retornar. Finalmente, ustedes van a querer poner una matriz 3D para representar la imagen en el espacio de color YCrCb. Esta matriz va a ser del mismo tamaño que np.zeros((height, width), dtype='uint8'), en donde height y width van a ser obtenidos de la imagen original. Ahora pueden convertir la imagen de vuelta al espacio de color RGB. Intenten utilizar [cv2.imwrite(filename, image_matrix)](http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=imread#bool imwrite(const string& filename, InputArray img, const vector<int>& params)) si ustedes quieren ver la imagen procesada en cualquier momento.

Como resumen de lo que tienen que hacer: tienen que tomar el algoritmo secuencial que les damos y convertir cada una de sus partes en una funcion map y reduce.


#### Cómo es que estan las imágenes almacenadas

Las imágenes están almacenadas como arreglos 3D de NumPy una vez hayan sido cargadas. Tienen un "shape" o dimensiones (height, width, depth), donde height es cuantas filas tiene la imagen, width cuantas columnas tiene la imagen, y depth cuantos canales tiene en este caso 3 porque cada imagen tendrá 3 diferentes canales en el espacio de color de entrada. Si ustedes tuvieran una matriz img en el espacio de color YCrCb, la manera de indexing es como lo siguiente:

```python
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED) # carga la imagen (la carga en el espacio de color BGR)
image = cv2.cvtcolor(image, cv2.COLOR_BGR2YCrCb) # la convierte a YCrCb, hay una función de ayuda para esto
Y = image[:,:,0]  # todas las filas y columnas del canal 0
Cr = image[:,:,1] # todas las filas y columnas del canal 1
Cb = image[:,:,2] # todas las filas y columnas del canal 2

Y.shape # esto devuelve una tupla (height, width) porque Y es una matriz 2D ahora
sublock = Y[16:24, 32:40] # un subblock de 8x8 empezando en la fila 16 y la columna 32 de Y

# construyendo una copia de la imagen original y sus tres canales (YCbCr)
image_copy = np.zeros((image.shape[0], image.shape[1], image.shape[2]))
image_copy[:,:,0] = Y
image_copy[:,:,1] = Cr
image_copy[:,:,2] = Cb
```

#### Notas Importantes

* Solo vamos a aceptar que modifiquen el archivo **spark_image_compressor.py**. Ningún cambio se deberia de hacer a otro archivo de python del proyecto. No seguir esta instrucción es automaticamente un 0 como nota. No se van a aceptar excusas.
* Si suben su proyecto utilizando **naive_compress** es decir, de forma serial y no con MapReduce, van a tener 0 como nota.
* Solo como referencia, la solución es de aproximadamente 90 lineas de codigo. Utilizando cosas que estan en **helper_functions.py** puede disminuir la cantidad de codigo que van a escribir.

#### Pruebas y Check

Para probar su algoritmo pueden hacerlo de 3 formas

##### Utilizando Check

```shell
# ustedes deberian de cambiar threads al numero del threads que tiene su procesador
$ spark-submit check.py --threads 8
```

lo que hace es correr su algoritmo con 100 imagenes random y guardar el resultado en un archivo de texto y compararlo con una referencia que nosotros les damos que esta en la carpeta **ref-out**, no crean que porque son random siempre van a salir valores diferentes ya que hemos puesto un **seed** de 1 para que todos siempre tengan el mismo resultado.

##### Utilizando Image Diff

Primero que nada para hacer esto ustedes lo que tienen que hacer es correr su programa de la siguiente manera:

```shell
# ustedes pueden cambiar input a otra imagen que este en test
# QF lo pueden cambiar a valores de 99, 66 y 33
# threads lo tienen que cambiar al numero de threads de su computadora
$ spark-submit run_spark_compressor.py --input test/test1.jpg --QF 33 --threads 8
```

esto les va a generar una imagen (llamada spark_QF33_test1.jpg) en la carpeta de su proyecto y para compararla con su referencia tienen que hacer lo siguiente (en el caso de QF=33)

```shell
$ python image_diff.py --input1 ref-out/naive_QF33_test1.jpg --input2 spark_QF33_test1.jpg
Images match
```
Si les sale "Images match" entonces está bien su algoritmo


##### Utilizando un video

Para esto realmente lo único que tienen que hacer es lo siguiente:

```shell
$ spark-submit run_spark_compressor.py --input test/video.mp4 --QF 33 --threads 8 --video
```

Si el video comprimido tiene un menor tamaño entonces están haciendo las cosas bien


#### Entrega

**FECHA: 9 Mayo de 2017 11:55 PM**<br>

La entrega será por medio de **GitHub** pero tienen que subir su link de su repositorio al GES recuerden tambien llenar el **Sheet** de google docs y el grupo es de máximo 2 integrantes.

Cualquier duda que tengan por **SLACK** a **andres**
