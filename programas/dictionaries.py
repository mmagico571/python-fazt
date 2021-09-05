# dictionaries
    # ->02:11:50

# Declaracion de diccionarios
producto = {
    "name": "libro",
    "cantidad":100,
    "precio": 3
    }

persona = {
    "nombre": "Ryan",
    "apellido": "Ray",
    "cuenta": 407068399
}

print(type(producto))
print(type(persona))

print(producto)
print(persona)


# 2 Metodos para los diccionarios
print(dir(producto))

# 3 Imprimir las llaves del diccionario
print(producto.keys())

# 4 obtener los items
print(producto.items())

# 5 Limpiar un diccionario
producto.clear()
print(producto)

# 6 Elimanr diccionarios
# del producto
print(producto)

# 7 anidar diccionarios
    # en una lista

producto2 = [
    {"id": 1,
    "nombre":"p1",
    "existencias": 1500},
    {"id": 2,
    "nombre":"p2",
    "existencias": 500},
    {"id": 3,
    "nombre":"p3",
    "existencias": 1000}
]
print(producto2)