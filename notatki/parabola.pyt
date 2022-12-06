import numpy as np
import matplotlib.pyplot as plt

a = int(input("podaj wspolczynik a paraboli"))
b = int(input("podaj wspolczynik b paraboli"))
c = int(input("podaj wspolczynik c paraboli"))

x = np.linspace(-10, 10, 100)

y = a*x**2 + b*x + c

plt.plot(x,y)
plt.show()