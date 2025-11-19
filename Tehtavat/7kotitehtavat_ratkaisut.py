# 7.1 Vuodenajat

vuodenajat = ("talvi", "talvi", "kevät", "kevät","kevät", "kesä","kesä","kesä","syksy","syksy","syksy", "talvi")
kk = int(input("Anna kuukauden numero (1-12): "))

vuodenaika = vuodenajat[kk-1]

print(f"Vuodenaika on {vuodenaika}.")
print("Vuodenaika on", vuodenaika,".")

# 7.2 nimi

nimet = set()
nimi = input("Anna nimi, tyhjä lopettaa: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)

    nimi = input("Anna nimi, tyhjä lopettaa: ")
print("Syötetyt nimet: ")
for n in nimet:
    print(n)

# 7.3
lentoasemat = {
    "EFHK": "Helsinki-Vantaa" ,
    "JHKY" : "Dubai",
    "KERF" : "Oslo"
}

while True:
    print("Valitse toiminto: A = Syötä, B = Hae, Q = lopeta: ")
    valinta = input("Mitä haluat tehdä?").upper()
    if valinta == "A":
        icao = input("Anna lentoaseman icao-koodi: ")
        nimi = input("Anne lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Uusi arvo tallennettu.")

    elif valinta == "B":
        icao = input("Anna lentoaseman icao-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi" , lentoasemat[icao])
        else:
            print("Koodilla ei löydy nimeä.")

    elif valinta == "Q":
        print("Ohjelma päättyy...")
        break

    else:
        print("Virheellinen valinta.")

print("Kiitos, hei!")




