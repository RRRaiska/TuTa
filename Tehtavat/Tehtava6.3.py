# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def bensan_maara(pyydetyt_gallonat):
    litrat = pyydetyt_gallonat * gallona
    return litrat

gallona = 3.785
pyydetyt_gallonat = float(input("Anna gallonoiden määrä? "))

while pyydetyt_gallonat >= 0:
    print(bensan_maara(pyydetyt_gallonat))
    pyydetyt_gallonat = float(input("Anna gallonoiden määrä? "))

if pyydetyt_gallonat < 0:
    print("Kiitos käynnistä.")