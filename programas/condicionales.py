# Condicionales
    #->02:19:50

# 1 Operadores de comparacion
    # mayor que >
    # menor que <
    # igual que ==

# 2 Estructura if
edad = 20
if edad > 30:
    print("mayor que treinta")
else:
    print("Menor que treinta")

color = "red"

if color == "blue":
    print("blue")
else:
    print("Otro color")

# 3 Estructura elif

if color == "blue":
    print('blue')
elif color == "red":
    print("red")
else:
    print("Otro color")

# 4 Anidacion if
name = "juan"
apellido = "lopez"

if name == "juan":
    if apellido == "hernandez":
        print("Tu eres juan hernandez")
    else:
        print("Tu NO eres juan hernandez")
else:
    print("tu no eres juan")

# 5 Operadores logicos
    # and
    # or
    # not

# 6 estructura if y operadores logicos
x = 20
y = 20
if x >= 1 and x <= 10:
    print("ok")
else:
    print("Fuera de rango")

if(x>15 or y>15):
    print("hay uno mayor a 15")
else:
    print("todos son menores de 15")

if(not(x==y)):
    print("Son diferentes")
else:
    print("son iguales")