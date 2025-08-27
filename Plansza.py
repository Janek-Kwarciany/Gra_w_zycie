class Plansza:
    _instancja = None

    def __new__(cls, szerokosc=10, wysokosc=10):
        cls.siatka = [[0 for x in range(szerokosc)] for y in range(wysokosc)] 
        if cls._instancja is None:
            cls._instancja = super(Plansza, cls).__new__(cls)
        return cls._instancja

    def ustaw_komorke(self, x, y, komorka):
        self.siatka[x][y] = komorka

    def pobierz_komorke(self, x, y):
        return self.siatka[x][y] 
