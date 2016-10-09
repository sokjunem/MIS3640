import turtle
import random
sj = turtle.Turtle


def north(x):
    turtle.lt(90)
    turtle.fd(x)
    turtle.setheading(0)

def west(x):
    turtle.lt(180)
    turtle.fd(x)
    turtle.setheading(0)

def south(x):
    turtle.lt(270)
    turtle.fd(x)
    turtle.setheading(0)

def east(x):
    turtle.fd(x)
    turtle.setheading(0)
    
def drunkard_map(distance, intersection):
    for i in range(intersection):
        decision = random.choice([1, 2, 3, 4])
        print(decision)
        if decision == 1:
            north(distance)
        elif decision == 2:
            west(distance)
        elif decision == 3:
            south(distance)
        else:
            east(distance)

drunkard_map(50, 5)

turtle.mainloop()

