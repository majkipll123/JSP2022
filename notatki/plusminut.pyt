lista = input("wpisz liste liczb całkowitych (elementy oddzielone spacjami)").split()
lista2 = []
lista1 = []
for i in lista:
    lista1.append(int(i))
lista1.sort()
for i in lista1:
    if i not in lista2:
        lista2.append(i)
lista2.sort()
lista1 = []

last = lista2[-1]
for i in range(0,last):
    if i not in lista2:
        lista1.append(i)
lista1.sort()
print(lista1)