#napisz klase w python inicjaloizowana za pomoca listy n liczb rzeczywistych klasa powinna zawierac metode zwracajaca trojelementowe podlisty takie ze suma elementow wynosi 0
class x:
    def __init__(self,l):
        self.dane_wej=l
        self.podlisty=[]
        for i in range(len(self.dane_wej)):
            for j in range(i+1,len(self.dane_wej)+1):
                self.podlisty.append(self.dane_wej[i:j])
    def ser_l(self):
        return self.podlisty