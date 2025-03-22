import turtle

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

turtle.done()