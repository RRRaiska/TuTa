numerot = {"viivi":"050-1234567",
           "ahmed":"040-1456987",
           "pekka":"050-9876541"}

# alkiot voi sisältää useita asioita. Esim Viivi voisi olla opettaja ja numero
# voisi olla kurssit joita viivi opettaa.
# pekka voi olla myös numero ja puhelinnumero voi olla myös numero eikä str.

print(numerot)

#miten lisätään numero luetteloon? avaimiin viitataan hakasuluilla
numerot["Olga"] = "045-1234567"
print(numerot)

#numeron vaihtaminen
numerot["viivi"] = "040-1234567"
print(numerot)

# miten etsitään numeroa?
nimi = input("Anna etsimäsi henkilön nimi: ")

if nimi in numerot: #jos nimi on numerot-listalla niin se etsitään.
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")
