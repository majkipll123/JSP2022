i=1
with open("index.txt",'r') as f:
    tekst = f.readline()
    print(i,": ", tekst, sep="")
    i += 1
    while tekst:
        tekst = f.readline()
        print(i, ": ", tekst, sep="")
        i += 1