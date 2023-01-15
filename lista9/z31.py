#storz program ktory oblicza maxymalna wysokosc w rzucie ukosnym, zasieg  oraz czas lotu
import matplotlib.pyplot as plt
import numpy as np
#rzut ukośny
Vo=float(input("Podaj prędkość początkową: "))
alfa=float(input("Podaj kąt: "))
g=9.81
#oblicz czas po ktorym nastapi zderzenie z ziemia
t=(2*Vo*np.sin(alfa))/g
x=Vo*np.cos(alfa)*t
y=Vo*np.sin(alfa)*t-0.5*g*t**2
#zwracanie maksymalnej wartosci y
print("Maksymalna wysokość: ",np.max(y))
#zwraca zasieg w chwili koncowej x=0
print("Zasięg: ",np.max(x))
#zwraca czas
print("Czas: ",np.max(t))
#rysowanie trzeh wykresów
plt.subplot(3,1,1)
plt.plot(t,x)
#plt.plot(t,y)
plt.xlabel("t")
plt.ylabel("v")
plt.title("Rzut ukośny")
plt.subplot(3,1,2)
plt.plot(y,x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Rzut ukośny")
plt.subplot(3,1,3)
plt.plot(t,y)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Rzut ukośny")
plt.show()

