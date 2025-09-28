# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

kayttajatunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")

while salasana != "Python123!":
    print(f"Pääsy evätty.")
    salasana = input("Anna salasana: ")

else:
    print("Tervetuloa!")