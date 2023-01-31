
def dzielniki(liczba):
    lista = []
    for i in range(1, liczba):
        if liczba % i == 0:
            lista.append(i)
    
    return lista

def pierwsza(liczba):
    if liczba == 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def doskonala(liczba):
    suma = 0
    for i in dzielniki(liczba):
        suma += i
    if suma == liczba:
        return True
    return False

def main():
    try:
        liczba = int(input('Podaj liczbe: '))
    except ValueError:
        print('To nie jest liczba')
    else:
        print('Dzielniki: ', dzielniki(liczba)+[liczba])
        if pierwsza(liczba):
            print('Liczba pierwsza')
        if doskonala(liczba):
            print('Liczba doskonala')
if __name__ == '__main__':
    main()
  