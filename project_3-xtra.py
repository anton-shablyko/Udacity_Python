import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    a = turtle.Turtle()
    a.speed(10)
    a.color("green")
    for x in range(36):
        a.right(10)
        for i in range(6):
            a.fd(50)
            a.right(60)
    a.right(90)
    a.fd(300)
    window.mainloop()

def fractal():
    window = turtle.Screen()
    window.bgcolor("black")
    b = turtle.Turtle()
    b.color("green")
    b.speed(10)

#draw_flower()