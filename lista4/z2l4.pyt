lista=input("Podaj kilka liczb oddzielonych od siebie ',' a usune powtarzajace sie liczby ")
lista=lista.split(",")
lista=list(set(lista))
print(lista)

