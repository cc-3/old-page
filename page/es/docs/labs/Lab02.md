# Lab 2 - C Avanzado y Manejo de Memoria

## Objetivos

* Manipular los bits de números.
	* Aprendan a controlar sus nuevos poderes.
* Practicar trabajar con la asignación de memoria de manera dinámica (esa cosa de _malloc_).
	* Aprovechar toda la memoria no utilizada.
* Pensar cómo el manejo de memoria dinámica los puede hacer mejores personas.
	* Son bromas. Perdón, pero sólo los puede volver mejores programadores.

## Preparación
De primero, deben de descargar todos los archivos que necesitarán para completar este laboratorio, estos se encuentran [aquí](https://github.com/cc-3/lab02-C-MM.git). Recuerden que deben aceptar la asignación y se les creará automáticamente un repositorio con una extensión que termine con su usuario.
Recuerden que este será público para que se pueda revisar por copia o plagio. Esto será sancionado acorde al reglamento de la universidad.

Ahora, ya pueden ejecutar en la terminal el comando que les descargará los archivos base en el directorio a su elección:
```shell
git clone link_al_lab
```


## Ejercicio 1: Operando Bits

Para este inciso, su trabajo es completar el archivo **bit_ops.c** de manera que las funciones cumplan con su función. Para ello deberán utilizar las operaciones de bits básicas: and (&), or (\|), xor (^), not (~) y los corrimientos a la derecha (\>\>) y a la izquierda (<<). Deben evitar el uso de bucles o condicionales.

¡¡¡¡No usar loops o condicionales!!!! Eso significa que MIENTRAS realicen el ejercicio no tienen el derecho de escribir las palabras: if, else, while, for, switch o algo de índole similar. Por favor no traten de engañarnos, todo el personal involucrado (esperamos) saben cómo se miran todas estas palabras, entonces si las encontramos, ![YOU SHALL NOT PASS](https://github.com/cc-3/lab02-C-MM/Imágenes Lab02/You Shall Not Pass GIF.gif).

**NOTA IMPORTANTE:** Considerar que _n_ es un valor que inicia en la posición cero, contando desde la derecha, por lo que el bit que se encuentre hasta la derecha es el bit cero.

```shell
// Return the nth bit of x.
// Assume 0 <= n <= 31
unsigned get_bit(unsigned x,
                 unsigned n);

// Set the nth bit of the value of x to v.
// Assume 0 <= n <= 31, and v is 0 or 1
void set_bit(unsigned * x,
             unsigned n,
             unsigned v);

// Flip the nth bit of the value of x.
// Assume 0 <= n <= 31
void flip_bit(unsigned * x,
              unsigned n);
```
**Ayuda** para _set_bit_: La parte complicada es no saber el valor del bit antes de cambiarlo. Pero, sabemos que _0 | x = x_, pero ¿podemos aprovecharnos de esto? ¿Es posible volverlo cero?

Una vez terminen de editar las funciones, pueden compilar y correr el código con:
```shell
$ make bit_ops
$ ./bit_ops
```
Lo cual imprimirá el resultado de algunas pruebas.

Ahora deben de subirlo al autograder XD.

## Ejercicio 2: Registro de Corrimiento con Retroalimentación Lineal
En este ejercicio deben de implementar una función que compute la siguiente iteración de un registro de corrimiento de retroalimentación lineal (LFSR por sus siglas en inglés). ¡Algunas aplicaciones que utilizan LFSRs son: televisión digital, teléfonos con acceso múltiple por división de código, Ethernet, USB 3.0 y mucho más! Esta función deberá generar números pseudo-aleatorios utilizando operadores binarios. Para un poco de información adicional, pueden visitar el siguiente [link de Wikipedia](https://es.wikipedia.org/wiki/LFSR). En el archivo 'lfsr.c' deben de completar la función _lfsr_calculate()_ de manera que realice lo siguiente:

### Diagrama del Hardware (Explicación Más Abajo)
![LFSR](https://github.com/cc-3/lab02-C-MM/Imágenes Lab02/LFSR.png)

### Explicación del Diagrama de Arriba
* En cada llamada de _lfsr_calculate()_, deben de correr el contenido del registro un bit hacia la derecha.
* Este corrimiento no es ni lógico, ni aritmético. En el lado izquierdo deben de colocar un bit equivalente a un XOR de los bits que estaban, originalmente, en las posiciones 1, 3, 4 y 6.
* El objeto que parece un faro de automóvil curvado es un XOR, el cual recibe dos entradas (a, b) y devuelve en su salida a^b.
* A diferencia del ejercicio 1, las posiciones de los bits **inician con 1**.

Después que hayan implementado de manera correcta _lfsr_calculate()_, compilen lfsr.c y córranlo. Su respuesta debe ser similar a lo siguiente:
```shell
$ make lfsr
$ ./lfsr
My number is: 1
My number is: 5185
My number is: 38801
My number is: 52819
My number is: 21116
My number is: 54726
My number is: 26552
My number is: 46916
My number is: 41728
My number is: 26004
My number is: 62850
My number is: 40625
My number is: 647
My number is: 12837
My number is: 7043
My number is: 26003
My number is: 35845
My number is: 61398
My number is: 42863
My number is: 57133
My number is: 59156
My number is: 13312
My number is: 16285
 ... etc etc ...
Got 65535 numbers before cycling!
Congratulations! It works!
```

##Ejercicio 3: Manejo de Memoria
Este ejercicio requiere de los archivos: vector.h, vector-test.c y vector.c, en donde les proveemos con la base para la implementación de un arreglo de longitud variable. Este inciso busca que se familiaricen con el uso de los "structs" de C, así como el manejo de memoria en este lenguaje. En otras palabras, no se preocupen por los detalles prácticos de esta estructura de datos un tanto extraña. Sólo no lo hagan.

**Su trabajo es completar las funciones** _vector-new()_, _vector_get()_, _vector_delete()_ **y** _vector_set()_ **en** _vector.c_ **de manera que** _vector-test.c_ **corra sin errores de manejo de memoria.**

###¿Cómo funciona un _vector_t_?
* Posee un _int size_ que indica cuántos elementos posee actualmente. En otras palabras, el _size_ es igual al índice de la última posición que ha sido alterada del vector. Por ejemplo, si se tiene un vector con un _size_ de 5 y se altera su ducentécimo bit (índice iniciando en cero),  su tamaño se verá actualizado a 201. La longitud por defecto del vector _vector_new_ es de 1.
* Tiene un _int \*data_, un arreglo dinámico de enteros que contiene los valores de los componentes del vector. Si se altera el ducentécimo elemento de un vector _v_ a 8 entonces el elemento modificado (de nuevo, iniciando en cero) de _v->data_ debería evaluar a 8. El valor de un vector _vector_new_ es 0 por defecto.
* El valor de cualquier componente de algún vector que no ha sido explícitamente editado es 0. Si se deseara conocer el valor en la quinta posición de un vector, pero sólo se ha alterado el valor de los primeras dos, la interrogante tendría como respuesta 0. Además, si se quisiera el contenido en la séptima posición de un vector de longitud igual a 5, también sería 0. **NO** devolvería un error.

Es momento de revisar el código de _vector.c_ si no lo han hecho. Aquí hay comentarios complementarios que describen cómo deberían de correr las funciones. Recuerden que los usuarios de su estructura de datos _vector_t_ deben asumir que todas las entradas al vector son 0, a menos que hayan sido definidas de otra manera por ellos. Tengan esto en mente, porque _malloc_ no hace esto por ustedes.

###¿Qué deben hacer?**
* Observen las funciones nombradas, creativamente, _bad_vector_new()_ y _also_bad_vector_new()_ e indiquen por qué son malas maneras de inicializar un _struct_ en C.
* Completen _vector_new_, la versión correcta. Hay exactamente seis (6) espacios para que escriban una expresión en C, indicados con el comentario que dice _/\* YOUR CODE HERE \*/_. Escriban una _expresión_ en estos sitios. Esto significa no más de una línea de código. Existen comentarios adicionales que describen qué debería de suceder en la línea de código inferior a cada división.
* Terminen _vector_get()_ de la misma manera en que lo hicieron para la función anterior: de manera respetuosa, dispuesto a aprender, con mente abierta y conscientes de qué es lo que están escribiendo, ya que esta es la mejor forma de programar.
* Complementen _vector_delete()_. Una solución satisfactoria no debería de llevar más de dos líneas de código.
* Corrijan a _vector_set()_. Esta es la más complicada. Bienvenidos a las ligas mayores. El problema de manipular una posición/índice arbitrario en un vector _v_ es que es posible que no se haya reservado suficiente espacio con _malloc_ en _vector->data_ (sí, eso significa que tuvieron que haber guardado memoria con _malloc_). Piensen cómo administrar la memoria para lograr esto, para ver qué hacer con la data que estaba ahí antes y de qué otras cosas deben de hacer en su nuevo bloque de datos.   Ayuda: Recuerden que los índices que no hayan sido alterados deben de ser cero. Hay distintas formas de acabar resolviendo esta función. Consideren el uso de las 3 funciones _\_\_alloc_, porque pueden resultar útiles...

Saber cómo reorganizar y liberar memoria es importante para la programación en C. Piensen que el manejo de memoria es como un parqueo, si hay carros parqueados y los dueños nunca se van, entonces no tienen espacio para nuevos carros. **Y recuerden que deberían tener un 'heap' vacío al terminar su programa.**

Finalmente, acuérdense de correr ``./submit TOKEN `` para evaluar su trabajo en el autograder y de subir el link de su repositorio al GES.