import turtle as a
import time

a.pensize(1)
a.color("white")
a.bgcolor("black")
a.speed(3)
a.fillcolor("#FFFFFF")
a.begin_fill()

a.right(60)
a.forward(170)
a.left(60)
a.backward(30)

a.right(60)
a.backward(110)

a.goto(0, 0)
a.right(60)
a.forward(250)

a.left(120)
a.forward(30)

a.left(60)
a.forward(190)
a.goto(0, 0)
a.end_fill()
a.goto(0, -56)

a.color("black")
a.goto(0, -155)
a.left(120)
a.forward(50)

a.color("white")
a.fillcolor("#FFFFFF")
a.begin_fill()

a.backward(400)
a.left(90)
a.forward(25)
a.right(90)
a.forward(245)

a.right(60)
a.backward(43)

a.left(60)
a.forward(30)

a.right(60)
a.forward(43)

a.left(60)
a.forward(140)

a.right(120)
a.forward(30)
a.end_fill()

a.right(60)
a.forward(400)

a.write("PPARKY", font=("ABeeZee", 49, "normal"), align="right")

a.hideturtle()
time.sleep(100)
