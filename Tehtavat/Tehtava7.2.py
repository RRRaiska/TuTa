# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
# jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
# nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien
# tallentamiseen.

nimet = set(input("Anna nimi? (Tyhjä lopettaa syöttämisen.) "))

while nimet != "":
    nimet = input("Anna nimi? (Tyhjä lopettaa syöttämisen.) ")
    nimet.add
    print(nimet)

