# Condicionales
    #->02:19:50

# Operadores de comparacion
    # mayor que >
    # menor que <
    # igual que ==

# Estructura if
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

# Estructura elif

if color == "blue":
    print('blue')
elif color == "red":
    print("red")
else:
    print("Otro color")

# Anidacion if
name = "juan"
apellido = "lopez"

if name == "juan":
    if apellido == "hernandez":
        print("Tu eres juan hernandez")
    else:
        print("Tu NO eres juan hernandez")
else:
    print("tu no eres juan")

# Operadores logicos
    # and
    # or
    # not