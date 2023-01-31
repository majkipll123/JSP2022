import random
import time
import sortowanie

def main():
    lista = []
    for i in range(1000):
        lista.append(random.randint(0, 1000))
    start = time.time()
    sortowanie.bubble_sort(lista)
    end = time.time()
    print('Czas sortowania bąbelkowego: ', end - start)
    start = time.time()
    sortowanie.selection_sort(lista)
    end = time.time()
    print('Czas sortowania przez wybieranie: ', end - start)

if __name__ == '__main__':
    main()




