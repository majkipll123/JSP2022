import numpy as np
import matplotlib.pyplot as plt

t=1
Vo=1
alfa=1
x=1
y=1

#wykres predkosci w kierunku poziomym i pionowym
plt.plot(t,Vo*np.cos(alfa),label="Poziomo")
plt.plot(t,Vo*np.sin(alfa),label="Pionowo")
plt.xlabel("Czas")
plt.ylabel("Prędkość")
plt.title("Prędkość w kierunku poziomym i pionowym")
plt.legend()
plt.subplot(3,1,2)
#wykres położenia w czasie
plt.plot(t,x,label="Poziomo")
plt.plot(t,y,label="Pionowo")
plt.xlabel("Czas")
plt.ylabel("Położenie")
plt.title("Położenie w czasie")
plt.legend()
plt.subplot(3,1,3)
#wykres trajektorii
plt.plot(x,y)
plt.xlabel("Poziomo")
plt.ylabel("Pionowo")
plt.title("Trajektoria")
plt.show()


