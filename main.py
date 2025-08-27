from Plansza import Plansza
from Komorka import Komorka
from Fabryka_komorek import FabrykaKomorek
import random

wysokosc = 10
szerokosc = 10

def losuj_stan_komorki():
    stan = {
        1 : 'zywa komorka',
        2 : 'martwa komorka'
    }

    wylosuj = random.randint(1, 2)
    return stan[wylosuj]

def policz_sasiadow(plansza, x, y):
    for x in range(len(plansza)):
        for y in range(len(plansza[x])):
            print(f"plansza[{y}] = {plansza[x]}")

    kierunek = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

    sasiedzi = []

    for dx, dy in kierunek:
        nx,ny = x + dx, y +dy
        if 0 <= nx < len(plansza) and 0 <= ny < len(plansza[0]):
            sasiedzi.append(plansza[nx][ny])


    print(f'Sasiedzi elemntu tablicy[{x}][{y}] = {plansza[x][y]} to : {sasiedzi}')
    
    # Metoda zwraca liczę żywych komórek w sąsiedztwie puntu x,y
    #  - Parametry: x, y - współrzędne komórki

if __name__ == "__main__":
    plansza = Plansza(szerokosc, wysokosc)
    for x in range(wysokosc):
        for y in range(szerokosc):
            plansza.ustaw_komorke(x, y, FabrykaKomorek.utworz_komorke(losuj_stan_komorki()))

print(plansza)