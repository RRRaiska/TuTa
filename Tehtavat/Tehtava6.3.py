# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def bensan_maara(gallonat):
    summa = gallonat * gallona
    return summa

gallona = 3.785
gallonat = float(input("Anna gallonoiden määrä? "))

while gallonat >= 0:
    print(bensan_maara(gallonat))
    print(float(input("Anna gallonoiden määrä? ")))
    if gallonat < 0:
        print("Kiitos käynnistä.")