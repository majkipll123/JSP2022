import math
import cmath
wybor = input("wybierz konwersje: z układu kartezjańskiego na sferczyny = 1 lub ze sferycznego na kartezjański = 2 ")
if wybor == '1':
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    r = math.sqrt(x*x + y*y + z*z)
    theta = cmath.acos(z/r)
    fi = cmath.atan(y/x)
    print("wartosci po konwersji do układzu sferycznego: r = ", r,", theta = ", theta, ", fi = ",fi)
if wybor == '2':
    r = float(input("r = "))
    while(r <= 0):
        r = float(input("Podaj R >= 0 !!! "))
    theta = float(input("theta = "))
    fi = float(input("fi = "))
    x = r*math.sin(theta)*math.cos(fi)
    y = r*math.sin(theta)*math.sin(fi)
    z = r*math.cos(theta)
    print("wartosci po konwersji do układzu kartezjańskiego: x = ", x,", y = ", y, ", z = ",z)
else: 
    print("nie no nie ma takiego wyboru")