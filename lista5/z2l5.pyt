def naslowa(x):
    jednosci ={
        1:"jeden",
        2:"dwa",
        3:"trzy",
        4:"cztery",
        5:"piec",
        6:"szesc",
        7:"siedem",
        8:"osiem",
        9:"dziewiec"
    }
    dziesiatki={
        1:"dziesiec",
        11:"jedenasice",
        12:"dwanascie",
        13:"trzynascie",
        14:"czternascie",
        15:"pietnascie",
        16:"szesnascie",
        17:"siedemnascie",
        18:"osiemnascie",
        19:"dziewietnascie",
        2:"dwadziescia",
        3:"trzydziesci",
        4:"czterdziesci",
        5:"piedziesiat",
        6:"szesdziesiat",
        7:"siedemdziesiat",
        8:"osiemdziesiat",
        9:"dziewiedziesiat"
    }
    setki={
        1:"sto",
        2:"dwiescie",
        3:"trzysta",
        4:"czterysta",
        5:"piecset",
        6:"szescset",
        7:"siedemset",
        8:"osiemset",
        9:"dziewiecset"
    }
    l=""
    if len(x) ==1:
        if int(x) in jednosci:
            print(jednosci.get(int(x)))
    elif len(x) == 2:
        if int(x) in dziesiatki:
            print(dziesiatki.get(int(x)), end=" ")
        elif int(x[0]) in dziesiatki:
            print(dziesiatki.get(int(x[0])), end=" ")
            if int(x[1]) in jednosci:
                print(jednosci[int(x[1])])
    elif len(x) == 3:
        if int(x[0]) in setki:
            print(setki[int(x[0])], end=" ")
        if int(x[1:]) in dziesiatki:
            print(dziesiatki[int(x[1:])], end=" ")
        elif int(x[1]) in dziesiatki:
            print(dziesiatki[int(x[1])], end=" ")
            if int(x[2]) in jednosci:
                print(jednosci[int(x[2])])
    elif len(x) == 4:
        print("tysiąc", end=" ")
        if int(x[1]) in setki:
            print(setki[int(x[1])], end=" ")
        if int(x[2:]) in dziesiatki:
            print(dziesiatki.get(int(x[2:])), end=" ")
        elif int(x[2]) in dziesiatki:
            print(dziesiatki.get(int(x[2])), end=" ")
            if int(x[3]) in jednosci:
                print(jednosci.get(int(x[3])))

x = input("Podaj liczbe: ")
naslowa(x)

