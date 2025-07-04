# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 310
}

# Function to calculate total investment
def calculate_investment():
    total_investment = 0
    investments = []

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock in stock_prices:
            try:
                quantity = int(input(f"Enter quantity of {stock}: "))
                value = stock_prices[stock] * quantity
                total_investment += value
                investments.append((stock, quantity, value))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Stock not found in price list.")

    # Display results
    print("\n--- Investment Summary ---")
    for stock, qty, value in investments:
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    print(f"Total Investment Value: ${total_investment}")

    # Ask to save the result
    save = input("\nDo you want to save the result? (yes/no): ").lower()
    if save == 'yes':
        file_type = input("Choose file format - txt or csv: ").lower()
        if file_type == 'txt':
            with open("investment_summary.txt", "w") as f:
                f.write("--- Investment Summary ---\n")
                for stock, qty, value in investments:
                    f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
                f.write(f"Total Investment Value: ${total_investment}\n")
            print("Saved as investment_summary.txt")
        elif file_type == 'csv':
            with open("investment_summary.csv", "w") as f:
                f.write("Stock,Quantity,Price per Share,Value\n")
                for stock, qty, value in investments:
                    f.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
                f.write(f",,,{total_investment}\n")
            print("Saved as investment_summary.csv")
        else:
            print("Invalid file type. Not saved.")

# Run the tracker
calculate_investment()
# This code is a simple stock investment tracker that allows users to input stock symbols and quantities,
# calculates the total investment value, and saves the summary in either a text or CSV file.
# It uses hardcoded stock prices for simplicity.
# The user can enter multiple stocks, and the program will summarize the investments and total value.
# The code handles invalid inputs and provides feedback to the user.
# The user can choose to save the results in a specified format.
# The program continues to prompt for stock symbols until the user types 'done'.
# The code is designed to be user-friendly and straightforward for basic stock tracking needs.