import xml.etree.ElementTree as ET

class Rates:
    def __init__(self, path):
        self.rates = {}
        tree = ET.parse(path)
        root = tree.getroot()
        for child in root:
            currency = child.get("currency")
            rate = child.get("rate")
            if rate is not None:
                self.rates[currency] = float(rate)

    
    def list_rates(self):
        print("List of available exchange rates:")
        for currency, rate in self.rates.items():
            print(f"{currency}: {rate}")
    
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != "PLN":
            if from_currency in self.rates:
                amount = amount / self.rates[from_currency]
            else:
                raise KeyError(f"{from_currency} not found in exchange rates")
        if to_currency in self.rates:
            # convert to target currency
            amount = amount * self.rates[to_currency]
        else:
            raise KeyError(f"{to_currency} not found in exchange rates")
        return amount

# initialize with the path to the XML file
rates = Rates(r"C:\Users\majki\Downloads\a020z230130.xml")
def main():
    rates.list_rates()
    from_currency = input("Enter currency to convert from: ")
    to_currency = input("Enter currency to convert to: ")
    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("Invalid input. Amount must be a number.")
        return
    try:
        converted_amount = rates.convert(from_currency, to_currency, amount)
        print(f"Converted amount: {converted_amount}")
    except KeyError as e:
        print(str(e))

if __name__ == '__main__':
    main()
