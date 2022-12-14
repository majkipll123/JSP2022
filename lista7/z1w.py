import time
def fib(n):
    if n==0: return 0 
    elif n==1: return 1
    return fib(n-1) + fib(n-2) 
c=0
n1,n2=0,1
n=int(input("podaj liczbe wyrazow ktora chcesz zobaczyc "))
start_time = time.time()
if n==0:
    print(n1)
else: 
    fib(n)
print("sekund ",end=" ")
print(time.time() - start_time)
