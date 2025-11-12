# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen
# jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
# nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien
# tallentamiseen.

nimet = set()
nimi = input("Anna nimi? (Tyhjä lopettaa syöttämisen.) ")
nimet.add(nimi)
#listan testaus
print(nimet)

while nimi != "":
    nimet.add(nimi)
    if nimi in nimet != nimi:
        print("Uusi nimi.")
    nimi = input("Anna nimi? (Tyhjä lopettaa syöttämisen.) ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")

print(nimet)
# Melkein toimii. JOstain syystä printtaa molemmat uusi ja aiemmin syötetty,
# kun koittaa jo olemassa olevaa nimeä.
