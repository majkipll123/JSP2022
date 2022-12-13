from SzyftCezara import * 
a=input("podaj zdanie do szyfru ")
b=int(input("podaj o ile chcesz przesunac "))
v=(obroc(a,b))
print(v)
print(obroc2(v,b))