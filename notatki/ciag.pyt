import numpy as np
class CiagArytmetyczny:
    def __init__(self,a_0,r):
        self.a_0 = a_0
        self.r = r
    def element(self,n):
        self.n = n
        print(n,"-ty element = ",self.a_0 + (self.n-1)*self.r)
    def cumulative_sum(self,n):
        self.n = n
        print("suma ", n, " elementow = ",np.sum( (self.a_0*2+(self.n-1)*self.r)*self.n/2 ))
    def elements(self,n):
        self.n = n
        self.lista = []
        i = n
        while i > 0:
            self.lista.append(self.a_0 + (self.n-i)*self.r)
            i -= 1
        print(n," elementow ciagu ",self.lista)
    def dwaCiagi(self,a2,r2,n):
        self.a_0 = a2 + self.a_0
        self.r = r2 + self.r
        print("\n dla drugiego ciagu ")
        ciag.element(n)
        ciag.cumulative_sum(n)
        ciag.elements(n)


a = int(input("podaj pierwszy wyraz pierwszego ciagu "))
a2 = int(input("podaj pierwszy wyraz drugiego ciagu "))
r = int(input("podaj roznice pierwszego ciagu "))
r2 = int(input("podaj roznice drugiego ciagu "))
n = int(input("podaj na ilu wyrazach wykonac metody "))


ciag = CiagArytmetyczny(a,r)

ciag.element(n)
ciag.cumulative_sum(n)
ciag.elements(n)
ciag.dwaCiagi(a2,r2,n)