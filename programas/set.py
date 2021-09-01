# set
    # ->02:07:00
    # Coleccion desordenada que no tiene un indice

# 1 Declaracion de una variable tipo set
colors = {"Rojo","Verde","Azul"}
print(colors)
print(type(colors))

# 2 Metodos para set
print(dir(colors))

# 3 Saber si un elemento se encuentra dentro de set
print("Rojo" in colors)
print("Negro" in colors)

# 4 Agregar elementos a set
colors.add("Blanco")
print(colors)

# 5 Eliminar elementos de set
colors.remove("Rojo")
print(colors)

# 6 Limpiar todo el set
colors.clear()
print(colors)

# 7 Borrar el set
del colors
    # print(colors)
