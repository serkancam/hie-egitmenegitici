# -*- coding: utf-8 -*-

import turtle

cizim = turtle.Turtle()

cizim.circle(50)

turtle.mainloop()


#%%
import turtle
cizim = turtle.Turtle()


cizim.penup()
cizim.setpos(50,50)
cizim.pendown()
cizim.circle(30)
turtle.mainloop()

#%%

import turtle
painter = turtle.Turtle()
painter.pencolor("blue")

for i in range(100):
    painter.forward(100)
    painter.left(120)


painter.fd()
turtle.done()
