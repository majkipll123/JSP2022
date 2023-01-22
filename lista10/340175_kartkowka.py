import math 
class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    @staticmethod
    def dodaj(z1, z2):
        return Zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def odejmij(z1, z2):
        return Zespolona(z1.re - z2.re, z1.im - z2.im)

    @staticmethod
    def mnoz(z1, z2):
        return Zespolona(z1.re * z2.re - z1.im * z2.im, z1.re * z2.im + z1.im * z2.re)

    @staticmethod
    def dziel(z1, z2):
        return Zespolona((z1.re * z2.re + z1.im * z2.im) / (z2.re**2 + z2.im**2), (z1.im * z2.re - z1.re * z2.im) / (z2.re**2 + z2.im**2))

    def __str__(self):
        return str(self.re) + '+' + str(self.im) + 'i'

    def modul(self):
        return (self.re**2 + self.im**2)**0.5
        
    def argument(self):
        return math.atan(self.im / self.re)

if __name__ == '__main__':
    z1 = Zespolona(1, 2)
    z2 = Zespolona(3, 4)
    print(Zespolona.dodaj(z1, z2))
    print(Zespolona.odejmij(z1, z2))
    print(Zespolona.mnoz(z1, z2))
    print(Zespolona.dziel(z1, z2))
    print(z1.modul())
    print(z1.argument())

