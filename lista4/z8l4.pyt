def harmoniczny(n):
    return sum(1.0/d for d in range (2,n+1))
b=int(input('podaj n-ta liczbe szeregu harmonicznego: '))
print(harmoniczny(b))