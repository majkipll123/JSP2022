import random

def generate_random_pesel():
    # Generates a random PESEL number as a string
    pesel = str(random.randint(100000000, 999999999))
    pesel = pesel[:3] + str(random.randint(0, 2)) + pesel[4:]
    check_digit = str(random.randint(0, 9))
    return pesel + check_digit

def write_pesel_to_file(pesel):
    # Writes the PESEL number to a file called "PESEL.txt"
    with open("PESEL.txt", "a") as file:
        file.write(pesel + "\n")

# Generate and write 10 PESEL numbers to the file
for i in range(10):
    pesel = generate_random_pesel()
    write_pesel_to_file(pesel)
