import turtle

t = turtle.Pen()

# chassis
t.reset()
t.color(1, 0 ,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()

# achterwielen
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()


t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

# verder leren
t.up()
t.forward(70)
t.down()

def mijncirkel(rood, groen, blauw):
    t.color(rood, groen, blauw)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

#1 = 100
mijncirkel(0.15, 0.45, 0.5)





turtle.mainloop()
