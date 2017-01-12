---
layout: post
title:  "Tutorial de Python"
date:   2017-01-11
category: tutorial
description: Aprender casi todo sobre python
permalink: /:categories/:title.html
---

### Python

_NOTA1 aquí les vamos a mostrar lo básico, Python tiene un sin fin de cosas bien cool que pueden buscar por su cuenta como “NumPy, SciPy, MatPlotLib, etc.”_

Python es un lenguaje de programación de alto nivel (su abstracción es bastante alta, casi es pseudocódigo). Además Python es un lenguaje interpretado y usa “dynamic typing”, esto a diferente de Java que usa “static typing”, significa que no se declara que tipo de dato va a ser una variable sino que dinámicamente el interprete lo decide dependiendo del tipo de dato que se le sea asignado a la variable. Se dice que el código de Python es pseudocódigo porque los deja expresar ideas bastante poderosas en muy pocas lineas de código y sigue siendo bastante entendible.

_NOTA2: Python es un lenguaje de programación orientado a objetos, todo los tipos en Python hasta los basicos son objetos, inclusive las funciones son objetos (que raro). En Python si es necesario tomar en cuanta la identación porque asi es como Python interpreta el flujo del programa "IDENTEN BIEN"._

Para correr el interprete de Python en sus computadoras vía command line utilicen:

```shell
$ python
```

***

### Tipos de datos básicos

Como muchos lenguajes, Python tiene un numero de tipos de datos básicos incluyendo enteros, floats, booleans y strings. Estos tipos de datos se comportan como lo han visto en otros lenguajes de programación (Java por ejemplo).

**Manejo de Números:** Los enteros y los floats trabajan como ustedes vieron que trabajaban en Java


```python
x = 3
print type(x) # Imprime "<type 'int'>"
print x       # Imprime "3"
print x + 1   # Suma; Imprime "4"
print x - 1   # Resta; Imprime "2"
print x * 2   # Multiplicacion; Imprime "6"
print x ** 2  # Exponenciar; Imprime "9"
x += 1
print x  # Imprime "4"
x *= 2
print x  # Imprime "8"
y = 2.5
print type(y) # Imprime "<type 'float'>"
print y, y + 1, y * 2, y ** 2 # Imprime "2.5 3.5 5.0 6.25"
```

*Noten que no como muchos lenguajes, Python no tiene incremento unitario (x++) o decremento (x--).*

Python también tiene tipos long para enteros y números complejos. Vean la [documentación](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex) para más detalles.


<p><b>Booleans:</b> Python implementa todos los operadores usuales para hacer lógica booleana, pero usa palabras en Ingles en vez de simbolos (&amp;&amp;, ||, etc.):</p>

```python
t = True
f = False
print type(t) # Imprime "<type 'bool'>"
print t and f # AND; Imprime "False"
print t or f  # OR; Imprime "True"
print not t   # NOT; Imprime "False"
print t != f  # XOR; Imprime "True"
```

**Strings:** Python tiene buen soporte de strings:

```python
hello = 'hello'   # Literales String  se pueden usar apostrofes
world = "world"   # o comillas, no importa la verdad
print hello       # Imprime "hello"
print len(hello)  # String length; Imprime "5"
hw = hello + ' ' + world  # Concatenacion de Strings
print hw  # Imprime "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # Estilo sprintf
print hw12  # Imprime "hello world 12"
```

Los objetos strings tienen un montón de métodos útiles; Por ejemplo:

```python
s = "hello"
# Pone la letra del principio en mayuscula
print s.capitalize()  
# Pasa el string a mayusculas
print s.upper()       
# Justifica un string, rellenando con espacios; Imprime "  hello"
print s.rjust(7)      
# Centra un string, rellanando con espacios; imprime " hello "
print s.center(7)
# Reemplaza todas las apariciones de un substring por otro;
print s.replace('l', '(ell)')  
# imprime "he(ell)(ell)o"}
# Quita los white-characters del principio y final; prints "world"
print '  world '.strip()
```
Pueden encontrar una lista de todos los metodos en la [documentación](https://docs.python.org/2/library/stdtypes.html#string-methods).

***

### Contenedores


Python incluye un montón de tipos de contenedores: listas, diccionarios, sets y tuplas.

**Listas:**

una lista en Python es equivalente a un arreglo en Java, pero es dinámico (puede cambiar su tamaño, es decir no es fijo) y puede tener elementos de diferentes tipos:

```python
# Crea una lista
xs = [3, 1, 2]  
# Imprime "[3, 1, 2] 2"
print xs, xs[2]  
# Los indices negativos empiezan desde el final de la lista prints "2"
print xs[-1]     
# Las listas pueden contener elementos de diferentes tipos
xs[2] = 'foo'    
# Imprime "[3, 1, 'foo']"
print xs         
# Añade un elemento al final de la lista
xs.append('bar')
# Imprime la lista
print xs         
# Quita y devuelve el ultimo elemento de la lista
x = xs.pop()  
# Imprime "bar [3, 1, 'foo']"  
print x, xs      
```

Puden encontrar más detalles en la [documentación](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists) de listas.


**Slicing:** Además de acceder a los elementos de una lista uno a la vez, Python provee una sintaxis consistente para acceder a sublistas; esto se conoce como slicing.

```python
# range es una funcion que ya viene con Python y crea una lista de n elementos enteros.
nums = range(5)
# Imprime "[0, 1, 2, 3, 4]"
print nums   
 # Agarra una sublista desde el indice 2 hasta el indice 3 es decir [2,4)      
print nums[2:4]   
# Agarra una sublista desde el indice 2 hasta el final de la lista, es decir [2,4]
print nums[2:]     
# Agarra una sublista desde el principio de la misma hasta el indice 2 sin incluir, es decir [0,2)
print nums[:2]    
# Agarra toda la lista "[0, 1, 2, 3, 4]"
print nums[:]     
# El slice puede ser negativo, en este caso agarra desde el principio hasta el penultimo elemento, es decir [0,3]
print nums[:-1]    
# Asigna una sublista al slice
nums[2:4] = [8, 9]
# Imprime "[0, 1, 8, 8, 4]"   
print nums         
```

**Ciclos:** Pueden iterar sobre elementos de una lista de la siguiente manera:

```python
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print animal
# Imprime "cat", "dog", "monkey", cada uno en una nueva linea      
```

Si quieren acceder al indice de cada elemento dentro del ciclo, pueden utilizar la funcion “enumerate”:

```python
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)
# Imprime "#1: cat", "#2: dog", "#3: monkey", Cada uno en su linea   
```

**List comprehensions:** Cuando estamos programando, frecuentemente vamos a querer transformar un tipo de dato hacia otro. Como un ejemplo simple, consideren el siguiente código que calcula numeros al cuadrado:

```python
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares   # Imprime [0, 1, 4, 9, 16]
```

Pueden hacer este código más simple utilizando una list comprehension:

```python
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares   # Imprime [0, 1, 4, 9, 16]
```

Las list comprehension pueden contener condiciones:

```python
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares  # Imprime "[0, 4, 16]"
```

***

### Diccionarios

Un diccionario guarda un par (key, value), similar a un Map en java. Pueden utilizarlo así:

```python
d = {'cat': 'cute', 'dog': 'furry'}  # Crea un nuevo diccionario con algunos datos
print d['cat']       # Toma el valor del key “cat”
print 'cat' in d     # Verifica que el key “cat” este en el diccionario   d
d['fish'] = 'wet'    # Añade un par key,value al diccionario
print d['fish']      # Imprime "wet"; si tratan de buscar un key que no existe # print d['monkey']  # KeyError: 'monkey' not a key of d
print d.get('monkey', 'N/A')  # Agarra un elemento con un valor por defecto; imprime "N/A"
print d.get('fish', 'N/A')    # Agarra un elemento con un valor por defecto; imprime "N/A"
del d['fish']        # Remueve un elemento del diccionario
print d.get('fish', 'N/A') # "fish" ya no pertenece al diccionario; imprime "N/A"
```

Pueden encontrar todo lo que necesitan saber de diccionarios en la [documentación](https://docs.python.org/2/library/stdtypes.html#dict).

**Ciclos:** es fácil iterar sobre las keys de un diccionario:

```python
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)
# Imprime "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"
```

Si quieren acceder a las keys y sus valores correspondientes pueden utilizar el método “iteritems”:

```python
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)
# Imprime "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"
```

**Dictionary comprehensions:** Estos son similares a las list comprehensions, pero ayuda a construir diccionarios fácilmente, por ejemplo:

```python
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_square  # Imprime "{0: 0, 2: 4, 4: 16}"
```

***

### Sets

Un set es un la colección no ordenada de elementos distintos. Como ejemplo simple, consideren lo siguiente:

```python
animals = {'cat', 'dog'}
print 'cat' in animals   # Verifica que un elemento este en el set; Imprime “True”
print 'fish' in animals  # Imprime "False"
animals.add('fish')      # Añade un elemento al set
print 'fish' in animals  # Imprime "True"
print len(animals)       # Numero de elementos en un set; imprime "3"
animals.add('cat')       # Añadir un elemento que ya esta en el set, lo permite pero no pasa nada
print len(animals)       # Imprime "3"
animals.remove('cat')    # Remueve un elemento del set
print len(animals)       # imprime "2"
```

Otra vez, todo lo que quieran saber acerca de los sets lo pueden encontrar en la [documentación](https://docs.python.org/2/library/sets.html#set-objects).

**Loops:** Iterear sobre un set tienen la misma sintaxis que iterar sobre una lista; sin embargo como los sets no tienen orden, no pueden asumir sobre en que orden se van a visitar los elementos del set:

```python
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)
# Imprime "#1: fish", "#2: dog", "#3: cat"
```

**Set comprehensions:** como las listas y los diccionarios, podemos construir sets fácilmente utilizando set comprehensions:

```python
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums  # Imprime "set([0, 1, 2, 3, 4, 5])"
```

***

### Tuplas

Una tupla es una lista ordenada de elementos “fija”. Una tupla es bastante similar a una lista, una de las más importantes diferencias es que las tuplas se pueden utilizar como keys en un diccionario y como elementos de los sets, mientras que las listas no. Aquí hay un ejemplo:

```python
d = {(x, x + 1): x for x in range(10)}  # Crea un diccionario con keys de tuplas
t = (5, 6)       # Crea una tupla
print type(t)    # Imprime "<type 'tuple'>"
print d[t]       # Imprime "5"
print d[(1, 2)]  # Imprime "1"
```

La [documentación](https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences) tiene mas información acerca de las tuplas.

***

### Funciones


Las funciones de Python se definen utilizando el keyword def. Por ejemplo:

```python
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print sign(x)
# Imprime "negative", "zero", "positive"
```

Vamos a definir funciones que toman argumentos, y opcionalmente argumentos keyword, como esto:

```python
def hello(name, loud=False):
    if loud:
        print 'HELLO, %s' % name.upper()
    else:
        print 'Hello, %s!' % name

    hello('Bob') # Imprime "Hello, Bob"
    hello('Fred', loud=True)  # Imprime "HELLO, FRED!"
```

Hay mucha información acerca de como definir funciones en Python en la [documentación](https://docs.python.org/2/tutorial/controlflow.html#defining-functions).

***

### Clases


De esto no creo que se tengan que preocupar para este curso pero la sintaxis para definir clases en Python es así:


```python
class Greeter:
    # Constructor
    def __init__(self, name):
        self.name = name  # Crea un atributo para la clase

    # Un metodo de la clase
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

g = Greeter('Fred')  # Crea una instancia de la clase
g.greet()            # Llama al metodo de la clase; imprime "Hello, Fred"
g.greet(loud=True)   # Llama al metodo de la clase; imprime "HELLO, FRED!"
```

Pueden leer sobre las clases en Python y su definición en la [documentación](Pueden leer sobre las clases en Python y su definición en la documentación.).
