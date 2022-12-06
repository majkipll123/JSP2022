a=int(input("wpisz a > 0:"))
b=int(input("wpisz b:"))
c=int(input("wpisz c > b:"))
suma=0
for i in range(c):
    if(i%a==0):
        suma += i
    elif(i%b==0):
        suma += i
print(suma)