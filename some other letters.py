from letters import *

word = textinput("letter drawing program", "make a word using some of these letters: a, f, h, i, j, k, l, m, o, p, r, s, x, y, z")

for letter in word:
    if letter == "a":
        pismeno_a()
        penup()
        forward(40)
        pendown()
    elif letter == "f":
        pismeno_f()
        penup()
        forward(40)
        pendown()
    elif letter == "h":
        pismeno_h()
        penup()
        forward(40)
        pendown()
    elif letter == "i":
        pismeno_i()
        penup()
        forward(40)
        pendown()
    elif letter == "j":
        pismeno_j()
        penup()
        forward(40)
        pendown()
    elif letter == "k":
        pismeno_k()
        penup()
        forward(40)
        pendown()
    elif letter == "l"  :
        pismeno_l()
        penup()
        forward(40)
        pendown()
    elif letter == "m":
        pismeno_m()
        penup()
        forward(40)
        pendown()
    elif letter == "o":
        pismeno_o()
        penup()
        forward(40)
        pendown()
    elif letter == "p":
        pismeno_p()
        penup()
        forward(40)
        pendown()
    elif letter == "r":
        pismeno_r()
        penup()
        forward(40)
        pendown()
    elif letter == "s":
        pismeno_s()
        penup()
        forward(40)
        pendown()
    elif letter == "x":
        pismeno_x()
        penup()
        forward(40)
        pendown()
    elif letter == "y":
        pismeno_y()
        penup()
        forward(40)
        pendown()
    elif letter == "z":
        pismeno_z()
        penup()
        forward(40)
        pendown()
    else:
        break
exitonclick()