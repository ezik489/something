import random

x = random.randint(1, 100)

pokusy = 0
while True:
    hadane_cislo = int(input("hadej cislo"))
    pokusy += 1

    if hadane_cislo == x:
        print("vyhral jsi za", pokusy, "krok/y")
        break

    elif hadane_cislo > x:
        print("cislo je mensi")

    elif hadane_cislo < x:
        print("cislo je vetsi")



