import turtle

def draw_square(x):
    for _ in range(4):
        x.forward(100)
        x.right(90)

def draw():
    window = turtle.Screen()
    window.bgcolor("#B0B000")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("#0000B0")
    brad.speed(2)

    for i in range(1, 36):
        draw_square(brad)
        brad.left(10)

    window.exitonclick()

draw()