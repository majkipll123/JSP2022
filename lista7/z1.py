import time
c=0
n1,n2=0,1
n=int(input("podaj liczbe wyrazow ktora chcesz zobaczyc"))
start_time = time.time()
if n==0:
    print(n1)
else: 
    print("Fibonacci sequence:")
    while c < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       c += 1
print("sekund ",end=" ")
print(time.time() - start_time)
