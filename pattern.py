from turtle import *

speed('fastest')
for i in range(6):
    fd(100)
    lt(360/6)
    circle(50)
    for i in range(6):
        fd(50)
        lt(360/6)
        dot(10)
mainloop()