import sys
import matplotlib.pyplot as plt

zmienne_wejsciowe = sys.argv[1:]
etykiety = []
wartosci = []

for i in range(len(zmienne_wejsciowe)):
    if i % 2 == 0:
        etykiety.append(zmienne_wejsciowe[i])
    else:
        wartosci.append(float(zmienne_wejsciowe[i]))


plt.title("Wykres słupkowy najpopularniejszych Języków programowania")
plt.bar(etykiety, wartosci)
plt.xlabel("takietam")
plt.ylabel("wartości takichtam")
plt.show()