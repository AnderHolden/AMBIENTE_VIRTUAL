import random

#Ejemplo 4: Juego de adivianza con While
numero = random.randint(1, 10)
print("Adivina un número entre 1 y 10 🎲")
intento = 0

while intento != numero:
    intento = int(input())
    if intento > numero:
        print("Muy alto 🔼")
    else:
        if intento < numero:
            print("Muy bajo 🔽")

print("¡Correcto! 🎉")
