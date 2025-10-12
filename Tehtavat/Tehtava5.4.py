# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin.
# Käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
# niiden läpikäymiseen.

kaupungit = []

for x in range(0,5):
    kaupunki = input("Kaupungin nimi? ")
    kaupungit.append(kaupunki)
    print(kaupungit)

for item in kaupungit:
    print(item)

