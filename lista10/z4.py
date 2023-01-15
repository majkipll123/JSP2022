#napisz program do przelicania wakut, kursy wczytywanie z pliku .xml 
#glowna klasa powinna byc inicjalizowana sciezka do pliku xml 
#powinno posiadac konwertowanie z jednej waluty do drugiej podane przez uzytkownika 
class waluty:
    def __init__(self,sciezka):
        self.sciezka=sciezka
        self.kursy={}
        self.kursy=self.wczytaj()
    def wczytaj(self):
        import xml.etree.ElementTree as ET
        tree=ET.parse(self.sciezka)
        root=tree.getroot()
        for i in root:
            self.kursy[i.attrib['currency']]=float(i.attrib['rate'])
        return self.kursy
    def konwertuj(self,waluta1,waluta2,kwota):
        return kwota*self.kursy[waluta1]/self.kursy[waluta2]
    def pokaz(self):
        return self.kursy
    def pokaz_walute(self,waluta):
        return self.kursy[waluta]

    
