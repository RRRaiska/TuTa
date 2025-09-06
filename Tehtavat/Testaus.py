# Pyydetään käyttäjältä hyttiluokkaa
hyttiluokka = input("Syötä hyttiluokka (LUX, A, B, C): ")

# Tarkistetaan syöte ja tulostetaan kuvaus
if hyttiluokka == "LUX":
    print("LUX: Ylimmän kerroksen sviitti parvekkeella.")
elif hyttiluokka == "A":
    print("A: Hytissä on parveke.")
elif hyttiluokka == "B":
    print("B: Hytissä ei ole ikkunaa.")
elif hyttiluokka == "C":
    print("C: Sisähytti ilman ikkunaa.")
else:
    print("Tuntematon hyttiluokka. Valitse LUX, A, B tai C.")