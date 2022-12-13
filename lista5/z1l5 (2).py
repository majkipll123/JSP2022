def naliczbynie(x):
    wartosci ={
        "zero":0,
        "jeden":1,
        "dwa":2,
        "trzy":3,
        "cztery":4,
        "piec":5,
        "szesc":6,
        "siedem":7,
        "osiem":8,
        "dziewiec":9,
        "dziesiec":10,
        "jedenasice":11,
        "dwanascie":12,
        "trzynascie":13,
        "czternascie":14,
        "pietnascie":15,
        "szesnascie":16,
        "siedemnascie":17,
        "osiemnascie":18,
        "dziewietnascie":19,
        "dwadziescia":20,
        "trzydziesci":30,
        "czterdziesci":40,
        "piedziesiat":50
    }
    l=0 
    if x in wartosci:
        l+= wartosci.get(x)
    else:
        x=x.split(" ")
        if x[0] in wartosci:
            l+=wartosci.get(x[0])
        if x[1] in wartosci:
            l+=wartosci.get(x[1])
    return l
x= input("podaj liczbe slownie")
print(naliczbynie(x))