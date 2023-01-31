# Sortowanie bąbelkowe i przez wybieranie


def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                #funkcja bubble sort
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



def selection_sort(lista):
    for i in range(len(lista)):
        minimum = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimum]:
                minimum = j
                #funkcja selection sort
        lista[i], lista[minimum] = lista[minimum], lista[i]
    return lista


