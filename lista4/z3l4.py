import math
pi=math.pi
rad=int(input("Podaj czy chcesz konwertowac radiany na stopnie(1) czy stopnie na radiany(0)"))

if rad ==0:
    x=float(input("teraz podaj ile stopni chcesz obliczyc na radiany"))
    print((x*180)/pi)
else:  
    x=float(input("teraz podaj ile radianow chcesz przeliczyc na stopnie"))
    print((x*pi)/180)
  