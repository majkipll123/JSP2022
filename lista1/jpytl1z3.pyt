#!/usr/bin/env python
import math
x=int(input())
m=math.radians(x)
sin=math.sin(m)
a=int(input())
b=int(input())
pole=1/2*a*b*sin
print("pole:")
print(pole)
print("wartosc sinusa:")
print(sin)
print("podany kat w radianach:")
print(m)