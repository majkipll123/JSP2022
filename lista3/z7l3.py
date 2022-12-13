n=int(input())
a=0
b=1
print(a,b, end=" ")
for i in range (1, n-1):
    a,b=b, a+b
    print(b, end=" ")
