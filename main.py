from Plansza import Plansza
from Komorka import Komorka
from Fabryka_komorek import FabrykaKomorek
import random
import time

wysokosc = 10
szerokosc = 10

def losuj_stan_komorki():
    stan = {
        1 : 'zywa komorka',
        2 : 'martwa komorka'
    }

    wylosuj = random.randint(1, 2)
    return stan[wylosuj]

# def policz_sasiadow(plansza, x, y):
#     for x in range(len(plansza)):
#         for y in range(len(plansza[x])):
#             print(f"plansza[{y}] = {plansza[x]}")

#     kierunek = [(-1, 0), (1, 0), (0, -1), (0, 1),
#             (-1, -1), (-1, 1), (1, -1), (1, 1)]

#     sasiedzi = []

#     for dx, dy in kierunek:
#         nx,ny = x + dx, y +dy
#         if 0 <= nx < len(plansza) and 0 <= ny < len(plansza[0]):
#             sasiedzi.append(plansza[nx][ny])


#     print(f'Sasiedzi elemntu tablicy[{x}][{y}] = {plansza[x][y]} to : {sasiedzi}')
    
#     # Metoda zwraca liczę żywych komórek w sąsiedztwie puntu x,y
#     #  - Parametry: x, y - współrzędne komórki


def policz_sasiadow(plansza, x, y):
    sasiedzi = []
    if (x > 0) and (x < 9) and (y > 0) and (y < 9): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x == 0) and (x < 9) and (y > 0) and (y < 9): 
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x > 0) and (x < 9) and (y == 0) and (y < 9): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x > 0) and (x == 9) and (y > 0) and (y < 9): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x > 0) and (x < 9) and (y > 0) and (y == 9): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))
    elif (x == 0) and (y == 0):
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x == 0) and (y == 9): 
        sasiedzi.append(plansza.pobierz_komorke(x + 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))
    elif (x == 9) and (y == 0): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y + 1))
    elif (x == 9) and (y == 9): 
        sasiedzi.append(plansza.pobierz_komorke(x - 1, y))
        sasiedzi.append(plansza.pobierz_komorke(x, y - 1))

    ilosc_zywych_komorek = 0

    for sasiad in sasiedzi:
        if sasiad.pobierz_stan() == True:
            ilosc_zywych_komorek += 1
    
    return ilosc_zywych_komorek

if __name__ == "__main__":
    # tworzymy nową planszę
    plansza = Plansza(szerokosc, wysokosc)
    # inicjalizujemy planszę wylosowanymi komórkami
    for x in range(wysokosc):
        for y in range(szerokosc):
            plansza.ustaw_komorke(x, y, FabrykaKomorek.utworz_komorke(losuj_stan_komorki()))

    while 1:
        for x in range(wysokosc):
            for y in range(szerokosc):
                ilosc_zywych = policz_sasiadow(plansza, x, y)
                
                # warunek narodziny
                if plansza.pobierz_komorke(x, y).pobierz_stan() == False:
                    if ilosc_zywych == 3:
                        plansza.pobierz_komorke(x, y).zmien_stan(True)
                
                # warunek smierc
                if plansza.pobierz_komorke(x, y).pobierz_stan() == True:
                    if ilosc_zywych < 2 or ilosc_zywych > 3:
                        plansza.pobierz_komorke(x, y).zmien_stan(False)
                # print(f"x: {x}, y: {y}, ilosc zywych sasiadow {ilosc_zywych}")

        for y in range(wysokosc):
            for x in range(szerokosc):
                stan = plansza.pobierz_siatke()[y][x].pobierz_stan()
                print(f"{stan}", end=' ')
            print("\n")
        
        print("\n")
        time.sleep(1)

print(plansza)
