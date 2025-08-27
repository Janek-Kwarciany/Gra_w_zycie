from Komorka import Komorka
from Plansza import Plansza
from Fabryka_komorek import FabrykaKomorek
from Obserwator import Obserwator
import sys

# Symulacja gry
class Symulacja:
    def __init__(self, plansza, obserwator):
        # Konstruktor symulacji
        # - Parametry: plansza (obiekt typu Plansza), obserwator (obiekt typu GUIWidok)
        pass

    def policz_sasiadow(self, x, y):
        # Metoda zwraca liczę żywych komórek w sąsiedztwie puntu x,y
        #  - Parametry: x, y - współrzędne komórki
        pass

    def aktualizuj(self):
        # Metoda aktualizująca stan gry
        # - Powinna iterować po planszy i zaktualizować stan komórek
        # - Można dodać logikę gry w życie (np. sprawdzanie sąsiedztwa i zmianę stanu komórek)
        pass


    if __name__ == "__main__":
    # plansza = Plansza(Plansza.SZEROKOSC, Plansza.WYSOKOSC)

    # # Tworzenie listy wszystkich możliwych współrzędnych
    # # - Użyj listy do przechowywania wszystkich możliwych pozycji
    # # - Do generowania skupień komórek możesz napisać własną funkcję
    # # losującą bez powtórzeń pary x,y należące do planszy

    # widok = GUIWidok()
    # symulacja = Symulacja(plansza, widok)
    # timer = QTimer()
    # # timer.timeout.connect(lambda: metoda_aktualizująca_symulację())
    # symulacja.aktualizuj()
    # timer.start(100)
    # widok.window.setGeometry(100, 100, 500, 500)
    # sys.exit(widok.app.exec_())