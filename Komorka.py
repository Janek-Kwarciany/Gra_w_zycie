import random

class Komorka:
    def __init__(self, zywa=True):
        self.zywa = zywa

    def zmien_stan(self, stan):
        self.zywa = stan

    def pobierz_stan(self):
         return self.zywa
