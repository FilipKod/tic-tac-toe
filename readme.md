# Piskvorky

- dvaja hraci
- hrac cislo 1 zapisuje pomocou symbolu X
- hrac cislo 2 zapisuje pomocou symbolu O
- hra konci ked:
    - jeden z hracov vyplni:
        - cely riadok
        - cely stlpec
        - alebo jeden z diagonalov
    - skoncit remizou vyplenim vsetkych policok oboma hracmi bez toho ze by niekto z nich dokazal vyplnit riadok, stlpec alebo diagonal
- kazde kolo sa zacne napisom: ***Vitajte v kole X***
- pred kazdym tahom hraca sa vypise hracia plocha
- na hraciu plochu treba pouzit vnorene polia
- na vypisanie prazdneho miesto pouzite symbol **podtrzniku**
- na zadanie tahu treba zadat dve suradnice pomocou standartneho vstupu
- suradnica **moze** byt index v tom danom poli
    - ja by som ale pouzil oznacenie ako na sachovnici
- implementacia osetrenia chyb
    - ak hrac zada suradnicu ktora sa nenachadza v poli
    - ak hrac zada omylom pismeno alebo cislo tam kde nema
    - ostrenie vyhodnocovania hry
        - remiza alebo vyhra jedneho z hracov
- kod rozdelit do modulov a logicky ich usporiadat
- dodrziavanie konvecie
    - anglicke nazvy
    - snake case


### Moznosti ako rozhodnut ktory hrac bude mat ***X*** a ktory ***O***:
1. Hrac cislo 1 si vybere ci bude pouzivat **X** alebo **O** a pocitac vybere ktori zacne
2. Pocitac automaticky po zadani mena vypise ci bude hrac pouzivat **X** alebo **O**