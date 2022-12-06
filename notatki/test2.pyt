spol = 0
samo = 0
napis=input("podaj napis")
for x in napis:
    if x in "aeiouy":
        samo = samo+1
    else:
        spol = spol+1
print("spolglosek bylo tyle :")
print(spol,end=" ")
print("a samoglosek tyle:")
print(samo)