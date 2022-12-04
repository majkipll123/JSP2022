
import cmath
a=""
b=""
wyraz=list(input())
wyraz2=list(input())
print(wyraz)
print(wyraz2)
if (len(wyraz)%2)==0:
    print(wyraz[:(len(wyraz)/2)]+wyraz2+wyraz[(len(wyraz)/2):])
else:
    print(a.join(wyraz[0,x2])+wyraz2+b.join(wyraz[x2:]))
