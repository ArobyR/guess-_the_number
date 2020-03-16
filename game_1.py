""" AUTHOR == Gr0b1t:
                    Aroby
"""
# Nuestro objetivo es adivinar el número.
# mientras mas cerca este del numero debe dar una pista, frio = lejos, caliente = cerca,
# También poner el número de intentos requeridos.
# solo 10 intentos permitidos

from random import randint

num_intentos = 0
number_random = randint(1, 100)

print("Usted solo tiene 10 intentos.")

while num_intentos < 10:
    print(f"Intento {num_intentos+1}:")
    numero = int(input())
    num_intentos += 1

    # Si esta lejos del numero imprimir frio, caliente == cerca

    # Frio
    if numero >= number_random + 4 or numero <= number_random - 4:
        print("Frio")

    # Caliente
    if numero == number_random + 3 or numero == number_random -3:
        print("Caliente")

    if numero == number_random + 2 or numero == number_random - 2:
        print("Caliente")

    if numero == number_random + 1 or numero == number_random - 1:
        print("Caliente")

    if numero == number_random:
        break

if numero == number_random:
    print("Eres el ganador")

else:
    print("\nEres un perdedor este juego se ha acabado... :)")
    print("\nEl numero era: ", number_random)