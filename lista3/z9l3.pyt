n=int(input())
m=int(input())
tabela=[]
for i in range(m):
    rzad=[]
    for j in range(n):
        rzad.append(i*j)
    tabela.append(rzad)
for wiersz in tabela:
    
    print("".join([f"{number:5d}"for number in wiersz]))


