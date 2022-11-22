import turtle

screen=turtle.Screen()
screen.title("pn")

pen_ontario = turtle.Turtle()
pen_ontario.color("blue")



ontario = [100,105,200,300,400,1000,2000,2500,3000,4000,5000,5550]

startx = -500
starty = -500
pen_ontario.penup()
pen_ontario.goto(startx,starty)
pen_ontario.pendown()

penx = turtle.Turtle()
penx = turtle.Turtle()
penx.color("red")
penx.penup()
penx.goto(startx,starty)
penx.pendown()
penx.goto(-startx,starty)

peny = turtle.Turtle()
peny = turtle.Turtle()
peny.color("red")
peny.penup()
peny.goto(startx,starty)
peny.pendown()
peny.goto(startx,-starty)


# draw graph for ontario
for i in range (len(ontario)):
    x = i * 20
    y = ontario[i]/20
    pen_ontario.goto(x + startx, y + starty)

turtle.exitonclick()
