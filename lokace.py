import random

class Hrad:
    mistnosti = ["obývák", "chodba", "sklep", "trůnní sál"]
    chodby = [[1, 2], [0], [0], [1, 2]]
    zamcene_chodby = [[], [3], [], []]
    klic = 2
    zlato = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 15000)]
    jmeno = "Hrad"

class Posta:
    mistnosti = ["vchod", "hala", "za prepazkou", "trezor"]
    chodby = [[1, 2], [0], [0], [1, 2]]
    zamcene_chodby = [[], [3], [], []]
    klic = 1
    zlato = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 2500)]
    jmeno = "Posta"

class Chalupa:
    mistnosti = ["obejvak", "pokoj", "dedecek", "suplik"]
    chodby = [[1, 2], [0, 3], [0], [1]]
    zamcene_chodby = [[], [], [], [3]]
    klic = 1
    zlato = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 5000)]
    jmeno = "Chalupa"