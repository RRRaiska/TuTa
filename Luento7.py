viikonpaivat = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai")

paiva = int(input("Anna päivän numero (1-7): "))
p = viikonpaivat[paiva-1] #indekseihin ja sanakirjoihin viitataan hakasuluilla
print(f"Päivä numero {paiva} on {p}")
#jos haluaisi viitata monikon sisällä olevaan listaan niin siihen viitattaisiin myös tupla hakasuluilla.

