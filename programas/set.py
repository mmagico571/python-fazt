# set
    # ->02:07:00
    # Coleccion desordenada que no tiene un indice

# Declaracion de una variable tipo set
colors = {"Rojo","Verde","Azul"}
print(colors)
print(type(colors))

# Metodos para set
print(dir(colors))

# Saber si un elemento se encuentra dentro de set
print("Rojo" in colors)
print("Negro" in colors)

# Agregar elementos a set
colors.add("Blanco")
print(colors)

# Eliminar elementos de set
colors.remove("Rojo")
print(colors)

# Limpiar todo el set
colors.clear()
print(colors)

# Borrar el set
del colors
    # print(colors)
