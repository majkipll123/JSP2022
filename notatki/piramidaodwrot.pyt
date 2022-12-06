n = int(input("wpisz liczbe"))
i = n
while i > 0:
    print("*" * i)
    i-=1
for i in range(2,n+1):
    print("*"*i)