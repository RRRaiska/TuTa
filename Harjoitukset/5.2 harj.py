# Luo ostoslista ostettavista tuotteista. Tee while-silmukka, jossa kysyt käyttäjältä tuotetta
# syötteenä. Ohjelman tulee poistaa tuotteet yksi kerrallaan listasta ja tulostaa jäljellä olevat
# tuotteet jokaisen ostoksen jälkeen. Jos tuotetta ei ole ostoslistalla, ilmoita siitä käyttäjälle!
from os import remove

ostoslista = ["maito", "leipä", "juusto", "leikkele", "peruna", "hedelmä", "rahka"]

tuote = input("Minkä tuotteen lisäsit ostoskoriin? ")

while tuote in ostoslista:
    print("Hyvä, tuote poistettu ostoslistalta.")
    ostoslista.remove(tuote)
    print(ostoslista)
    tuote = input("Minkä tuotteen seuraavaksi lisäsit ostoskoriin? ")

#    while ostoslista == []:
#        print("Ostoslista on tyhjä.")

    if tuote not in ostoslista:
        print("Tuote ei ole ostoslistalla.")
        tuote = input("Minkä tuotteen seuraavaksi lisäsit ostoskoriin? ")

#Miten ohjelma kertoo, että ostoslista on tyhjä? Kokeiluni ei toiminut.
