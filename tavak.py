# Hozzon létre osztályt To néven!

class To:
    def __init__(self,nev,terulet):
        self.nev = nev
        self.terulet = terulet

# Importálja a tavak.txt fájl tartalmát egy megfelelő adatszerkezetbe úgy, hogy To típusúak legyenek!
# Az adatokat tabulátor választja el!

tavak = list()

with open("tavak.txt",'r',encoding="UTF-8") as f:
    for sor in f:
        adatsor = sor.strip().split("\t")
        adatsor[1] = float(adatsor[1].replace(',','.'))
        t = To(adatsor[0],adatsor[1])
        tavak.append(t)

# Adja meg a legnagyobb tó nevét!

maxnev = tavak[0].nev
maxterulet = tavak[0].terulet

for to in tavak:
    if to.terulet > maxterulet:
        maxterulet = to.terulet
        maxnev = to.nev

print(maxnev)

# Adja meg a legkisebb tó területét!

minterulet = tavak[0].terulet

for to in tavak:
    if to.terulet < minterulet:
        minterulet = to.terulet
print(minterulet)

# Adja meg, hány 100 négyzetméternél nagyobb területű tó van!

i = 0
for to in tavak:
    if to.terulet > 100:
        i += 1
print(f"{i} db")

# Adja meg van-e 500 négyzetméternél nagyobb területű tó!

x = 0
while x < len(tavak) and not tavak[x].terulet > 500:
    x += 1

if x < len(tavak):
    print("Van 500 négyzetméternél nagyobb területű tó.")
else:
    print("Nincs 500 négyzetméternél nagyobb területű tó.")
print(x)

# Adja meg a tavak területének összegét!

osszterulet = 0
for to in tavak:
    osszterulet += to.terulet
print(osszterulet)

# Adja meg van-e P-vel kezdődő nevű tó!

p = 0
while p < len(tavak) and not tavak[p].nev.startswith('P'):
    p += 1
if p < len(tavak):
    print("Van P-vel kezdődő nevű tó.")
else:
    print("Nincs P-vel kezdődő nevű tó.")

# Készítsen függvényt, amely megadja, hogy ezek a tavak hány %-át teszik ki Svájc területének, ha tudja, hogy az 41285!

def Svajc(osszterulet):
    szazalek = osszterulet/41285*100
    return szazalek

# Írjuk ki a 300 négyzetkilométernél nagyobb tavakat a nagytavak.txt fájlba!

with open("nagytavak.txt",'w',encoding="UTF-8") as n:
    for to in tavak:
        if to.terulet > 300:
            n.write(f"{to.nev} {to.terulet}\n")