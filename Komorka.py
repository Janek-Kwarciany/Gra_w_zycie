import random

class Komorka:
    def __init__(self, zywa=True):
        self.zywa = zywa

    def zmien_stan(self, stan):
        self.zywa = stan
