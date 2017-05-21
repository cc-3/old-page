---
layout: post
title:  "Proyecto 4-2: MapReduce y AWS EC2"
date:   2017-05-20
category: proyecto
description: >
    En la parte 2 del proyecto 4 van a trabajar en el Amazon Elastic Cloud (EC2). Probarán su proyecto 4 con un set de imagenes más grande y verificarán como es el resultado (en tiempo).
permalink: /:categories/:title.html
---

## AWS EC2 y Spark

En esta parte del proyecto, vamos a utilizar el poder del Amazon Elastic Cloud EC2, para comprimir de manera más rápida. Vamos a estar utilizando una sola máquina con las siguientes características:

```shell

Tipo de instancia: R4

Descripción: Las instancias R4 estan optimizadas para aplicaciones que requieran utilizar
memoria de manera intensa y ofrecen un mejor precio por GiB de RAM

Características:

High Frequency Intel Xeon E5-2686 v4 (Broadwell) Processors
DDR4 Memory
Support for Enhanced Networking

61 GiB de memoria RAM
8 cores virtuales

Networking performance: hasta mas de 10 GiB

I/O performance: Alta

Nombre de API: r4.2xlarge
```

#### Preparando Su Cuenta


NOTA: Tienen que tener una cuenta de AWS antes de hacer esta parte.
Si ya tienen su cuenta de amazon pueden aplicar al AWS educate para que les acreditemos los US $100. Sigan los pasos que estan aqui:

1. Ingresar a: [AWS](https://aws.amazon.com/) y hacer login con su correo de galileo.
2. Al ingresar con su usuario, ir a "My Account" que se encuentra en la esquina superior derecha donde esta su nombre y anotar su "Account Id"
3. Ingresar a [AWS Educate](https://www.awseducate.com) y darle "Apply Now" y en la siguiente pagina dar click donde dice "Apply for AWS Educate for Students" algo como la Figura 1 tienen que tener
4. Si les sale algo que tienen que ingresar en algun lugar: course numbers and names o algo parecido escriban: CCIII

<img src="/assets/img/proj/educate1.png" style="display: block;margin: 0 auto;">

Primero necesitamos hacer un par de configuraciones para prepar su cuenta y poner a trabajar cosas en el EC2. Sigan estos pasos (del 1 al 6):

##### Paso 1

Métanse a su cuenta de AWS en el siguiente [link](http://aws.amazon.com/). Una vez dentro les va a aparecer algo como esto:

<img src="/assets/img/proj/aws1.png" style="display: block;margin: 0 auto;">

##### Paso 2

Den click donde dice EC2

<img src="/assets/img/proj/aws2.png" style="display: block;margin: 0 auto;">

##### Paso 3

Busquen donde dice Key Pairs

<img src="/assets/img/proj/aws3.png" style="display: block;margin: 0 auto;">

##### Paso 4

Hagan click donde dice Create Key Pair


<img src="/assets/img/proj/aws4.png" style="display: block;margin: 0 auto;">

##### Paso 5

Escriban MapReduceCC3 (Tiene que verse igual las mayúsculas importan) y denle click a create

<img src="/assets/img/proj/aws5.png" style="display: block;margin: 0 auto;">

##### Paso 6

Les va aparecer esto y va a bajar un archivo llamado MapReduceCC3.pem, guardenlo, cuidenlo, etc... en algun lugar donde puedan volver a acceder a el

<img src="/assets/img/proj/aws6.png" style="display: block;margin: 0 auto;">

#### Cómo correr el código en EC2

Una vez hayan configurando su cuenta en el AWS, vamos a enseñarles como tienen que probar su programa.

Primero describamos como su código va a correr en el EC2. A través del AWS vamos a rentar una computadora. En este caso no vamos a estar utilizando un cluster (un set de computadoras conectadas en una red local rápida) sino 1 sola computadora y será lo mismo que ejecutarlo en en su computadora, pero primero tienen que configurar la instancia como lo hicieron con su propia maquina.

Para hacer las cosas más fáciles decidimos hacer un video-tutorial de lo que tienen que hacer en este proyecto así que lo único que tienen que hacer es seguir paso a paso lo que ven en el video:

##### Tutorial:

##### Parte 1:

<video width="640" height="480" controls>
  <source src="/assets/img/proj/video1.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

##### Parte 2:

<video width="640" height="480" controls>
  <source src="/assets/img/proj/video2.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

##### Parte 3:

<video width="640" height="480" controls>
  <source src="/assets/img/proj/video3.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

***

#### Calificación y Entrega Final:

**FECHA: 4 Junio de 2017 11:55 PM**<br>

La entrega será por medio de **GES** (serán los mismos grupos asignados de la vez pasada) Tienen que subir su archivo test_output.zip

Cualquier duda que tengan por **SLACK**
