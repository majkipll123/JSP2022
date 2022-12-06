slowo = input("wpisz cos ")
slowo = list(slowo)
taknie = 1
dl = len(slowo)
i = 0
while i < dl/2:
    j = (i + 1) * (-1)
    if slowo[i] != slowo[j]:
        taknie = 0
    i+=1
if (taknie):
    print(''.join(slowo), " jest palindromem")
else:
    print(''.join(slowo), " nie jest palindromem")