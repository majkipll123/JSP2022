import matplotlib.pyplot as plt
import numpy as np 
#rzut ukośny
Vo=float(input("Podaj prędkość początkową: "))
alfa=float(input("Podaj kąt: "))
g=9.81
t=np.linspace(0,10,100)
x=Vo*np.cos(alfa)*t

y=Vo*np.sin(alfa)*t-0.5*g*t**2
#zwracanie maksymalnej wartosci y
print("Maksymalna wysokość: ",np.max(y))
#zwraca zasieg w chwili koncowej x=0 
print("Zasięg: ",np.max(x))
#zwraca czas 
print("Czas: ",np.max(t))
#rysowanie trzeh wykresów 
#pierwszy wykres na ktorym widac predkosc chwilowa w kierunku pionowym i pozniomym po czasie
plt.subplot(3,1,1)
plt.plot(t,Vo*np.sin(alfa)-g*t)
plt.plot(t,Vo*np.cos(alfa))
plt.xlabel("t")
plt.ylabel("v")
plt.title("Rzut ukośny")


#drugi wykres na ktorymn widac polozenmie funkcji czasu
plt.subplot(3,1,2)
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Rzut ukośny")
#trzeci wykres na ktorymn widac wykres toru rzutu ukosnego
plt.subplot(3,1,3)
plt.plot(t,y)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Rzut ukośny")
plt.show()
