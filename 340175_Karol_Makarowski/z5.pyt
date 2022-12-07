wyrazy=[]
abcd=""
vowels = 'aeiou'
def punkty():

    ip_str = input("podaj zdanie/wyraz: ")
    wyraz(ip_str)
    print(wyraz(ip_str))

def wyraz(string):
    samo=0
    for i in range(len(string)):
        if string[i] in vowels:
            samo+=1
    print(samo)
    #print(wyrazy.append((samo,wyraz())))
punkty()


