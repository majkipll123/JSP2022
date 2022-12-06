liczba = float(input("wpisz liczbe zmiennoprzecinkowa"))
liczba = str(liczba)
tab1 = [0,0,0,0,0,0,0,0,0,0]
tab2 = [0,0,0,0,0,0,0,0,0,0]
kropka = 0
for i in liczba:
    if kropka == 1:
        x = int(i)
        tab2[x] += 1
    if (i != ".") and (kropka == 0):
        x = int(i)
        tab1[x] += 1
    elif (i == "."):
        kropka = 1
licznik = 0
for i in tab1:
    print(licznik," dla części całkowitej występuje ",i," razy")
    licznik += 1
licznik = 0
for i in tab2:
    print(licznik, " dla części dziesiętnej występuje ", i, " razy")
    licznik += 1