import os
import sys
from datetime import datetime

def obroc(txt, key):
    def cipher(i, low=range(97,123), upper=range(65,91)): 
        if i in low or i in upper:
            
            s = 65 if i in upper else 97
            i = (i - s + key) % 26 + s
        return chr(i)
    a=''.join([cipher(ord(s)) for s in txt]) 
    return a

def save_file(a, shift, date):
    #"""Funkcja zapisująca zaszyfrowany tekst do pliku"""
    filename = f"plik_zaszyfrowany{shift}_{date}.txt"
    try:
        with open(filename, "w") as f:
            f.write(a)
    except:
        print(f"Wystąpił błąd podczas zapisu pliku {filename}.")
        sys.exit(1)

def get_filepath():
    #"""Funkcja pobierająca ścieżkę do pliku od użytkownika"""
    filepath = input("Podaj ścieżkę do pliku, który chcesz zaszyfrować: ")
    if not os.path.isfile(filepath):
        print(f"Plik {filepath} nie istnieje.")
        sys.exit(1)
    return filepath

def get_shift():
    #"""Funkcja pobierająca przesunięcie od użytkownika"""
    shift = 0
    while shift < 1 or shift > 10:
        try:
            shift = int(input("Podaj przesunięcie szyfru (1-10): "))
        except ValueError:
            print("Wprowadzona wartość jest niepoprawna. Wprowadź liczbę całkowitą.")
    return shift

def main():
    filepath = get_filepath()
    shift = get_shift()
    date = datetime.now().strftime("%Y%m%d")
    
    try:
        with open(filepath, "r") as f:
            text = f.read()
    except:
        print(f"Wystapil blad podczas odczytu pliku {filepath}.")
        sys.exit(1)

    a = obroc(text, shift)
    save_file(a, shift, date)

if __name__ == "__main__":
    main()
