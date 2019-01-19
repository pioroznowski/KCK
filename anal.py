import pandas as pd
import aseegg as ag
import matplotlib.pyplot as plt
import numpy as np


dane = pd.read_csv("C:/Users/beton/desktop/sub-01-trial-003.csv")

df = pd.DataFrame(dane)

#wydobycie kolumn bazy danych potrzebnych do opracowania raportu
amp = df[df.columns[1]]

liczba = df[df.columns[5]]

#definiowanie czasu(liczba wierszy[7579] dzielona przez częstotliwość[200])
t = np.linspace(0, 37.895, 37.895*200)

#filtracja sygnału
bez_pradu = ag.pasmowozaporowy(amp, 200, 49, 51)
przefiltrowany = ag.gornoprzepustowy(bez_pradu, 200, 3 )


#szukanie liczby na którą mrugano
for index, wartosc in enumerate(przefiltrowany):
    if wartosc > 0.15:
        print(index,wartosc)
        print(liczba[index])

#wykresy
plt.subplot(2,1,1)
plt.title('Wykres sygnału przed filtracją')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.plot(t,amp)
plt.subplot(2,1,2)
plt.title('Wykres sygnału po filtracji')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.plot(t,przefiltrowany)
plt.show()



















#plt.plot(df[df.columns[6]])
#plt.show()
