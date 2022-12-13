print("wtaj w programie ktory policzy dla ciebie NWD dwoch podanych przez ciebie liczb ")
liczba1=int(input('podaj piersza liczbe'))
liczba2=int(input('podaj druga liczbe'))
licznik=0
while liczba1!=liczba2:
    licznik+=1
    if liczba1>liczba2:
        liczba1=liczba1-liczba2
    else:
        liczba2=liczba2-liczba1
print('NWD podanych przez ciebe liczb to :', liczba1)