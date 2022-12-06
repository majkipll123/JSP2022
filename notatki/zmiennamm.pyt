import math
def funkcja(r,zmienna):
    if zmienna == "m":
        print("Pole = ", math.pi*r*r,"m^2")
    elif zmienna == "cm":
        print("Pole = ", (math.pi*r*r)/10000,"cm^2")
    elif zmienna == "mm":
        print("Pole = ", (math.pi * r * r )/ 1000000, "mm^2")


r = float(input("Wpisz promien "))
zmienna = input("Wpisz jednostke ")

funkcja(r,zmienna)