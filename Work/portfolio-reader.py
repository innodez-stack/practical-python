# 1. Create an empty list to store the portfolio data
portfolio_data = []
total_cost = 0.0

# 2. Read the portfolio data from a file or other source
with open("Data/portfolio.csv", "r") as f:
    for line in f:
        # Remove the \n and extra whitespace from each line
        clean_line = line.strip()
        # Parse each line and append to the portfolio data list
        portfolio_data.append(clean_line)
    print("\n-----Processing Portfolio Data-----")
    for item in portfolio_data[1:]:
        columns = item.split(",") # Split the line into columns based on commas
        shares = int(columns[1])
        price = float(columns[2])

        # Calculate the total cost
        total_cost += shares * price

print(f"\nTotal cost of the portfolio: ${total_cost:.2f}")