class kolo:
    def __init__(self, R):
        self.R = R
    def obwod(self):
        return 2*3.14*self.R
    def pole(self):
        return 3.14*self.R**2
    def __str__(self):
        return "Kolo o promieniu: " + str(self.R)
def main():
    k = kolo(5)
    print(k)
    print(k.obwod())
    print(k.pole())
if __name__ == '__main__':
    main()