import turtle
fnn = turtle.Turtle()
fnn.color('white')
turtle.bgcolor("#73ad70")
def curve():
    for _ in range (200):
        fnn.right(1)
        fnn.forward(1)

fnn.speed(4)

fnn.begin_fill()
fnn.left(90)
fnn.left(50)
fnn.forward(110)
curve()
fnn.left(120)
curve()
fnn.forward(110)
fnn.end_fill()


turtle.done()