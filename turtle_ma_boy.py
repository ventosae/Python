import turtle
def draw_all():
    draw_circle2()
    draw_circle()
    draw_triangle()
    draw_shape()


    
def draw_shape():
    wn = turtle.Screen()
    wn.bgcolor("lightgrey")
    marine = turtle.Turtle()
    marine.shape("triangle")
    marine.color("gold")
    marine.speed(50)
    for i in range(180):
        marine.forward(100)
        marine.right(30)
        marine.forward(20)
        marine.left(60)
        marine.forward(50)
        marine.right(30)
        for m in range(3):
            marine.penup()
            marine.setposition(0, 0)
            marine.pendown()
            
            marine.right(2)


def draw_circle():
    wn = turtle.Screen()
    wn.bgcolor("lightgrey")
    sure = turtle.Turtle()
    sure.shape("triangle")
    sure.color("yellow")
    sure.speed(50)
    p = 1   
    for i in range(80):
        sure.circle(3)
        while p<i:
            p = p+1
            sure.circle(p)
            sure.setposition(p, 0)

def draw_circle2():
    wn = turtle.Screen()
    wn.bgcolor("lightgrey")
    s = turtle.Turtle()
    s.shape("triangle")
    s.color("yellow")
    s.speed(50)
    p = 1   
    for i in range(80):
        s.circle(3)
        while p<i:
            p = p+1
            s.circle(p)
            s.setposition(p, 0) 


def draw_triangle():
    wn = turtle.Screen()
    wn.bgcolor("lightgrey")
    h = turtle.Turtle()
    h.shape("triangle")
    h.color("peru")
    h.speed(50)
    p = 180  
    for i in range(8):
        h.forward(100) 
        h.left(120)
        h.forward(100)
        h.left(120)
        h.forward(100)



    
##    sur = turtle.Turtle()
##    surski = turtle.Turtle()
##
##    sur.shape("triangle")
##    sur.color("gold")          
##    sure.forward(100)
##    sure.left(90)
##    marine.forward(100)
##    marine.left(90)
##    marine.forward(100)
##    marine.left(90)
##    marine.forward(100)
##    marine.left(90)
##    marine.forward(100)
##    sur.circle(200)           
##    for i in range(12):
##        for c in range(12):
##            c = c + 10
##            marine.speed(5)
##            marine.left(90)
##            marine.forward(100)
##            marine.left(c)
##            marine.forward(100)
##            marine.left(c)
##            marine.forward(100)
##            marine.left(90)
##            marine.forward(100)
draw_all()
 

 

 
 
