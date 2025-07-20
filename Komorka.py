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