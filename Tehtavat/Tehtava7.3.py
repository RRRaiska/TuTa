# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.

# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.

# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.

# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.

# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

lentokentat = {}

valinta = input("Valitse seuraavista: A = uuden lentokentän tietojen syöttäminen, B = lentokentän tietojen hakeminen tai Q = ohjelman lopetus. ")

while valinta == "A":
    kentta = input("Syötä lentokentän nimi: ")
    ICAO = input("Syötä lentokentän ICAO-koodi: ")
    lentokentat.update({kentta:ICAO})
    print(lentokentat)
    valinta = input("Valitse seuraavista: A = uuden lentokentän tietojen syöttäminen, B = lentokentän tietojen hakeminen tai Q = ohjelman lopetus. ")

while valinta == "B":
    ICAO = input("Syötä ICAO-koodi: ")
    for k in lentokentat:
        print(k)
    valinta = input("Valitse seuraavista: A = uuden lentokentän tietojen syöttäminen, B = lentokentän tietojen hakeminen tai Q = ohjelman lopetus. ")

# En osannut etsiä tiettyä kenttää listalta.