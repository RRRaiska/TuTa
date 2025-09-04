#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
#montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = float(input("\nOnnea! Ahti tarjosi antejaan. \n"
                   "Tarkistetaan kuitenkin onhan kuhasi riittävän suuri ruokapöytään. \n"
                   "\nKerro siis kalastamasi kuhan pituus senttimetreissä: \n"))

if kuha < 37 :
    print(f"Voi sentään. Tämä yksilö on vielä liian pieni. Siltä puuttuu {37 -kuha} senttimetriä mitasta. \n"
          f"Päästähän hänet takaisin kasvamaan! \n")

else:
    print("Mahtavaa, tämä yksilö on jo riittävän suuri!")