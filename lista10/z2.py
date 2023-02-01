class x:
    def __init__(self,l):
        self.dane_wej=l
        self.podlisty=[]
        for i in range(len(self.dane_wej)):
            for j in range(i+1,len(self.dane_wej)+1):
                self.podlisty.append(self.dane_wej[i:j])
    def ser_l(self):
        return self.podlisty
def main():
    l=[-1,2,3]
    a=x(l)
    print(a.ser_l())
if __name__ == '__main__':
    main()