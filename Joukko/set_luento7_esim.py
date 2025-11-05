autot = {"Audi","Toyota", "Nissan"}
print(autot)
#joukko/set tulee missä tahansa järjestyksessä! eli printtaa joka kerta erilailla.
# Eli näillä ei ole indeksejä. Sama arvo voi esiintyä vain kerran.

#joukkoon voi lisätä tai poistaa.
# tätä voi käyttää esim. käyttäjätunnuksien listalla. Eli ei voi olla monta samaa käyttäjätunnusta.

autot.add("Mersu")
print(autot)

autot.remove("Audi")
print(autot)

for a in autot: #tämä printtaa autot yksitellen satunnaisessa järjestyksessä ja näin voi etsiä käyttänimiä
    print(a)