import numpy as np
import matplotlib.pyplot as plt

j = int(input("wpisz liczbe calkowitą od 1 do 3 "))
x = np.linspace(-10,10,50)
y = np.linspace(-10,10,50)

if j == 1:
    plt.plot(x,y)

elif j == 2:
    plt.subplot(2,1,1)
    plt.plot(x,y)
    plt.subplot(2,1,2)
    plt.plot(y,x**2)

elif j == 3:
    plt.subplot(3,1,1)
    plt.plot(x,y)
    plt.subplot(3,1,2)
    plt.plot(y,x**2)
    plt.subplot(3,1,3)
    plt.plot(y,x**3)

plt.show()