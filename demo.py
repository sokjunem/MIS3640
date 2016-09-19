import turtle

import math

sj = turtle.Turtle()

turtle.speed(10)

def new_position(x, y):         #setting coordination
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

def reset(rtangle):             # reset the angle of the arrow.
    turtle.setheading(0)
    turtle.rt(rtangle)

def bf(t, length):              #bow tie shape
    turtle.lt(30)
    for i in range(2):
        turtle.fd(length)
        turtle.rt(120)
    turtle.fd(2 * length)
    for i in range(2):
        turtle.lt(120)
        turtle.fd(length)

def mirror_circle(t, r, x, y):
    circle(t, r, -x, -y)
    turtle.rt(180)
    circle(t, r, x, y)
    

def shape_2(t, r):
    coordination = math.sqrt(r**2 - (r/2)**2)

    circle(sj, r, 0, -r)
    turtle.rt(60)
    arc(sj, r, 120, -coordination, r/2)
    reset(120)
    arc(sj, r, 120, 0, r)
    reset(180)
    arc(sj, r, 120, coordination, r/2)
    reset(240)
    arc(sj, r, 120, coordination, -(r/2))
    reset(300)
    arc(sj, r, 120, 0, -r)
    reset(0)
    arc(sj, r, 120, -coordination, -(r/2))

shape_2(sj, 100)

turtle.mainloop