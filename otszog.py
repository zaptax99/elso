import turtle

def otoszog():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    for _ in range(5):
        turtle.forward(200)
        turtle.left(72)

ablak = turtle.Screen()
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pensize(5)
turtle.pencolor("blue")

turtle.listen()
turtle.onkey(otoszog, "h")
turtle.onkey(turtle.bye, "q")

turtle.mainloop()
