import sys
import os 
#program zapisuje wszystko do niepalindromow ?????/
dane=[(line) for line in sys.stdin] if len(sys.argv)==1 else [(args)for args in sys.argv[1:]]
def palindrom(arg):
    a=''.join(arg)
    plik = open(a, 'r')
    tekst = plik.read()
    if tekst == tekst[::-1]:
        try:
            plik = open('palindromy.txt', 'a')
            plik.write(tekst)
        except FileNotFoundError:
            print('Nie ma takiego pliku')
    else:
        try:
            plik = open('niepalindromy.txt', 'a')
            plik.write(tekst)
        except FileNotFoundError:
            print('Nie ma takiego pliku')



    plik.close()
def main():
    palindrom(dane);

if __name__ == '__main__':
    main()