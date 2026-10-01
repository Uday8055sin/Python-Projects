# ==========================================
#       STOCK PORTFOLIO TRACKER
# ==========================================

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

# Dictionary to store user's portfolio
portfolio = {}

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, "=", "$", price)

print("\nEnter 'done' when you finish adding stocks.")

# ------------------------------------------
# User Input
# ------------------------------------------

while True:

    stock = input("\nEnter stock name: ").upper()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    quantity = input("Enter quantity: ")

    # Check if quantity is a number
    if not quantity.isdigit():
        print("Please enter a valid quantity.")
        continue

    quantity = int(quantity)

    # Store stock and quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# ------------------------------------------
# Calculate Total Investment
# ------------------------------------------

total_investment = 0

print("\n" + "=" * 45)
print("           YOUR PORTFOLIO")
print("=" * 45)

for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    investment = price * quantity

    total_investment += investment

    print(
        stock,
        "| Price: $", price,
        "| Quantity:", quantity,
        "| Investment: $", investment
    )

# ------------------------------------------
# Display Total
# ------------------------------------------

print("=" * 45)
print("TOTAL INVESTMENT: $", total_investment)
print("=" * 45)

# ------------------------------------------
# Save Result to TXT File
# ------------------------------------------

save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write("=" * 40 + "\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Price: ${price} | "
                f"Quantity: {quantity} | "
                f"Investment: ${investment}\n"
            )

        file.write("\n")
        file.write(
            f"TOTAL INVESTMENT: ${total_investment}\n"
        )

    print("Portfolio saved successfully in portfolio.txt")

else:

    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")