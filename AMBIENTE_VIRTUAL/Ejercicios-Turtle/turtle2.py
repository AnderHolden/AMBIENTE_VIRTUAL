import turtle
from PIL import Image 

pantalla = turtle.Screen()
pantalla.bgcolor("black")
t = turtle.Turtle()
t.color("purple")

for _ in range(36):
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.right(10)

for _ in range(36):
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.right(10)

# Guardar imagen
turtle.getscreen().getcanvas().postscript(file="turtle2.eps")

# Convertir EPS a PNG
img = Image.open("turtle2.eps")
img.save("turtle2.png")

turtle.done()