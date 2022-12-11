K = ({"k": "król", 2: {2:"syn", "1": ["córka", "wróbel"]}, "3": "5"}, ("żółw", "pies"))
print(K[0][2]["1"][1])

A = [["Jeden", "Dwa"], {1: "jeden", 2: "dwa"}]
print("Przed: ", A)
A[1][1] = A[0][0]
A[1][2] = A[0][1]
print("Po: ", A)
