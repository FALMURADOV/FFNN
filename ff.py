import turtle
n = turtle.Turtle()
n.screen.bgcolor('black')
n.pensize(2)
n.color('red')
n.left(90)

n.backward(100)
n.speed(200)
n.shape('turtle')

def tree(i):
    if i < 10 :
        return
    else:
        n.forward(i)
        n.color('green')
        n.circle(2)
        n.color('blue')
        n.left(30)
        tree(3*i/4)
        n.right(60)
        tree(3*i/4)
        n.left(30)
        n.backward(i)

tree(100)
turtle.done()