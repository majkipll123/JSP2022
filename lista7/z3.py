import random
import time
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
start_time = time.time()
rand_list100=[]
rand_list200=[]
rand_list300=[]
a=100
b=200
c=300
for i in range(a):
    rand_list100.append(random.randint(0,20))
    

for i in range(b):
    rand_list200.append(random.randint(0,20))
    

for i in range(c):
    rand_list300.append(random.randint(0,20))

bubbleSort(rand_list100)
bubbleSort(rand_list200)
bubbleSort(rand_list300)
print("sekund ",end=" ")
print(time.time() - start_time)