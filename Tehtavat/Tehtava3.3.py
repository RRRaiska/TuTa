# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Kirjoita biologinen sukupuolesi (nainen/mies): ")
hemoglobiini = int(input("Mikä on hemoglobiiniarvosi? "))

nainen = "nainen"
mies = "mies"

if sukupuoli == nainen and hemoglobiini < 117:
    print("Hemoglobiinisi on alhainen. ")
if sukupuoli == nainen and hemoglobiini >= 117 and hemoglobiini < 175:
    print("Hemoglobiinisi on normaali. ")
if sukupuoli == nainen and hemoglobiini >= 175:
    print("Hemoglobiinisi on korkea. ")

if sukupuoli == mies and hemoglobiini < 134:
    print("Hemoglobiinisi on alhainen. ")
if sukupuoli == mies and hemoglobiini >= 134 and hemoglobiini < 195:
    print("Hemoglobiinisi on normaali. ")
if sukupuoli == mies and hemoglobiini >= 195:
    print("Hemoglobiinisi on korkea. ")
