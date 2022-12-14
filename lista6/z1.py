import sys 
from  trojkat import *
#if __name__ is "__main__":
x=int(input("podaj 1 liczbe do trojkata"))
y=int(input("podaj 2 liczbe do trojkata"))
z=int(input("podaj 3 liczbe do trojkata"))

if (pole(x,y,z)>0):
    print(obw(x,y,z))
    print(pole(x,y,z))
    print(rozno(x,y,z))
    print(kat(z,y,x))
else :
    print("warunki trojkata nie sa spelnione")