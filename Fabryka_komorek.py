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