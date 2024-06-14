class Stock:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

    def value(self):
        return self.quantity * self.price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        self.stocks = [stock for stock in self.stocks if stock.symbol != symbol]

    def total_value(self):
        return sum(stock.value() for stock in self.stocks)

    def total_change(self):
        return sum(stock.quantity * (stock.price - 100) for stock in self.stocks)

def main():
    portfolio = Portfolio()

    while True:
        print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per share: "))
            portfolio.add_stock(Stock(symbol, quantity, price))
            print("Stock added successfully.")

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            portfolio.remove_stock(symbol)
            print("Stock removed successfully.")

        elif choice == "3":
            print("\nPortfolio:")
            for stock in portfolio.stocks:
                print(f"Symbol: {stock.symbol}, Quantity: {stock.quantity}, Price: {stock.price}, Value: {stock.value()}")
            print(f"\nTotal Portfolio Value: {portfolio.total_value()}")
            print(f"Total Portfolio Change: {portfolio.total_change()}")

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
