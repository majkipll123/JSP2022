import numpy as np
import sys
import os

dane = [int(line) for line in sys.stdin] if len(sys.argv) == 1 else [int(args) for args in sys.argv[1:]]

wybor=input("Podaj czy chcesz wczytać dane z pliku (PLIK) czy z klawiatury (KLAWA) czy system (SYS): ")
if wybor =="PLIK":
    try:
        with open("dane.txt","r") as f:
            A=np.array(f.read().split(),dtype=float)
    except:
        print("Błąd wczytywania pliku")
        exit()

elif wybor=="KLAWA":
    A=np.array(input().split(","),dtype=float)
elif wybor=="SYS":
    A=np.array(dane)
else:
    print("Błędny wybór")
    exit()

suma=np.sum(A) #suma wszystkich elementów
srednia=np.mean(A) #średnia wszystkich elementów
wariancja=np.var(A)  #oblicz wariację i odchylenie standardowe
odchylenie=np.std(A)
print("Suma: ",suma)    
print("Średnia: ",srednia)
print("Wariancja: ",wariancja)
print("Odchylenie standardowe: ",odchylenie)