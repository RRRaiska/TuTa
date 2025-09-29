# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

kayttajatunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
toistot = 0

while toistot < 5:
    toistot += 1
    while kayttajatunnus != "python":
        while salasana != "rules":
            print(f"Pääsy evätty.")
            kayttajatunnus = input("Anna käyttäjätunnus: ")
            salasana = input("Anna salasana: ")
print("Tervetuloa!")

# en osannut tehdä 5 kerran looppia.