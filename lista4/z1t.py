a=[1,2,3,4,5,6,7]
print(sum(a))


def permutacje(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return(lista)
    list=[]
    for i in range(len(lista)):
        m=lista[i]
        remlista = lista[:i] + lista[i+1:]
        for p in permutacje(remlista):
            list.append([m]+p)
    return list
abcd=list('123')
for p in permutacje(abcd):
    print(p)
    


S=[]
n=int(input("podaj ile wyrazow ciagu harmonicznego cos tam"))
for i in range(n):
    s=float(1/(i+1))
    S=s.append()
print(sum(S))