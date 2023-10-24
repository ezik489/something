import time
time.sleep(7)
from turtle import *
g = textinput("","Chose a letter, a or b: ")
def a():
    for i in range(7000000):
        forward(70)
        right(70)

def b():
    for i in range(700000):
        forward(50)
        left(50)
if g == "a":
    a()
elif g == "A":
    a()
elif g == "B":
    b()
else:
    b()

exitonclick()