stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}


total_investment = 0

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        total_investment += stocks[stock_name] * quantity
    else:
        print("Stock not found!")

print("Total Investment Value =", total_investment)

# Optional: Save to file
with open("investment.txt", "w") as file:
    file.write(f"Total Investment Value = {total_investment}")

print("Result saved in investment.txt")