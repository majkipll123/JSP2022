print("Witaj w kalkulatorze")
print("Podaj ilość przedmiotów (od 1 do 11)")
i = int(input())
s=[]
ocena = 1
suma = 0
lp = 0
# a1=list(map(char,a))
while i >= 1: #zmiana zmniejsze od 11 na wieksze od 1 
    print(f"Przedmiot nr {i}")
    print("Podaj oceny wagi 4:")
    print("(Po każdej ocenie wciśnij enter aby wpisać kolejną, a po wypisaniu wszystkich ocen wprowadź 0)")
    while ocena > 0:
        ocena = int(input())
        suma = suma + ocena * 4
        if ocena !=0:
            lp = lp + 4 # zmiana na +4 poniewaz jak waga oceny to 4 to musisz dodac 4 a nie 1 bo jak masz 5 wagi 4 i podzielisz przez 1 to ci wyjdzie ocena 20 xd
    ocena = 1
    print("Podaj oceny wagi 3:")
    print("(Po każdej ocenie wciśnij enter aby wpisać kolejną, a po wypisaniu wszystkich ocen wprowadź 0)")
    while ocena > 0:
        ocena = int(input())
        suma = suma + ocena * 3
        if ocena !=0:
            lp = lp + 3
    ocena = 1
    print("Podaj oceny wagi 2:")
    print("(Po każdej ocenie wciśnij enter aby wpisać kolejną, a po wypisaniu wszystkich ocen wprowadź 0)")
    while ocena > 0:
        ocena = int(input())
        suma = suma + ocena * 2
        if ocena !=0:
            lp = lp + 2
    ocena = 1
    print("Podaj oceny wagi 1:")
    print("(Po każdej ocenie wciśnij enter aby wpisać kolejną, a po wypisaniu wszystkich ocen wprowadź 0)")
    while ocena > 0:
        ocena = int(input())
        suma = suma + ocena * 1
        if ocena !=0:
            lp = lp + 1
    ocena = 1
    srednia=0 #to tutaj ponizej powiin za kazdym razme dodawac do listy srednia ale dodaje tylko ta ostatnia 
    srednia= suma/lp #nie wiem ocb
    suma=0
    lp=0
    srednia1=str(srednia)
    
    s.append(srednia1)
    i = i - 1
s=tuple(s)
print(s)