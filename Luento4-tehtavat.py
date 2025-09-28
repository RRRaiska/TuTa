# esimerkki 1.
kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt < kerrat:
    print("Hyvää huomenta")
    tehdyt = tehdyt + 1

# esimerkki 2.
komento = input("Anna komento: ")
while komento != "lopeta":
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print("Toiminnot lopetettu.")

# esimerkki 3.
import random
noppa1 = noppa2 = heitot = 0
while (noppa1!=6 or noppa2!=6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")

# esimerkki 4.
eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1
