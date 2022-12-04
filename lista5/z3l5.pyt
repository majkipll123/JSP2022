rzymskie = {
    "M" : 1000,
    "D" : 500,
    "C" : 100,
    "L" : 50,
    "X" : 10,
    "V" : 5,
    "I" : 1
}
def rz_arab(r):
    suma = 0
    for i in range(len(r)):
        if i == len(r)-1:                  
            suma += rzymskie[r[i]]
            return suma
        if rzymskie[r[i]] < rzymskie[r[i+1]]:   
            suma -= rzymskie[r[i]]              
        else:
            suma += rzymskie[r[i]]             
    return suma

print(rz_arab("MMMDCXLVIII"))