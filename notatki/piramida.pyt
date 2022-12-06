n = int(input("wpisz liczbe"))
j = n-1
for i in range(1,n+1):
    print(" "*j,end="")
    print("**"*i)
    j-=1