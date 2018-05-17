# w zmiennej dane przechowywana jest zawartość pliku punkty.txt
fr = open("punkty.txt", "r")
dane = fr.read()
fr.close()

# zmienna koniec zawiera indeksy, w których następuje przejście do nowej lini
koniec = [-1]
for x in range(len(dane)):
    if dane[x] == "\n":
        koniec.append(x)

# zmienna wiersze jest ulogicznioną bazą danych, każdy klucz zawiera informacje na temat jednego wiersza
wiersze = []
for x in range(1, len(koniec)):
    wiersze.append(dane[koniec[x-1]+1: koniec[x]])

def wnetrze_kola(a, b, r, ilosc=len(wiersze)):
    wnetrze = []
    for wiersz in wiersze[:ilosc]:
        przerwa = wiersz.index(" ")
        x = int(wiersz[0:przerwa])
        y = int(wiersz[przerwa+1:])
        if (x-a)**2 + (y-b)**2 < r**2:
            wnetrze.append(wiersz)
    return wnetrze

def brzeg_kola(a, b, r):
    brzeg = []
    for wiersz in wiersze:
        przerwa = wiersz.index(" ")
        x = int(wiersz[0:przerwa])
        y = int(wiersz[przerwa+1:])
        if (x-a)**2 + (y-b)**2 == r**2:
            brzeg.append(wiersz)
    return brzeg

def liczba_pi(liczba_punktow, zaokraglij=4, trzeba=True):
    p = 400**2
    r = 200**2
    n = liczba_punktow
    nk = len(wnetrze_kola(200, 200, 200, liczba_punktow))
    if trzeba == True:
        return round((nk*p)/(n*r), zaokraglij)
    elif trzeba == False:
        return (nk*p)/(n*r)

from math import pi
def blad_bzw(n):
    return abs(pi-liczba_pi(n, trzeba=False))

print("Do brzegu kola naleza punkty o wspolrzednych : ")
print(brzeg_kola(200, 200, 200))
print("Do wnetrza kola naleza punkty o wspolrzednych : ")
print(len(wnetrze_kola(200, 200, 200)), "\n")
for i in [1000, 5000, 10000]:
    print("przyblizona wartosc pi dla", i, "punktow:", liczba_pi(i))
print("\n")
for i in [1000, 1700]:
    print("blad bezwzgledny przyblizonej wartosci liczby pi z", i, "punktow:", round(blad_bzw(i),4))
