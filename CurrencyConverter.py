class Currency_Converter:
    def __init__(self):
        self.countries = ['USA', 'Mexico', 'Canada', 'UK', 'Japan', 'China']
        self.money_name = {'USA': 'USD', 'Mexico': 'Pesos', 'Canada': 'CAD', 'UK': 'GBP', 'Japan': 'JPY', 'China': 'CNY'}
        self.exchange_rate = {'USA': 1.0, 'Mexico': 19.56, 'Canada': 1.33, 'UK': 0.79, 'Japan': 109.07, 'China': 6.47}
    
    def getCountries(self):
        return self.countries
    
    def getMoney_name(self):
        return self.money_name

    def getExchange_rate(self):
        return self.exchange_rate
    
    def convert_currency(self, amount, from_currency, to_currency):
        initial_amount = amount
        amount = amount / self.exchange_rate[from_currency]
        amount = round(amount * self.exchange_rate[to_currency], 2)
        return "From " + str(initial_amount) + " " + from_currency + " " + self.money_name[from_currency] + ", the conversion to " + to_currency + " is " + str(amount) + " " + self.money_name[to_currency]



def main():

    cc = Currency_Converter()
    print("List of exchangable countires: " + str(cc.getCountries()))
    print("Conversion rates to USD: " + str(cc.exchange_rate))
    while True:
        from_currency = input("Enter the country to convert from or enter quit to quit: ")
        if from_currency == "quit":
            break
        amount = input("Enter amount: ")
        to_currency = input("Enter the country to convert to: ")
        result = cc.convert_currency(float(amount), from_currency, to_currency)
        print(result)


if __name__ == "__main__":
    main()
