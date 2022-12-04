klucz = {
    "a" : "y",
    "e" : "i",
    "i" : "o",
    "o" : "a",
    "y" : "e"
}
slowo = list("Andrzej duda prezydentem polski")
zakres = len(slowo)
def szyf():
    for i in range(zakres):
        for j in klucz:
            if(slowo[i] == j):                
                slowo[i] = klucz[j]         
                break
    szyfr = "".join(slowo)                 
    return szyfr
szyfr = list(szyf())

def deszyf():
    for i in range(zakres):
        for j in klucz:                  
            if(szyfr[i] == klucz[j]):     
                szyfr[i] = j
                break
    deszyfr = "".join(szyfr)
    return deszyfr

print(szyf())
print(deszyf())