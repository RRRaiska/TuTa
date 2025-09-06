# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

hLuokka = input("Kerro minkä hyttiluokan haluaisit: LUX, A, B vai C? ")

if hLuokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hLuokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hLuokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hLuokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

# Opettaja: Yritin tehdä koodin niin, että tämä olisi hyväksynyt myös kirjoitusasun Lux, a, b tai c.
# Olin lisännyt näin jokaiseen if hLuokka == "LUX" or "Lux": mutta se ei toiminut. Se printtasi joka kerta vastaukseksi
# tuon ensimmäisen printin eli LUX on... Mitä tein väärin?