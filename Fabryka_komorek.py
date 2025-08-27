from Komorka import Komorka

class FabrykaKomorek(Komorka):
    @staticmethod
    def utworz_komorke(typ):
        if typ == 'zywa komorka':
            return Komorka(zywa=True)
        elif typ == 'martwa komorka':
            return Komorka(zywa=False)
        else:
            raise ValueError("Nieznany typ komórki")
