# Lab 0 - Git y Representación de Números

## Objetivos

* Aprender git y crear cuenta de GitHub.
* Ganar más intuición para trabajar con números binarios.

## Lecturas

![PH](/img/PH.jpg)

* P&amp;H: 2.4

## Ejercicio 1: Cuenta de GitHub

Por favor lee las siguientes instrucciones cuidadosamente antes de seguir con el laboratorio. La mayor parte de los problemas que tienen los estudiantes durante este laboratorio se pueden prevenir siguiendo atentamente los pasos que se indican.

Para este curso necesitaremos que uses **git**, un _sistema de control de versiones distribuido_. Los sistemas de control de versiones son las mejores herramientas para compartir y almacenar código a comparación de mandar correos con archivos adjuntos, utilizar memorias flash, o incluso compartir documentos mediante DropBox o Google Docs.

Vamos a estar usando **GitHub** para tener repositorios privados en donde van a _almacenar_ su código remotamente. Si la oración anterior no te dijo nada, no te preocupes vamos a guiarte en el proceso más adelante. Pero primero, necesitas crear una cuenta de **GitHub**.

¿Por qué GitHub? GitHub ahora le permite a todas las cuentas gratuitas tener repositorios privados ilimitados con algunas limitaciones que no van a ser ningún problema para nosotros.

### GitHub y Primer Repositorio

Navega a la siguiente página: [github.com](https://github.com/)

1. Si no tienes una cuenta de GitHub todavía, crea una en el siguiente [link](https://github.com/join/).
2. Crea un repositorio privado vacío, llamado lab0_git
    * Primero haz click en el siguiente [link](https://github.com/new/)
    * Luego llena los campos como se muestra la siguiente imagen

![crear repo](/img/labs/lab00/repo_es.png)

### Configurando git

Ahora que ya hemos creado nuestro repositorio, vamos a configurar git para que sepa quien eres. Abre una terminal <kbd>ctrl</kbd><kbd>alt</kbd><kbd>t</kbd> y ejecuta los siguientes comandos listados abajo, reemplazando **TU_NOMBRE** con tu nombre y apellido (entre comillas) y **TU_CORREO** con la dirección de correo que utilizaste para registrarte en GitHub.

```shell
git config --global user.name "TU_NOMBRE"
```

```shell
git config --global user.email "TU_CORREO"
```

## Ejercicio 2: git y Remotes

Primero, algunas definiciones rápidas:

* Un **remote** es la página web host o servidor que va a almacenar tu código remotamente en vez de tener únicamente tu código de forma local en tu propia computadora. Puedes pensar en esto de igual manera a como se almacena un archivo en DropBox o Google Drive pero con el poder que nos da git.

* Un **branch** es una secuencia (por aparte) de diferentes cambios a tu código. Puedes pensar en los _branches_ como diferentes versiones de tu codigo, que en algún punto fueron lo mismo. La siguiente figura muestra a que nos referimos como branches.

![branch](/img/labs/lab00/branch.svg)
<p align="center">_(créditos de imagen: BitBucket)_</p>

A lo largo de este curso, estarás trabajando en dos diferentes "_computadoras_" que generalmente tendran diferentes versiones de tu código en algún tiempo. Estas dos son: tu computadora personal y tu remote de GitHub (tus repositorios privados de GitHub). Es esencial que entiendas la diferencia entre estas dos y como puedes compartir código entre ellas.

1. Tu **computadora personal** es la que te servirá para hacer todo el trabajo (laboratorios y proyectos) que necesites hacer durante el curso, nada nuevo aquí.
2. Tu cuenta de GitHub y los **remotes** te servirán para muchos propósitos, pero la principal razón es para tener un backup o copia de respaldo, de tal manera que si algo malo le sucede a tu computadora (esperamos no <i class="em em-wink"></i>), puedas recuperar tu código en vez de empezar desde cero nuevamente. Conceptualmente, puedes pensar en los remotes de GitHub como otra computadora que únicamente almacena tu código y nada más. Siempre debes subir tus cambios hacia GitHub haciendo _push_ al remote (es decir actualizarás los archivos en GitHub) y también descargarás los cambios de GitHub haciendo _pull_ (actualizando los archivos en tu computadora personal).

### Obteniendo los Archivos

Crea una carpeta llamada `lab0_git` en algún directorio de tu preferencia.

```shell
mkdir lab00_git
cd lab00_git
```

Luego descarga los archivos base de la siguiente manera:

```shell
git remote add lab0-starter https://github.com/cc-3/lab0_git.git
git fetch lab0-starter
git merge lab0-starter/master -m "agregando codigo base, lab 0"
```

Deberías de ser capaz de ver los archivos del laboratorio si los listas en la terminal:

```shell
ls
```

Lo cual desplegará lo siguiente:

```shell
```

### Haciendo push hacia GitHub

Ahora vamos a hacer _push_ del código hacia el repositorio privado de GitHub que creamos anteriormente, ejecutando los siguientes comandos, pero estando en la carpeta que acabamos de crear `lab0_git`:

```shell
git remote add origin https://github.com/USUARIO/lab0_git.git
git push -u origin master
```

> **NOTA**: _Tienes que cambiar USUARIO por tu usuario de GitHub_.

Ahora que tenemos nuestro laboratorio almacenado en GitHub (puedes verificar esto navegando hacia https://github.com/USUARIO/lab00_git.git), podemos agregar un archivo y hacer algunos _commits_. Vamos a crear un archivo llamado `hello.sh` en la carpeta del laboratorio ejecutando los siguientes commandos en la terminal:

```shell
echo 'echo "Hola Mundo"' > hello.sh
```

Luego puedes correr el archivo en la terminal con `bash hello.sh`. En la terminal se imprimirá `Hola Mundo`. Ahora utilicemos git para ver los archivos que todavía no han sido rastreados utilizando `status`:

```shell
git status
```

Lo que producirá lo siguiente:

```shell
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  hello.sh

nothing added to commit but untracked files present (use "git add" to track)
```

Esto es porque hemos creado u archivo nuevo llamado `hello.sh` y no lo hemos agregado. Podemos agregarlo y hacer commit:

```shell
git add hello.sh # agrega el archivo hello.sh para hacer commit
git commit -m "Mensaje del Commit" # ingresa cualquier mensaje que quieras
git branch # deberias de ver que solo existe el branch master y que estas en ella (*)
git push -u origin master # Esto hace push de tu codigo hacia GitHub (lo puedes ver en GitHub ahora)
```

El control de versiones git esta construido alrededor de _commits_, o _checkpoints_ en el desarrollo de diferentes versiones/etapas de tu código. Para explicar los pasos de arriba un poco más:

* **git add [archivo]** le dirá a git que has hecho cambios a ese archivo y que quieres que esos cambios se guarden en el siguiente commit (staging).
* **git commit -m "mensaje"** oficialmente guarda esos cambios que acabas de agregar, y crea un _snapshot_ del contenido actual de todos los archivos en el repositorio. Ahora siempre vas a tener la opción de revertir tu código hacia este commit.
* **git push -u origin master** manda todo el contenido del repositorio que está en el branch "master" al repositorio remoto "origin" (recuerda que agregamos el repositorio de GitHub "lab0_git" como remote y lo llamamos "origin").

Cuando estamos trabajando con git, si alguna vez no estas seguro de algo, pero quieres asegurarte de que tienes una copia guardada del contenido actual de tu código, solo tienes que correr `git add .` y después `git commit` en la terminal.

Un último comando de git que puedes encontrar bastante util es `git log`. Puedes ejectuar este comando en la terminal y vas a ver un historial o log de todos los commits que se han hecho (en el branch actual), incluyendo el tiempo y quien hizo el commit.

## Ejercicio 3: Alfabeto Binario

Vamos a utilizar números de 4 bits. Si apilamos cinco números de 4 bits uno encima de otro en binario, podemos crear patrones e imágenes. Para ayudarte a visualizar esto, puedes pensar que un bit en cero es blanco y un bit en uno es negro. Por ejemplo mira el siguiente patrón de bits.

<p align="center"><img src="/img/labs/lab00/ex3.png" alt="Patron de Bits"/></p>

### Preguntas

1. ¿Cuáles son los cinco números en decimal (separados por una coma) que producen el patrón de arriba?
2. ¿Cuáles son los cinco digitos en hexadecimal (separados por una coma) que producen el patrón de arriba?
3. ¿Qué letra se dibuja con los siguientes números en decimal: 1,1,9,9,6?
4. ¿Qué letra se dibuja con el siguiente numero en hexadecimal: 0xF8F88?
5. ¿Cuál es el numero en hexadecimal para dibujar la letra B?
6. ¿Utilizarías cinco dígitos hexadecimales para dibujar la letra N? Contesta Si o No

En los archivos del laboratorio vas a encontrar un archivo de texto `ex3.txt` con lo siguiente:

```
1:
2:
3:
4:
5:
6:
```

En este archivo tienes que colocar todas tus respuestas de las preguntas de arriba siguiendo ese formato por ejemplo un archivo valido sería:

```
1:1,2,3,4,5
2:0x1,0x2,0x3,0x4,0x5
3:A
4:A
5:0xcafee
6:Si/No
```

Si ya contestaste todo y crees que esta correcto puedes agregar los cambios, hacer commit y subirlo al repositorio remoto ejecutando los siguientes comandos en la terminal:

```shell
git add ex4.txt
git commit -m "ex. 3 complete"
git push -u origin master
```

## Ejercicio 4: 1,000 billetes de $1

Imagina que tienes mil billetes de $1 y 10 sobres. Para este ejercicio tienes que encontrar una manera de poner una cantidad determinada de billetes de $1 en cada uno de los sobres de tal forma que sin importar la cantidad de dinero que se te pida (entre $1 y $1000), simplemente entregues una combinación de los sobres y que siempre estés seguro de que estas dando la cantidad correcta.
En los archivos del laboratorio hay un archivo de texto llamado `ex4.txt` en donde encontrarás lo siguiente:

```text
a,b,c,d,e,f,g,h,i,j
```

Cada una de las letras representa un sobre, tienes que reemplazar cada letra por la cantidad de billetes de $1 que creas correcta, esa cantidad tiene que ser `>= 0` (en decimal) y recuerda que la suma de la cantidad de cada uno de los sobres tiene que ser igual a `1000`.

Si ya contestaste todo y crees que esta correcto puedes agregar los cambios, hacer commit y subirlo al repositorio remoto ejecutando los siguientes comandos en la terminal:

```shell
git add ex4.txt
git commit -m "ex. 4 complete"
git push -u origin master
```

## Calificación

Si ya completaste el laboratorio puedes subirlo para calificación

```shell
./submit
```
