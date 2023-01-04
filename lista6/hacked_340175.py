#10
karol="Karol"
a = open("payload_340175.txt", "r")
yy=(a.read())
def obroc(txt, key):
    def cipher(i, low=range(97,123), upper=range(65,91)): 
        if i in low or i in upper:
            
            s = 65 if i in upper else 97
            i = (i - s + key) % 26 + s
        return chr(i)
    a=''.join([cipher(ord(s)) for s in txt]) 
    return a

def obroc2(a, key):
   def cipher(i, low=range(97,123), upper=range(65,91)):
     if i in low or i in upper:
       s = 65 if i in upper else 97
       i = (i - s - key) % 26 + s
     return chr(i)
   return ''.join([cipher(ord(s)) for s in a])
#kiedy wpisuje
b=10
v=(obroc(yy,b))
abc=1
while abc==1:
    v=(obroc(yy,b))
    if "Karol" in v:
        plik1=open("hacked_340175.txt","w")
        plik1.write(v)
        abc=0

plik1=open("hacked_340175.txt","w")
plik1.write(v)
