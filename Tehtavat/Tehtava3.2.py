#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
#(LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
#Tehtävässä on käytettävä if/elif/else-toistorakennetta.

hLuokka = (input("\nKerro minkä hyttiluokan haluaisit: LUX, A, B vai C? \n"))

if hLuokka == "LUX" or "Lux":
    print("\nLUX on parvekkeellinen hytti yläkannella.")

elif hLuokka == "A" or "a":
    print("\nA on ikkunallinen hytti autokannen yläpuolella.")

elif hLuokka == "B" or "b":
    print("\nB on ikkunaton hytti autokannen yläpuolella.")

elif hLuokka == "C" or "c":
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")



