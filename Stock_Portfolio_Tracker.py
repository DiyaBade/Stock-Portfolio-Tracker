#Stock Portfolio Tracker :-
import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not found in portfolio.")

    def track_performance(self):
        total_value = 0
        print("Stock\t|\tQuantity\t|\tCurrent Price\t|\tValue")
        print("-" * 60)
        for symbol, quantity in self.portfolio.items():
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
            response = requests.get(url)
            data = response.json()
            current_price = float(data["Global Quote"]["05. price"])
            value = current_price * quantity
            total_value += value
            print(f"{symbol}\t|\t{quantity}\t\t|\t${current_price:.2f}\t\t|\t${value:.2f}")
        print("-" * 60)
        print(f"Total Portfolio Value: ${total_value:.2f}")


def main():
    api_key = "YOUR_ALPHA_VANTAGE_API_KEY"
    portfolio = StockPortfolio(api_key)

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
