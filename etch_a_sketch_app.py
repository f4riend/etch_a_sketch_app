from turtle import Turtle,Screen,onkeypress

brush = Turtle()
canvas = Screen()
canvas.listen()


def mforward():
    brush.forward(10)

def mbackward():
    brush.back(10)

def directionl():
    brush.setheading(brush.heading() + 10)

def directionr():
    brush.setheading(brush.heading() - 10)

def clear():
    brush.clear()
    brush.penup()
    brush.home()
    brush.pendown()


onkeypress(mforward,"w")
onkeypress(mbackward,"s")
onkeypress(directionr,"d")
onkeypress(directionl,"a")
onkeypress(clear,"c")

canvas.exitonclick()