n = int(input("wpisz liczbe"))
for i in range(1,n+1):
    print("*"*i)
while n-1 > 0:
    print("*" * (n-1))
    n-=1