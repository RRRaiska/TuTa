# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja.
# Jos luku on pienempi kuin nolla, ohjelma tulostaa viestin "Virheellinen numero".
# Jos luku on suurempi kuin nolla, ohjelma tulostaa luvun neliöjuuren Pythonin
# sqrt-funktiolla. Molemmissa tapauksissa ohjelma kysyy sen jälkeen uutta lukua.
# Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja poistuu silmukasta.
# Esimerkki sqrt-funktion käytöstä:
import math

# from math import sqrt
# print(sqrt(9))
# Esimerkkituloste:

# Anna numero: 4
# 2.0
# Anna numero: -3
# Virheellinen numero
# Anna numero: 1
# 1.0
# Anna numero: 0
# Exiting...

kokonaisluku = int(input("Anna kokonaisluku: "))
from math import sqrt

while kokonaisluku < 0:
    print("Virheellinen luku.")
    kokonaisluku = int(input("Anna kokonaisluku: "))
while kokonaisluku > 0:
        print(math.sqrt(kokonaisluku))
        kokonaisluku = int(input("Anna kokonaisluku: "))
        if kokonaisluku == 0:
            print("Poistutaan ohjelmasta.")


