# Curso python para principiantes Fazt
>[Curso python para principiantes](https://www.youtube.com/watch?v=chPhlsHoEPo "Reproducir video en YouTube")

## 1. Que es python
Es un lenguaje de programacion de alto nivel de proposito general, es un lenguaje interpretado. Su sintaxis es muy sencilla, cuenta con una gran variedad de bibliotecas, funciona en diversas plataformas y considerado como un lenguaje multiparadigma. Cuenta con una amplia documentacion.

**Aplicaciones tipicas que se pueden elaborar**

* CLI
* GUI
* Aplicaciones WEB BackEnd
* Robotica y Hardware
* Aplicaciones cientificas

---

## 2. Instalacion de python

### En windos

[Pagina oficial de descargas de python](https://www.python.org/downloads/)

**Proceso de instalacion**

1. Descargar el instalador mas reciente de la pagina oficial.
2. Ejecutar el asistente del instalador. Agregar al PHAT.
3. Verificar la version de phyton desde consola: 
```python --version```
4. iniciar phyton en la terminal con el comando:  ```python``` o directamente desde la shell que se instala.

### En linux

En las distribuciones mas populares de linux ya viene preinstalado python. solo hay que verificar si esta actualizado en su version mas reciente.

---
## 3 Lo basico en python

1. Mostrar texto en pantalla:

```python
print("Hola Mundo")
```
2. Comentarios
```python
# Esto es un comentario en python
```
3. Salir del inteprete de python
```python
exit()
```
4. La extencion de un archivo fuente de python es **nombre.py**.

5. Para ejecutar un archivo de python
```
python3 archivo.py
```
***Programas elaborados***

[1 HolaMundo](programas/HolaMundo.py)

---
## 4 Tipos de datos en python

0. Mostrar el tipo de dato
```python
print(type("texto"))
print(type(100))
print(type(1.1))
print(type(True))
print(type(False))
print(type([10, 3.14,"Hola",True]))
print(type((10, 3.14,"Hola",True)))
print(type({"nombre":"tobias", "aPaterno":"piña", "aMaterno":"posos","edad":5}))
print(type(None))
```
1. string
```python
print("Primer texto")
print('Segundo texto')
print("""Tercer texto""")
print('''Cuarto texto''')
```
* concatenar textos

```python
print("texto 1 " + "texto 2")
```

2. Numeros

*  Enteros

```python
print(30)
```

*  Flotantes

```python
print(3.14)
```
3. Booleanos

```python
print(True)
print(False)
```

4. Listas
```python
[10,20,30,40]
["Hello","Bye","hola","adios"]
[10, 3.14,"Hola",True]
[]
```
5. Tuplas
```python
(10,20,30,40)
("Hello","Bye","hola","adios")
(10, 3.14,"Hola",True)
()
```
6. Diccionarios

```python
{"nombre":"tobias", "aPaterno":"piña", "aMaterno":"posos","edad":5}
```

7. Dato sin identificar

```python
None
```

***programas elaborados***

[dataTypes](programas/dataTypes.py)

---
## 5 Variables

### 1 Tipos de variables


```python
variableString = "texto"
variableDecimal = 10
variableFlotante = 3.14
variableLista = [1,2,3]
variableTupla = ("a","b")
variableDiccionario = {"numero1":100,"numero2":200}
variableSinIdentificar = None
print(variableString)
print(variableDecimal)
print(variableFlotante)
print(variableLista)
print(variableTupla)
print(variableDiccionario)
print(variableSinIdentificar)
```
### 2 Reglas de declaracion de variables
* Python es un lenguaje Case sensitive
* Los nombres empiezan con minusculas , mayusculas y giones bajos exepto numeros

```python
Libro = "I Robot"
libro = "Carbono alterado"
_libro = "La guerra de los mundos"
print(Libro)
print(libro)
print(_libro)
```
### 3 Declaracion de variables en multiples lineas


```python
x, y = 100 , 200
print(x,y)
```
### 4 Constantes
Las constantes se declaran en mayusculas

```python
PI = 3.14
print(PI)
```
### 5 Lenguaje dinamico
Cambio del tipo de dato para una variable en tiempo de ejecucion.

```python
mi_libro = "Ready Player ONE"
print(mi_libro)
mi_libro = 1984
print(mi_libro)
```

***programas elaborados***

[variables](programas/variables.py)

---

## 6 Variables string

### 6.1 Obtener todos lo metodos para una variable
```python
print(dir(myStr))
```
### 6.2 Convertir todo el texto a mayusculas
```python
print(myStr.upper())
```
### 6.3 Convertir todo el texto a minusculas
```python
print(myStr.lower())
```
### 6.4 Cambiar minusculas por mayusculas y mayusculas por minusculas
```python
print(myStr.swapcase())
```
### 6.5 Convertir la primera letra del string en mayuscula
```python
print(myStr.capitalize())
```
### 6.6 Remplazar un texto
```python
print(myStr.replace("Hola","Bye"))
```
### 6.7 Metodos encadenados
```python
print(myStr.replace("Hola","Bye").upper())
```
### 6.8 Contar caracteres
```python
print(myStr.count("l"))
```
### 6.9 Determina verdadero o falso si el string inicia con determinados caracteres
```python
print(myStr.startswith("Hola"))
```
### 6.10 Determina verdadero o falso si el string termina con determinados caracteres
```python
print(myStr.endswith("c++"))
```
### 6.11 Dividir el string separados por un caracter
```python
print(myStr.split(" "))
```
### 6.12 Encontrar la posicion de un caracter en el string
```python
print(myStr.find("H"))
```
### 6.13 Tamaño del string
```python
print(len(myStr))
```
### 6.14 Mostrar el indice de un caracter dentro de un string
```python
print(myStr.index("e"))
```
### 6.15 Si el estring es alfanumerico o si es numerico
```python
print(myStr.isalnum())
print(myStr.isalpha())
```
### 6.16 Imprimir un caracter mediante su indice
```python
print(myStr[6])
```
### 6.17 Imprimir un caracter mediante su indice inverso
* El ultimo caracter tiene el valor de -1
```python
print(myStr[-1])
```

***programas elaborados***

[strings](programas/strings.py)

---

## 7 Variables 

### 1 Numeros enteros
```python
entero = 100
print(type(entero))
print(entero)
```

### 2 Numeros flotantes
```python
flotante = 3.14
print(type(flotante))
print(flotante)
```

### 3 Operaciones aritmeticas
```python
    # 1 Suma
print(7+2)
    # 2 Resta
print(7-2)
    # 3 Multiplicacion
print(7*2)
    # 4 Division
print(7/2)
    # 5 Modulo
print(7%2)
    # 6 Division entera
print(7//2)
    # 7 Potencia de un numero
print(2**3)
```

### 4 Precedencia de operadores
```python
    # parentesis
    # potencia
    # multiplicaciones, diviciones
    # sumas y restas
```

### 5 Entrada de datos en python
```python
numero = input("Ingrese un numero: ")
print(numero)
```

### 6 Convertir string a enteros o flotantes
```python
print(type(numero))
suma = int(numero) + 5
print(suma)
print(type(suma))

numero2 = float(input("Ingresa otro numero: "))
print(type(numero2))
print(numero2)
```
***programas elaborados***

[numbers](programas/numbers.py)

---

## 8 Listas

### 1 Declaracion de listas
```python
lista1 = [1,"gato",3.14,[10,20,"laptop"],3.14]
lista2 = ["verde","blanco","rojo"]
print(lista1)
print(lista2)
```

### 2 Constructor
* l argumento de list es una tupla
```python
lista3 = list((1,2,3,9))
print(lista3)
print(type(lista3))
```

### 3 Rango
* El rango llega hasta uno menos que el valor limite
```python
rango = list(range(1,10))
print(rango)
```

### 4 Obtener la lista de metodos para las lisas
```python
print(dir(lista2))
```

### 5 Longitud de una lista
```python
print(len(lista3))
```

### 6 Imprimir desde la posicion de un elemento en la lista
```python
print(lista3[0])
print(lista3[1])
print(lista3[2])
print(lista3[3])
```

### 7 Imprimir desde la posicion de un elemento en la lista en forma inversa
```python
print(lista3[-4])
print(lista3[-3])
print(lista3[-2])
print(lista3[-1])
```

### 8 Saber si un elemento existe dentro de la lista
```python
print(1 in lista3)
print("uno" in lista3)
```

### 9 Reasignar el valor a un elemento de la listas
```python
print(lista3)
lista3[1] = "dos"
print(lista3)
```

### 10 Agregar un nuevo elemento a la lista
```python
lista3.append("diez")
print(lista3)
```

### 11 Agregar varios elementos a la lista
* El argumento de la funcion debe ser una tupla o una lista
```python
lista3.extend((11,12,13))
lista3.extend([20,21,22,23])
print(lista3)
```

### 12 Insertar un elemento antes de una posicion especifica de la lista
```python
lista3.insert(0,0)
lista3.insert(9,14)
lista3.insert(len(lista3),100)
print(lista3)
```

### 13 Eliminar ultimo elemento de la lista
```python
lista3.pop()
print(lista3)
```

### 14 Eliminar un elemento por su indice
```python
lista3.pop(2)
print(lista3)
```

### 15 Eliminar elementos por el valor que contiene el elemento de la lista
```python
lista3.remove("diez")
lista3.remove(0)
print(lista3)
```

### 16 Eliminar todos los elementos de una lista
```python
lista3.clear()
print(lista3) 
```

### 17 Ordenar alfabeticamente los elementos de una lista
```python
print(lista2)
lista2.sort()
print(lista2)
```

### 18 Ordenar alfabeticamente de forma inversa los elementos de una lista
```python
lista2.sort(reverse=True)
print(lista2)
```

### 19 Obtener el indice de un elemento por su valor
```python
print(lista1)
print(lista1.index("gato"))
print(lista1.index(3.14))
```

### 20 Contar las veces que aparece repetido un elemento en la lista
```python
print(lista1)
print(lista1.count(3.14))
```

***programas elaborados***

[list](programas/list.py)

---

## 9 Tuplas

### 1 Definicion de tuplas
```python
tupla1 = (1,2,3)
print(tupla1)
print(type(tupla1))
```

### 2 Constructores de tuplas
* Solo se les puede pasar por argumento una lista o una tupla
```python
tupla2 = tuple(("a","b","c"))
print(tupla2)
tupla3 = tuple(["x","y","z"])
print(tupla3)
```

### 3 Ver todos los metodos de una tupla
```python
print(dir(tupla1))
```

### 4 Considerar una tupla de un solo elemento
* Solo se debe colocar una coma al final del unico elemento
```python
tupla4 = (1)
print(tupla4)
print(type(tupla4))

tupla5 = (1,)
print(tupla5)
print(type(tupla5))
```

### 5 Imprimir un elemento de la tupla mediante su indice
```python
print(tupla3)
print(tupla3[2])
```

### 6 Eliminar toda la tupla
```python
del tupla3
    # print(tupla3)
```

### 7 Localizaciones ejemplo de uso de tuplas
```python
localizaciones = {
    (123, 456):"Tokio",
    (987, 765):"Mexico"
}
```

***programas elaborados***
[tuples](programas/tuples.py)



