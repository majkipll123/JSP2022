import os
import sys
import re
from datetime import datetime

def odszyfruj(plik, key):
    
    # bierze sciezke i bierze zaszyfrowany text
    with open(plik, 'r') as f:
        text = f.read()
    #szyfr cezara w pliku
    a_deszyfr = ""
    def cipher(i, low=range(97,123), upper=range(65,91)): 
        if i in low or i in upper:
            
            s = 65 if i in upper else 97
            i = (i - s - key) % 26 + s
        return chr(i)
    a_deszyfr=''.join([cipher(ord(s)) for s in text]) 
    return a_deszyfr
def decrypt_files_in_directory(sciezka):

    # pobiera wszystkie pliki z sciezki
    files = os.listdir(sciezka)
    # znajdz pliki "plik_zaszyfrowany%n_%Y%m%d.txt"
    wzor = re.compile(r'plik_zaszyfrowany(\d+)_\d{4}-\d{2}-\d{2}\.txt') # import re
    filename=""
    for file in files:
        
        dopasowanie = re.search(wzor,file) #zwraca boola
        #print(dopasowanie) dopasowanie = blad?
        if dopasowanie:
            #sciaga klucz z nazwy pliku
            key = int(dopasowanie.group(1))
            #odszyfruj plik
            a_deszyfr = odszyfruj(os.path.join(sciezka, file), key) #sciezka
            #zapisz odszyfrowany plik
            date = datetime.now().strftime("%Y%m%d")
            filename = f"plik_deszyfrowany{key}_{date}.txt"
    #try:
    with open(filename, "a") as f:
        f.write(a_deszyfr)
    #except:
        #print(f"Wystąpił błąd podczas zapisu pliku.")
        #sys.exit(1)


def main():
   
    # wiadomo co
    sciezka = input("Podaj sciezke do plików: ")

    # odszyfrowuje wszystkie pliki w sciezce i zapusije kazdy po kolei
    decrypt_files_in_directory(sciezka)



if __name__ == "__main__":
    main()