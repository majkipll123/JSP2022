def obroc(txt, key):
    def cipher(i, low=range(97,123), upper=range(65,91)): #sprawdza czy literka jest mala czy duza jezeli nie to pomija
        if i in low or i in upper:
            #jezeli jest mala to ustawia nma 65 czyli male a jezeli duza to 97 czyli duze A
            s = 65 if i in upper else 97
            #jezeli jest mala np a to bierze 97 odejmuje od niej 65 po czym dodale przeskok 
            #np 2 i wychodzi liczba z ktorej jezeli zrobikmy %26 poniewaz tyle jest liter w anglieksim alfabecie i dodamy do niej znowu 65 to da nam przesunieta liczbe
            i = (i - s + key) % 26 + s
        return chr(i) #zwraca nam literke
    a=''.join([cipher(ord(s)) for s in txt]) #do pustego stringa dodaje po kolei kazda litere lub znak specialny
    return a
# w obroc 2 nastepuje to samo tylko pobieramy juz zakodowane zdanie i klucz jest ujemny zeby dzialalo w 2 strone 
def obroc2(a, key):
   def cipher(i, low=range(97,123), upper=range(65,91)):
     if i in low or i in upper:
       s = 65 if i in upper else 97
       i = (i - s - key) % 26 + s
     return chr(i)
   return ''.join([cipher(ord(s)) for s in a])
