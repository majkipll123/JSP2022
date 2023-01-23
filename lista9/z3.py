
import matplotlib.pyplot as plt
import numpy as np
import math as m
Vo=float(input("Podaj prędkość początkową: "))
alfa=float(input("Podaj kąt: "))
g=9.81
#oblicz czas po ktorym nastapi zderzenie z ziemia
t=(2*Vo*m.sin(alfa))/g
pox=abs(Vo*m.cos(alfa)*t)
poy=Vo*m.sin(alfa)*t-0.5*g*t**2
#oblicz pozycje x wzgledem czasu
x=Vo*m.cos(alfa)*t
#oblicz pozycje y po czasie
y=Vo*m.sin(alfa)*x/g-0.5*g*x**2/Vo**2*m.cos(alfa)**2
#oblicz maksymalna wysokosc
hmax=Vo**2*m.sin(alfa)**2/(2*g)
#zwracanie maksymalnej wartosci y
print("Maksymalna wysokość: ",np.max(hmax))
#zasieg w chwili koncowej x=0
print("Zasięg: ",np.max(pox))
#czas
print("Czas: ",np.max(t))
print(hmax)

#rysowanie trzeh wykresów
#pierwszy wykres zawieta predkosc chwilowa w kierunku pionowym i poziomym
#drugi wykres zawiera polozenia w funkcji czasu
#trzeci wykres zawiera tor rzutu ukośnego
plt.subplot(3,1,1)
plt.plot(t,pox,label="Poziomo")
plt.plot(t,poy,label="Pionowo")
plt.xlabel("Czas")
plt.ylabel("Prędkość")
plt.title("Prędkość w kierunku poziomym i pionowym")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,x,label="Poziomo")
plt.plot(t,y,label="Pionowo")
plt.xlabel("Czas")
plt.ylabel("Położenie")
plt.title("Położenie w czasie")
plt.legend()
plt.subplot(3,1,3)
plt.plot(x,y)
plt.xlabel("Poziomo")
plt.ylabel("Pionowo")
plt.title("Trajektoria")
plt.show()
print(t)
print(pox)
