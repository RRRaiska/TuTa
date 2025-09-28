# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm.

tuumat = int(input("Tämä ohjelma muuttaa tuumia senttimetreiksi. Anna tuumamäärä, jonka haluat muutettavan: "))
tuuma = 2.54
tuumamaara = tuuma * tuumat
while tuumamaara >= 1:
    print(f"Antamasi tuumamäärä on {tuumamaara} senttimetriä.")
    tuumat = int(input("Tämä ohjelma muuttaa tuumia senttimetreiksi. Anna tuumamäärä, jonka haluat muutettavan: "))
    tuumamaara = tuuma * tuumat
    if tuumamaara <= 1:
        print("Annoit negatiivisen luvun. Anna positiivinen luku.")


