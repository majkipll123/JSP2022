#napisz klase o nazwie kolo ktora jest konstuowana  za pomoca promienia R i zawierajaca dwie metody obliczajace obwod i pole   
#kola o promieniu R

class kolo:
    def __init__(self, R):
        self.R = R
    def obwod(self):
        return 2*3.14*self.R
    def pole(self):
        return 3.14*self.R**2
#wypisz pole i obwod na ekranie
