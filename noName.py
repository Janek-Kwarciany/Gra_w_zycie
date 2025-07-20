import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QLabel
from PyQt5.QtCore import Qt, QTimer



# Singleton – zarządzanie stanem gry
class Plansza:
    _instancja = None
    SZEROKOSC = 20
    WYSOKOSC = 20

    def __new__(cls, szerokosc=10, wysokosc=10):
        # Metoda tworząca jedną instancję klasy Plansza
        # - Zapewnia, że tylko jedna instancja planszy istnieje w grze
        # - Zainicjalizuj szerokość i wysokość planszy oraz komórki

        pass

    def ustaw_komorke(self, x, y, komorka):
        # Ustawia komórkę na planszy w określonym miejscu
        # - Parametry: x (indeks w poziomie), y (indeks w pionie), komorka (obiekt typu Komorka)
        pass

    def pobierz_komorke(self, x, y, komorka):
        # zwraca komórkę o podanych współrzędnych
        # - Parametry: x (indeks w poziomie), y (indeks w pionie), komorka (obiekt typu Komorka)
        pass

#Komórka
class Komorka:
    def __init__(self, zywa=1):
        self.zywa = zywa
        # Konstruktor, który inicjalizuje stan komórki
        # - Parametr zywa określa, czy komórka jest żywa (True) czy martwa (False)
        #pass

    def zmien_stan(self, stan):
        self.zywa = stan
        # Metoda zmieniająca stan komórki
        # - Parametr stan to nowy stan komórki (True - żywa, False - martwa)
        #pass




# Fabryka komórek
class FabrykaKomorek:
    @staticmethod
    def utworz_komorke(typ):
        if typ == 'zywa komorka':
            return Komorka(zywa=True)
        elif typ == 'martwa komorka':
            return Komorka(zywa=False)


        # Fabryka do tworzenia komórek
        # - W zależności od typu ("zywa" lub "martwa") tworzy instancję odpowiedniej klasy
        #pass


# Obserwator – aktualizacja widoku
class Obserwator:
    def aktualizuj(self, plansza):
        pass


# Widok GUI
class GUIWidok(Obserwator):
    def __init__(self):
        # Konstruktor, który tworzy aplikację, okno i układ widoku
        # - Zainicjalizuj aplikację PyQt5, okno i widok
        # - Utwórz QGraphicsScene i QGraphicsView do rysowania komórek na planszy
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.layout = QVBoxLayout(self.window)
        self.label = QLabel("Gra w Życie", self.window)
        self.layout.addWidget(self.label)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self.window)
        self.layout.addWidget(self.view)
        self.window.setLayout(self.layout)
        self.window.setWindowTitle("Życie")
        self.window.show()
        pass

    def aktualizuj(self, plansza):
        # Metoda dodająca komórkę do widoku, rysując ją na planszy
        # - Jeśli komórka jest żywa, narysuj ją jako np. kolorowy prostokąt w odpowiednich współrzędnych
        # wykorzystaj metody scene.clear(), QGraphicsRectItem.setBrush(Qt.blue), scene.addItem(QGraphicsRectItem(params))

        pass


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

    print("twoze komorke")

    moja_komorka = Komorka(zywa = True)
    moja_komurkla = Komorka(1)
