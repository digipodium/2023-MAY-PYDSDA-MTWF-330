from turtle import *
from polygon import *

speed('fastest')

for i in range(6):
    hexagon(100)
    for i in range(6):
        hexagon(50)
        circle(50)
        lt(65)
    lt(50)

hideturtle()
mainloop()