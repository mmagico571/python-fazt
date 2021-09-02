# Listas
# ->01:38:

# 1 Declaracion de listas
lista1 = [1,"gato",3.14,[10,20,"laptop"],3.14]
lista2 = ["verde","blanco","rojo"]
print(lista1)
print(lista2)

# 2 Constructor
    # el argumento de list es una tupla
lista3 = list((1,2,3,9))
print(lista3)
print(type(lista3))

# 3 Rango
    # El rango llega hasta uno menos que el valor limite
rango = list(range(1,10))
print(rango)

# 4 Obtener la lista de metodos para las lisas
print(dir(lista2))

# 5 Longitud de una lista
print(len(lista3))

# 6 Imprimir desde la posicion de un elemento en la lista
print(lista3[0])
print(lista3[1])
print(lista3[2])
print(lista3[3])

# 7 Imprimir desde la posicion de un elemento en la lista en forma inversa
print(lista3[-4])
print(lista3[-3])
print(lista3[-2])
print(lista3[-1])

# 8 Saber si un elemento existe dentro de la lista
print(1 in lista3)
print("uno" in lista3)

# 9 Reasignar el valor a un elemento de la listas
print(lista3)
lista3[1] = "dos"
print(lista3)

# 10 Agregar un nuevo elemento a la lista
lista3.append("diez")
print(lista3)

# 11 Agregar varios elementos a la lista
    # el argumento de la funcion debe ser una tupla o una lista
lista3.extend((11,12,13))
lista3.extend([20,21,22,23])
print(lista3)

# 12 Insertar un elemento antes de una posicion especifica de la lista
lista3.insert(0,0)
lista3.insert(9,14)
lista3.insert(len(lista3),100)
print(lista3)

# 13 Eliminar ultimo elemento de la lista
lista3.pop()
print(lista3)

# 14 Eliminar un elemento por su indice
lista3.pop(2)
print(lista3)

# 15 Eliminar elementos por el valor que contiene el elemento de la lista
lista3.remove("diez")
lista3.remove(0)
print(lista3)

# 16 Eliminar todos los elementos de una lista
lista3.clear()
print(lista3) 

# 17 Ordenar alfabeticamente los elementos de una lista
print(lista2)
lista2.sort()
print(lista2)

# 18 Ordenar alfabeticamente de forma inversa los elementos de una lista
lista2.sort(reverse=True)
print(lista2)

# 19 Obtener el indice de un elemento por su valor
print(lista1)
print(lista1.index("gato"))
print(lista1.index(3.14))

# 20 Contar las veces que aparece repetido un elemento en la lista
print(lista1)
print(lista1.count(3.14))