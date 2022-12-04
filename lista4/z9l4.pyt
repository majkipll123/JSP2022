def silnia(n):
    return 1 if (n==1 or n==0) else n*silnia(n-1);
c=int(input("podaj lczbe z ktorej chcesz obliczyc silnie: "))
print('silnia dla twojego ',c,' wynosi',silnia(c))