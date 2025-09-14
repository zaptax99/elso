# elso program
# Ez a főprogram, ami importálja és használja a modulban írt függvényeket10

import modul

# Felhasználótól kérünk be két számot
elso = int(input("Add meg az első számot: "))
masodik = int(input("Add meg a második számot: "))

# Használjuk a modulban definiált függvényeket
osszeg = modul.osszead(elso, masodik)
szorzat = modul.szoroz(elso, masodik)

# Eredmények kiírása
print(f"\nAz általad megadott számok: {elso} és {masodik}")
print(f"Összegük: {osszeg}")
print(f"Szorzatuk: {szorzat}")

