liczba = input("wpisz liczbe słownie od 1 do 20 bez znakow polskich ")
slownik =   {
            "zero": 0,
            "jeden": 1,
            "dwa": 2,
            "trzy": 3,
            "cztery": 4,
            "piec": 5,
            "szesc": 6,
            "siedem": 7,
            "osiem": 8,
            "dziewiec": 9,
            "dziesiec": 10,
            "jedenascie": 11,
            "dwanascie": 12,
            "trzynascie": 13,
            "czternascie": 14,
            "pietnascie": 15,
            "szesnascie": 16,
            "siedemnascie": 17,
            "osiemnascie": 18,
            "dziewietnascie": 19,
            "dwadziescia": 20,
            }
if (liczba in slownik) and (slownik.get(liczba)%3 == 0):
    print("Syk", end="")
    if slownik.get(liczba)%5 == 0:
        print("Bzyk")
elif (liczba in slownik) and (slownik.get(liczba)%5 == 0):
    print("Bzyk")
else:
    print(liczba)