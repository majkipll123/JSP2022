def nieparzyste(lista):
    lista2 = []
    for i in lista:
        try:
            if i % 2 != 0:
                lista2.append(i)
        except TypeError:
            pass
    print(lista2)

nieparzyste([0,1,23,3,434,"a321c","b"])