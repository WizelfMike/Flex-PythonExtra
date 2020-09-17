import turtle

turtle.bgcolor("black")
turtle.pencolor("white")
turtle.setx(200)
turtle.clear()

for x in range(5):

 for x in range(40):
     turtle.forward(10)
     turtle.right(30)
     turtle.forward(20)
     turtle.right(30)
     turtle.left(45)
     turtle.forward(5)

 for x in range(44):
     turtle.left(30)
     turtle.forward(10)
     turtle.left(30)
     turtle.forward(20)


turtle.done()