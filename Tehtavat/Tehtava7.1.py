# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
# vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.


kuukaudet = ("Tammikuu","Helmikuu", "Maaliskuu" , "Huhtikuu" , "Toukokuu", "Kesäkuu" , "Heinäkuu" , "Elokuu", "Syyskuu" , "Lokakuu" , "Marraskuu", "Joulukuu")

kuukaudenNumero = int(input("Kerro kuukauden numero (1-12)? "))
kuukausi = kuukaudet[kuukaudenNumero-1]

if kuukaudenNumero == 12 or kuukaudenNumero == 1 or kuukaudenNumero == 2:
    print(kuukausi,f" {kuukausi}n vuodenaika on talvi.")
if kuukaudenNumero == 3 or kuukaudenNumero == 4 or kuukaudenNumero == 5:
    print(kuukausi,f" {kuukausi}n vuodenaika on kevät.")
if kuukaudenNumero == 6 or kuukaudenNumero == 7 or kuukaudenNumero == 8:
    print(kuukausi,f" {kuukausi}n vuodenaika on kesä.")
if kuukaudenNumero == 9 or kuukaudenNumero == 10 or kuukaudenNumero == 11:
    print(kuukausi,f" {kuukausi}n vuodenaika on syksy.")




