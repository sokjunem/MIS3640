import turtle

import math

sj = turtle.Turtle()

turtle.speed(10)

def new_position(x, y):#setting new coordination
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()

def square(t, length, x, y):
    new_position(x, y)
    for i in range(4):
        turtle.fd(length)
        turtle.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        turtle.fd(length)
        turtle.lt(angle)

def polygon(t, n, length, x, y):
    new_position(x, y)
    angle = 360 / n
    polyline(t, n, length, angle)
    
def arc(t, r, angle, x, y):
    new_position(x, y)
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r, x, y):
    arc(t, r, 360, x, y)

def reset(rtangle):#reset the angle of the arrow - move to right direction
    turtle.setheading(0)
    turtle.rt(rtangle)

def bf(t, length):#bow tie shape
    turtle.lt(30)
    for i in range(2):
        turtle.fd(length)
        turtle.rt(120)
    turtle.fd(2 * length)
    for i in range(2):
        turtle.lt(120)
        turtle.fd(length)

    
#Exercise3_1

def shape_1(t, r, d, e):
    new_position(d, e)
    bf(sj, r)
    turtle.lt(60)
    bf(sj, r)
    turtle.rt(120)
    circle(sj, r, d, e-r)

    x = math.radians(60) # coordination of small circles
    y = math.sin(x)
    z = y * r

    a = math.radians(30) # radius of small circles
    b = math.cos(a)
    c = (r/4) / b

    def mirror_circle(t, r, f, g):
        turtle.rt(180)
        circle(t, r, f, g+z)
        turtle.lt(90)
        circle(t, r, f+z-(2*c), g)

    mirror_circle(t, c, d, e)
    reset(0)
    mirror_circle(t, c, d-z+c, e+c-z)

shape_1(sj, 150, 50, 50)


#Exercise 3_2

def shape_2(t, r, x, y):
    new_position(x, y)
    coordination = math.sqrt(r**2 - (r/2)**2)

    circle(sj, r, x, y-r)
    turtle.rt(60)
    arc(sj, r, 120, x-coordination, y+r/2)
    reset(120)
    arc(sj, r, 120, x, y+r)
    reset(180)
    arc(sj, r, 120, x+coordination, y+(r/2))
    reset(240)
    arc(sj, r, 120, x+coordination, y-(r/2))
    reset(300)
    arc(sj, r, 120, x, y-r)
    reset(0)
    arc(sj, r, 120, x-coordination, y-(r/2))

shape_2(sj, 150, -50, 30)

#Exercise3_3

def ying_yang(t, r, x, y):
    turtle.pensize(int(input('type the width of the pen: ')))
    circle(sj, r, x, y-r)
    arc(sj, r/2, 180, x, y)
    arc(sj, r/2, 180, x, y)
    circle(sj, r/6, x, y+(r/3))
    circle(sj, r/6, x, y-(2*r/3))

ying_yang(sj, 100, 0, 0)

turtle.mainloop()

