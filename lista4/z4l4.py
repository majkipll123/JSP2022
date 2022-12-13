n=int(input("podaj wyraz ciagu geometrycznego ktory mam dla ciebie obliczyc  "))
a1=int(input("teraz podaj pierwszy wyraz ciagu geometrycznego  "))
q=int(input('natomiast teraz q  '))
if n==1:
    print(a1)
else:
    An=a1*(q**(n-1))
    print(An)