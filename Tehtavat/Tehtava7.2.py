# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
# jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
# nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien
# tallentamiseen.

nimet = set()
nimi = input("Anna nimi? (Tyhjä lopettaa syöttämisen.) ")

while nimi != "":
    nimet.add(nimi)
    nimi = input("Anna nimi? (Tyhjä lopettaa syöttämisen.) ")
    if nimi in nimet != nimi:
        print("Uusi nimi.")
else:
    print("Aiemmin syötetty nimi.")



print(nimet)

