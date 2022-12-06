ciag = input("wpisz slowo/zdanie")
i = 97
while i <= 122:
    if (i == 97) or (i == 101) or (i == 105) or (i == 111) or (i == 117) or (i == 121) or (i == 65) or (i == 69) or (i == 73) or (i == 79) or (i == 85) or (i == 89):
        litera = ciag.count(chr(i))
        litera += ciag.count(chr(i-32))
        print("samogłoska ", chr(i), " występuje ",litera)
    i+=1