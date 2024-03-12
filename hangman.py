import random

x = random.choice(["slovo", "jmeno", "kokos", "ne", "matematika"])

print("zahrajme si sibenici")

pokusy = 0
while True:
    hadane_pismeno = int(input("hadej pismeno"))
    pokusy += 1

    if hadane_pismeno == x:
        print("vyhral jsi za", pokusy, "krok/y")
        break

    elif hadane_pismeno != x:
        print("tohle pismeno neni ve slove")

