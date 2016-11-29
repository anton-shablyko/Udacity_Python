import turtle
def draw_rectangle(some_turtle):
    for y in range(4):
        some_turtle.forward(100)
        some_turtle.left(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    #1'st turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    for x in range(36):
        brad.right(10)
        draw_rectangle(brad)
    #2'nd turtle
    a = turtle.Turtle()
    a.shape("arrow")
    a.color("blue")
    a.circle(100)
    #3'd turtle
    b = turtle.Turtle()
    b.shape("circle")
    b.color("yellow")
    for x in range(3):
        b.fd(100)
        b.right(120)
    window.mainloop()

draw_art()
