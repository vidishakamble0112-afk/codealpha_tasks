STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nType 'done' when you have finished adding stocks.\n")

    portfolio = {}

    while True:
        stock = input("Enter stock name: ").upper().strip()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.\n")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty <= 0:
                print("Quantity must be greater than zero.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"Added {qty} x {stock}\n")

    if not portfolio:
        print("No stocks entered.")
        return

    total = 0
    lines = ["Stock Portfolio Summary", "-" * 40]
    for stock, qty in portfolio.items():
        value = STOCK_PRICES[stock] * qty
        total += value
        lines.append(f"{stock}: {qty} x ${STOCK_PRICES[stock]} = ${value}")
    lines.append("-" * 40)
    lines.append(f"Total Investment: ${total}")

    print()
    print("\n".join(lines))

    save = input("\nSave result to file? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio.txt", "w") as f:
            f.write("\n".join(lines))
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
