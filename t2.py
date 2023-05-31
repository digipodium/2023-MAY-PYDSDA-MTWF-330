from turtle import *

speed('slowest')
for i in range(5):
    pencolor('red')
    pensize(5)
    fd(200)
    lt(360/5)
    for j in range(5):
        pencolor('blue')
        pensize(1)
        fd(60)
        lt(360/5)
        write(f'{i},{j}')
mainloop()