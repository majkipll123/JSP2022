
class Obywatel:
    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.wiek = self.oblicz_wiek()

    def oblicz_wiek(self):
        import datetime
        data = datetime.datetime.now()
        rok = data.year
        miesiac = data.month
        dzien = data.day
        rok_urodzenia = int(self.data_urodzenia[0:4])
        miesiac_urodzenia = int(self.data_urodzenia[5:7])
        dzien_urodzenia = int(self.data_urodzenia[8:10])
        wiek = rok - rok_urodzenia
        if miesiac < miesiac_urodzenia:
            wiek -= 1
        elif miesiac == miesiac_urodzenia:
            if dzien < dzien_urodzenia:
                wiek -= 1
        return wiek

    def __str__(self):
        return 'Obywatel/ka ' + self.imie +" "+ self.nazwisko + ', ' + str(self.wiek)+", urodziny "+self.data_urodzenia+"."

def main():
    osob = Obywatel('Karol', 'Makarowski', '2003-09-11')
    print(osob)

if __name__ == '__main__':
    main()