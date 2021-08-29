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



***programas elaborados***

[strings](programas/strings.py)

