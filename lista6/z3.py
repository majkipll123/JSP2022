from itertools import groupby
def las(numer):
    return ''.join( str(len(list(g))) + k
		for k,g in groupby(numer) )
#intertool groupby robi tabele dla ktorej 
start='4'
for i in range(10):
	print(start)
	start = las(start)