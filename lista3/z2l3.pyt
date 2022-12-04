liczba= int(input())

if liczba%2 == 1 :
    print("liczba nieparzysta")
else:
    print("liczba parzysta")

abcd=("parzysta","nieparzysta")
print(abcd[liczba%2])
