# Tuplas
    # Conjunto de datos inmutables

# Definicion de tuplas
tupla1 = (1,2,3)
print(tupla1)
print(type(tupla1))

# Constructores de tuplas
    # Solo se les puede pasar por argumento una lista o una tupla
tupla2 = tuple(("a","b","c"))
print(tupla2)
tupla3 = tuple(["x","y","z"])
print(tupla3)

# Ver todos los metodos de una tupla
print(dir(tupla1))

# Considerar una tupla de un solo elemento
    # Solo se debe colocar una coma al final del unico elemento
tupla4 = (1)
print(tupla4)
print(type(tupla4))

tupla5 = (1,)
print(tupla5)
print(type(tupla5))

# Imprimir un elemento de la tupla mediante su indice
print(tupla3)
print(tupla3[2])

# Eliminar toda la tupla
del tupla3
    # print(tupla3)

# Localizaciones ejemplo de uso de tuplas
localizaciones = {
    (123, 456):"Tokio",
    (987, 765):"Mexico"
}