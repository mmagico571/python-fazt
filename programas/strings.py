# Estrings
# ->1:02:30

# 1 Obtener todos lo metodos para una variable
myStr = "Hola Mundo desde python"
    # se utiliza la palabra reservada dir()
# print(dir(myStr))

# 2 convertir todo el texto a mayusculas
print(myStr.upper())

# 3 convertir todo el texto a minusculas
print(myStr.lower())

# 4 cambiar minusculas por mayusculas y mayusculas por minusculas
print(myStr.swapcase())

# 5 convertir la primera letra del string en mayuscula
print(myStr.capitalize())

# 6 Remplazar un texto
print(myStr.replace("Hola","Bye")) 

# 7 Metodos encadenados
print(myStr.replace("Hola","Bye").upper())

# 8 Contar caracteres
print(myStr.count("l"))

# 9 determina verdadero o falso si el string inicia con determinados caracteres
print(myStr.startswith("Hola"))

# 10 determina verdadero o falso si el string termina con determinados caracteres
print(myStr.endswith("c++"))

# 11 dividir el string separados por un caracter
print(myStr.split(" "))


# 12 encontrar la posicion de un caracter en el string
print(myStr.find("H"))

# 13 tamaño del string
print(len(myStr))

# 14 mostrar el indice de un caracter dentro de un string
print(myStr.index("e"))

# 15 si el estring es alfanumerico o si es numerico
print(myStr.isalnum())
print(myStr.isalpha())

# 16 imprimir un caracter mediante su indice
print(myStr[6])

# 17 imprimir un caracter mediante su indice inverso
    # El ultimo caracter tiene el valor de -1
print(myStr[-1])