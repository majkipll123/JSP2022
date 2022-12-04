import cmath
x=int(input())
x=complex(x)
print(cmath.phase(1j)) 
print(abs(x)) 
print((x+3j).conjugate())






#notatki:
#zstrzalka sprzezenie 
#1+2i==(1,2) 
# (a,b) z= a+bi (a,b) |z|=pierwiastekz a^2+b^2
#modul liczby zespolonej to jest dlugosc wektora odpowiadajaca liczbie zespolonej 
# miara kata w radianach to jest argument z 
# sprzezenie zapewnia zmiane znaku a-bi??
# z*zsprzezenie= (a*bi)(a-bi)= a**2-bi**2= a**2- b**2 *i**2=a**2-b**2*(-1)= a^2+b^2 = |z|^2