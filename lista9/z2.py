import numpy as np
wybor=input("Podaj czy chcesz wczytać dane z pliku (PLIK) czy z klawiatury (KLAWA): ")
if wybor =="PLIK":
    try:
        with open("dane.txt","r") as f:
            A=np.array(f.read().split(),dtype=float)
    except:
        print("Błąd wczytywania pliku")
        exit()

elif wybor=="KLAWA":
    A=np.array(input().split(","),dtype=float)
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