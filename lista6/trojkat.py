import math
def obw(x,y,z):
    r=x+y+z
    return r
def pole(x,y,z):
    s=(x+y+z)/2
    c=math.sqrt(s*(s-x)*(s-y)*(s-z))
    return c
def rozno(x,z,y):
    if(x==y==z):
        a="rownoboczny"
        return a 
    if(x==y or y==z or z==x):
        a="rownoramienny"
        return a 
    else:
        a="roznoboczny"
        return a
def kat(x,y,z):
    if (x>y and x>z):
        if((z*z)+(y*y)<x*x):
            b="rozwartokatny"
            return b
        elif((z*z)+(y*y)>x*x):
            b="ostrokatny"
            return b
        else:
            b="prostokatny"
            return b
    elif (y>z and y>x):
        if((z*z)+(x*x)<y*y):
            b="rozwartokatny"
            return b
        elif((z*z)+(x*x)>y*y):
            b="ostrokatny"
            return b
        else:
            b="prostokatny"
            return b
    else:
        if((y*y)+(x*x)<z*z):
            b="rozwartokatny"
            return b
        elif((y*y)+(x*x)>z*z):
            b="ostrokatny"
            return b
        else:
            b="prostokatny"
            return b