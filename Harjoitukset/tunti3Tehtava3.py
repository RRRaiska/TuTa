luku = int(input("Anna jokin kokonaisluku: "))

#if luku % 3 == 0:
#    print("Boom")
#elif luku % 5 == 0:
#    print("Buzz")
#elif luku % 3 and 5 == 0:
#        print("BoomBuzz")

#Meni väärin, joten tässä oikea vastaus:
#Tuo viimeinen kohta pitää laittaa ensimmäiseksi.

if luku % 3 == 0 and luku % 5 == 0:
    print("BoomBuzz")
elif luku % 3 == 0:
    print("Boom")
elif luku % 5 == 0:
    print("Buzz")
