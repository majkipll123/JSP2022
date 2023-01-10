import datetime

def validate_pesel(pesel: str) -> bool:
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10)) % 10
    return int(pesel[-1]) == checksum

def extract_data_from_pesel(pesel: str) -> tuple:
    year = int(pesel[0:1])
    month = int(pesel[2:3])
    day = int(pesel[4:5])
    sex = int(pesel[10])
    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900
    sex = "K" if sex % 2 == 0 else "M"
    birth_date = datetime.date(year, month, day)
    return (birth_date, sex)

#reading file
with open("PESEL.txt") as pesel_file:
    pesel_list = pesel_file.readlines()

valid_pesel = []

#validating and extracting data
for pesel in pesel_list:
    pesel = pesel.strip()
    if validate_pesel(pesel):
        valid_pesel.append(pesel)
        birth_date, sex = extract_data_from_pesel(pesel)
        print(f"Nr PESEL: {pesel}\nData urodzenia: {birth_date.strftime('%d-%m-%Y')}; Płeć: {sex}")
    else:
        print(f"PESEL {pesel} jest nieprawidłowy.")

#saving to file
with open("valid_pesel.txt", "w") as valid_pesel_file:
    for pesel in valid_pesel:
        birth_date, sex = extract_data_from_pesel(pesel)
        valid_pesel_file.write(f"Nr PESEL: {pesel}\nData urodzenia: {birth_date.strftime('%d-%m-%Y')}; Płeć: {sex}\n")
