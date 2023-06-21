from turtle import *

def triangle():
    for i in range(3):
        fd(100)
        lt(120)

def square():
    for i in range(4):
        fd(100)
        lt(90)

def pentagon():
    for i in range(5):
        fd(100)
        lt(72)

def hexagon(d):
    for i in range(6):
        fd(d)
        lt(60)

def septagon():
    for i in range(7):
        fd(100)
        lt(360/7)

def octagon():
    for i in range(8):
        fd(100)
        lt(45)