ciag = input("wpisz slowo/zdanie")
i = 97
while i <= 122:
    litera = ciag.count(chr(i))
    litera += ciag.count(chr(i-32))
    print("litera ", chr(i), " występuje ",litera)
    i+=1