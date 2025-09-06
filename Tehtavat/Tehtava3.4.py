# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain,
# jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Mikä vuosi on? "))

# En osannut tarkistin netistä oikean vastauksen. Alla räpellykseni.
# Yritin myös sulkeita kuten oikeassakin tavassa, mutta multa puuttui tuo == 0.

# if vuosi == vuosi % 100 and vuosi % 400:
  #  print("Tämä on karkausvuosi. ")

# if vuosi == vuosi % 4:
 #   print("Tämä on karkausvuosi. ")


if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print("Tämä on karkausvuosi. ")

