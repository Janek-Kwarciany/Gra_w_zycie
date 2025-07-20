from noName import Komorka

z = Komorka(zywa=True)
m = Komorka(zywa=False)

tablica = [
(z, z ,m, z, m, m, z, z, z, m),
(z, m ,z, z, m, z, m, m, z, m),
(z, z ,z, z, m, z, z, m, z, z),
(z, z ,z, z, m, m, z, z, z, z),
(m, z ,z, z, m, m, m, z, z, z),
(z, z ,z, m, m, z, m, z, z, z),
(z, z ,z, m, m, z, m, z, z, z),
(m, z ,z, z, z, z, m, z, m, z),
(z, z ,m, z, z, z, z, m, z, z),
(z, z ,m, m, m, m, m, m, z, m),
(z, m ,m, z, z, m, z, z, z, z) ]

for row in tablica:
    for element in row:
        
        print(element)
print()
