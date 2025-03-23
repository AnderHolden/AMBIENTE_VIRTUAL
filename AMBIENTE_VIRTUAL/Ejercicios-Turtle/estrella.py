import turtle
from PIL import Image

t = turtle.Turtle()
t.speed(0)  # Velocidad de la tortuga
s = turtle.Screen()
s.bgcolor("black")

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']  # Lista de colores corregida

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

# Guardar imagen
turtle.getscreen().getcanvas().postscript(file="estrella.eps")

# Convertir EPS a PNG
img = Image.open("estrella.eps")
img.save("estrella.png")

turtle.done()


# import turtle
# import math

# pantalla = turtle.Screen()
# pantalla.title('Mi primer proyecto tortuga')
# pantalla.bgcolor('black')
# tortuga = turtle.Turtle()
# tortuga.speed(0)  # Máxima velocidad
# tortuga.pensize(2)

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']  # Lista de colores

# # Dibujar una espiral logarítmica
# factor = 0.1
# for i in range(500):
#     # Cambiar el color del lápiz
#     tortuga.color(colors[i % len(colors)])
#     # Calcular el radio usando una función exponencial
#     r = factor * math.exp(0.01 * i)
#     # Mover la tortuga
#     tortuga.forward(r)
#     tortuga.right(20)

# for i in range(500, 1000):
#     # Cambiar el color del lápiz
#     tortuga.color(colors[i % len(colors)])
#     # Calcular el radio usando una función exponencial
#     r = factor * math.exp(-0.01 * (i - 1100))
#     # Mover la tortuga
#     tortuga.forward(r)
#     tortuga.right(-20)

# turtle.done()


# import turtle

# # Configuración de la pantalla
# bob = turtle.Turtle()
# bob.getscreen().bgcolor("blue")
# bob.color("white")
# bob.penup()
# bob.goto((-300,200))
# bob.pendown()

# # Función recursiva para dibujar una estrella fractal
# def star(tortuga, size):
#     if size <= 10:
#         return
#     else:
#         tortuga.begin_fill()
#         for i in range(5):
#             tortuga.forward(size)
#             star(tortuga, size / 2)
#             tortuga.left(216)
#         tortuga.end_fill()

# # Dibujar la estrella
# star(bob, 360)

# # Crear otra tortuga para escribir el mensaje
# mensaje = turtle.Turtle()
# mensaje.color("yellow")
# mensaje.penup()
# mensaje.goto(0, -250)
# mensaje.hideturtle()

# # Escribir el mensaje con tamaño grande
# mensaje.write("🎉 ¡Listos para programar con Turtle! 🐢", align="center", font=("Comic Sans MS", 25, "italic"))

# turtle.done()

# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("green")
# a = 0
# b = 0
# t.speed(0)
# t.penup()
# t.goto(0, 200)
# t.pendown()
# while True:
#     t.forward(a)
#     t.right(b)
#     a += 3
#     b += 1
#     if b == 210:
#         break

# t.hideturtle()  # Corregido la indentación

# turtle.done()


# import turtle

# t = turtle.Turtle()
# t.speed(0) #Velocidad de la tortuga
# s = turtle.Screen()
# s.bgcolor("black")

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']  # Lista de colores corregida

# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.width(x // 100 + 1)
#     t.forward(x)
#     t.left(59)

# turtle.done()
# import turtle

# # Configuración de la pantalla
# pantalla = turtle.Screen()
# pantalla.bgcolor("black")
# pantalla.title("Agujero Negro")

# # Configuración de la tortuga
# t = turtle.Turtle()
# t.speed(0)  # Máxima velocidad
# t.width(2)

# # Lista de colores
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# # Dibujar el agujero negro
# for x in range(360):
#     t.pencolor(colors[x % 6])
#     t.forward(x)
#     t.right(59)

# # Ocultar la tortuga y mantener la ventana abierta
# t.hideturtle()
# turtle.done()

