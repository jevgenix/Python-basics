# tee ratkaisu tänne
from datetime import datetime

paiva = int(input('Päivä: '))
kuukausi = int(input('Kuukausi: '))
vuosi = int(input('Vosi: '))

spv = datetime(vuosi, kuukausi, paiva)
vv = datetime(1999, 12, 31)
if spv < vv:
    ero = vv - spv
    print(f"Olit {ero.days} päivää vanha, kun vuosituhat vaihtui.")
else:
    print('Et ollut syntynyt, kun vuosituhat vaihtui.')
