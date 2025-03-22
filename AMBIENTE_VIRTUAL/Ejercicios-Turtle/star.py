



# def cuenta_regresiva(n):
#     if n <= 0:
#         print("¡Boom!")
#     else:
#         print(n)
#         cuenta_regresiva(n-1)
# cuenta_regresiva(5)



import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")  # Corregido el color de fondo
pantalla.title("Estrella fractal")
tortuga = turtle.Turtle()
tortuga.speed(5)  # Velocidad reducida
tortuga.color("white")  # Color de la tortuga
tortuga.pensize(2)  # Grosor del trazo
tortuga.circle(150)  # Dibujar un círculo de radio 150
tortuga.penup()  # Levantar el lápiz
tortuga.goto(0, 150)  # Mover la tortuga a la posición (0, 150) sin dibujar
tortuga.pendown()  # Bajar el lápiz para dibujar
tortuga.speed(0)  # Máxima velocidad
turtle.done()  # Llamada a la función done

t = turtle.Turtle()
t.forward(100) # Mueve la totuga 100 px
t.right(90) # Gira la tortuga 90 grados
t.forward(100) # Mueve la tortuga 100 px
t.right(90) # Gira la tortuga 90 grados
t.forward(100) # Mueve la tortuga 100 px
t.right(90) # Gira la tortuga 90 grados
t.forward(100) # Mueve la tortuga 100 px
turtle.done()