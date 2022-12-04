x= range(3,100,3)
print(list(x))
z=list(x)
del z[4:100:3]
print(list(z))
print(sum(z)/len(z))