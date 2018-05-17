alfabet = []
for x in range(65, 91):
    alfabet.append(chr(x))

def szyfr(slowo, k):
    zakodowane = ""
    for litera in slowo:
        jawny = alfabet.index(litera)
        if jawny + k <= 25:
            kod = jawny + k
        else:
            kod = jawny + k%26
            if kod >= 25:
                kod = kod%26
        zakodowane += alfabet[kod]
    return zakodowane

dane = ''
def czytaj(n):
    fr = open('dane_6_'+str(n)+'.txt', 'r')
    global dane
    dane = fr.read()
    fr.close()
czytaj(1)
slowo = ''
for litera in dane:
    if litera == '\n':
        print(szyfr(slowo, 107))
        slowo = ''
    else:
        slowo += litera

def rozszyfruj(szyfr, k):
    slowo = ''
    for litera in szyfr:
        kod = alfabet.index(litera)
        if kod - k >= 0:
            jawny = kod - k
        else:
            jawny = kod - k%26
            if jawny >= 25:
                jawny = jawny%26
        slowo += alfabet[jawny]
    return slowo
print("\n")
czytaj(2)

koniec = [-1]
for x in range(len(dane)):
    if dane[x] == "\n":
        koniec.append(x)

wiersze = []
for x in range(1, len(koniec)):
    wiersze.append(dane[koniec[x-1]+1: koniec[x]])

for wiersz in wiersze:
    try:
        przerwa = wiersz.index(" ")
        print(rozszyfruj(wiersz[:przerwa], int(wiersz[przerwa+1:])))
    except (ValueError):
        print(wiersze.index(wiersz))
print("\n")

czytaj(3)
koniec = [-1]
for x in range(len(dane)):
    if dane[x] == "\n":
        koniec.append(x)

wiersze = []
for x in range(1, len(koniec)):
    wiersze.append(dane[koniec[x-1]+1: koniec[x]])
bledy = []
for wiersz in wiersze:
    przerwa = wiersz.index(" ")
    blad = True
    for x in range(26):
        if wiersz[:przerwa]==rozszyfruj(wiersz[przerwa+1:], x):
            blad = False
    if blad:
        bledy.append(wiersz)

for x in bledy:
    print(x[:x.index(" ")])
