# osa 1
# Luo sanakirja oppilaista ja kursseista, joille he ovat ilmoittautuneet. Sanakirjassa avain on oppilaan nimi ja arvo on lista kursseista,
# joilla oppilas on. Luo sanakirja, jossa on valmiiksi ainakin 3 oppilasta kursseineen.
# Tulosta koko sanakirja arvoineen allekkaisille riveille.

#osa 3
# Kirjoita funktio, jossa käyttäjältä kysytään kurssi, jonka osallistujamäärän
# hän haluaa tarkistaa. Funktio laskee ja tulostaa kyseiselle kurssille
# ilmoittautuneiden oppilaiden määrän sanakirjan perusteella.

def osallistujat(sanakirja):
    kurssi = input("Anna kurssin nimi, jonka osallistujamäärän haluat tietää: ")
    maara = 0

    for nimi,kurssit in sanakirja.items():
        if kurssi in kurssit:
            maara += 1
    return


oppilaat = {
    "Milla": ["matikka", "vitutus", "saatanan palvonta"],
    "Pekka": ["biologia", "kusipäiden tunnistaminen"],
    "Maija": ["historia", "vittuilun masterclass", "huutaminen"]
}

for nimi, kurssit in oppilaat.items():
    print(nimi, ":", kurssit)

# Kysy käyttäjältä uusi oppilas kursseineen lisättäväksi sanakirjaan. Kysy käyttäjältä kursseja,
# kunnes käyttäjä syöttää tyhjän. Tulosta uudelleen koko sanakirja, jotta näet että oppilas on lisätty.


uusiOppilas = input("Mikä on oppilaan nimi? ")
opinnot = []
print("Anna seuraavaksi oppilaan kurssit. ")

while True:
    kurssi = input("Anna seuraava kurssi: ")
    if kurssi == "":
        break
    opinnot.append(kurssi)

oppilaat[uusiOppilas] = opinnot
oppilasmaara = osallistujat(oppilaat)
print(f"Kurssille osallistuu {oppilasmaara} oppilasta.")

for n in oppilaat.items():
    print(n)

