from functools import reduce
i=input("podaj liczby odddzielone przecinkiem a ja podam ci ich sume i iloczyn: " )
a=i.split(',')
print(a)
a1=list(map(float,a))
print("Suma podanych przez ciebie liczb to: ")
print(sum(a1))
a2=reduce(lambda x, y : x*y,a1)
print("Ilocyn podanych przez ciebie liczb to: ")
print(a2)
