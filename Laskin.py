print("-------Tervetuloa käyttämään laskinta!-------")
print("Valitse mitä toimintoa haluat käyttää? \n A: Yhteenlasku \n B: Vähennyslasku"
      "\n C: Kertolasku \n D: Jakolasku ")
valinta = input("Valintasi (A - D): ").upper()

#Lukuja voi sekoittaa keskenään, mutta lukuja ja merkkijoukkoa ei voi ilman, että sen castaa.
a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))

if valinta == "A":
    print("Yhteenlasku:", a + b)
elif valinta == "B":
    print("Vähennyslasku:", a - b)
elif valinta == "C":
    print("Kertolasku:", a * b)
elif valinta == "D":
    print("Desimaalijakolasku", a / b)
else:
    print("Valitasi on virheellinen.")

