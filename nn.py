import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(100)
n = 70
h = 0
for i in range (360):
    c = colorsys.hsv_to_rgb('#53605c','#7B0323', '#00000')
    h+=1/n
    t.color(c)
    t.left(100)
    t.fd(200)
    for j in range (2):
        t.left(9)
        t.circle(20)