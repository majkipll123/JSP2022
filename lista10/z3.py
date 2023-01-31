#utworz klase ktora dopasowuje liste w 3 elementowe listy
#w tali sposob ze jezeli masz podane 1,2,3,4,5,6 to tworzy listy 3 elementowe 1,2,3 4,5,6
class SummingTriplets:
    def __init__(self, numbers):
        self.numbers = numbers
  
    def triplets_with_sum_zero(self):
        triplets = []
        numbers = self.numbers
        numbers.sort()
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            l, r = i + 1, len(numbers) - 1
            while l < r:
                s = numbers[i] + numbers[l] + numbers[r]
                if s == 0:
                    triplets.append([numbers[i], numbers[l], numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return triplets
def main():
    numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
    st = SummingTriplets(numbers)
    print(st.triplets_with_sum_zero())
if __name__ == '__main__':
    main()
    