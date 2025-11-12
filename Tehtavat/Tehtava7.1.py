# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


kuukaudet = ("Tammikuu","Helmikuu", "Maaliskuu" , "Huhtikuu" , "Toukokuu", "Kesäkuu" , "Heinäkuu" , "Elokuu", "Syyskuu" , "Lokakuu" , "Marraskuu","Joulukuu")

kuukaudenNumero = int(input("Kerro kuukauden numero (1-12)? "))
kuukausi = kuukaudet[kuukaudenNumero-1]

if kuukaudenNumero == 11 or kuukaudenNumero == 0 or kuukaudenNumero == 1:
    print("Vuodenaika on talvi.")
if kuukaudenNumero == 2 or kuukaudenNumero == 3 or kuukaudenNumero == 4:
    print("Vuodenaika on kevät.")
if kuukaudenNumero == 5 or kuukaudenNumero == 6 or kuukaudenNumero == 7:
    print("Vuodenaika on kesä.")
if kuukaudenNumero == 8 or kuukaudenNumero == 9 or kuukaudenNumero == 10:
    print("Vuodenaika on syksy.")

#ei toimi. ajatus ei kulje.


