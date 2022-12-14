import random
import time
def wypisz(tab): 
    for el in tab:
        print(el, end=" | ")
def sortuj_wstaw(tab, n): 
    for x in range(1, n):
        wybrana = tab[x] 
        y = x-1 
        while y >= 0 and wybrana< tab[y]: 
            tab[y+1] = tab[y] 
            y -= 1 
        tab[y+1] = wybrana 
start_time = time.time()
rand_list100=[]
rand_list200=[]
rand_list300=[]
a=100
b=200
c=300
for i in range(a):
    rand_list100.append(random.randint(0,20))
    

for i in range(b):
    rand_list200.append(random.randint(0,20))
    

for i in range(c):
    rand_list300.append(random.randint(0,20))
    sortuj_wstaw(rand_list100,a)
#wypisz(rand_list100) SPRAWDZA ALE DZIALA WIEC GIT
sortuj_wstaw(rand_list200,b)
sortuj_wstaw(rand_list300,c)
print("sekund ",end=" ")
print(time.time() - start_time)
