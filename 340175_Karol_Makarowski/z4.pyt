slownik = (3,5,6,9,12,18,21,24,27,33,36,39,42,48,51,54,57,63,66,69,71,74,77,83,86,89,92,98,10,15,12,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95)
for i in range(2,99,2):
    if (i in slownik) and ((i)%3 == 0):
        print("Syk")
        if (i in slownik) and ((i)%5 == 0):
            print("Bzyk")
    elif (i in slownik) and ((i)%5 == 0):
        print("Bzyk")
    else:
        print(i)