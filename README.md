# Tavak adatainak elemzése 🌊

Python script, amely egy szövegfájlból betölti a tavak adatait, és kérdések sorára válaszol velük kapcsolatban.

## Mit csinál?

- Az adatokat egy saját `To` osztályba tölti be (név és terület)
- Megkeresi a legnagyobb tavat és a legkisebb területet
- Megszámolja a 100-nál nagyobb területű tavakat
- Megvizsgálja, van-e 500-nál nagyobb területű tó, illetve P betűvel kezdődő nevű tó (lineáris keresés)
- Összegzi a tavak teljes területét
- Tartalmaz egy függvényt, amely kiszámolja, hogy a tavak Svájc területének (41 285) hány százalékát teszik ki
- A 300-nál nagyobb területű tavakat kiírja a `nagytavak.txt` fájlba

## Bemeneti fájl formátuma

A `tavak.txt` soronként egy tavat tartalmaz, tabulátorral elválasztva, a terület tizedesvesszővel:

```
név	terület
```

## Technológiák

Python 3, osztályok, fájlkezelés

## Futtatás

Tedd a `tavak.txt` fájlt a script mellé ugyanabba a mappába, majd futtasd:

```
python tavak.py
```
