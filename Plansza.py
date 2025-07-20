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