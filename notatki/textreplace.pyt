def funkcja(text):
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace(":", "")
    text = text.replace("'", "")
    text = text.lower()
    text = text.split()
    textmniej = []
    tab = []
    tab = list(tab)
    text2 = text
    for slowo in text:
        if slowo not in textmniej:
            textmniej.append(slowo)
    textmniej.sort()
    i = 0
    for j in range(len(textmniej)):
        tab.append(0)
    i = 0
    for slowo in text:
        if slowo in textmniej:
            for j in range(0,len(textmniej)):
                if textmniej[j] == slowo:
                    tab[j] += 1
                    i += 1
    i = 0
    for slowo in textmniej:
        print(slowo, ":", tab[i])
        i += 1

text = input("wpisz slowo/zdanie ")
funkcja(text)