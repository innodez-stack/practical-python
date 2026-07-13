# pcost.py
def portfolio_cost(filename):
    """Calculate the total cost of a portfolio from a CSV file."""
    total_cost = 0.0
    with open(filename, "r") as f:
        for line in f:
            # Remove the \n and extra whitespace from each line
            clean_line = line.strip()
            columns = clean_line.split(",")

            try:
                shares = int(columns[1])
                price = float(columns[2])
                total_cost += shares * price
            except (ValueError, IndexError):
                # Skip header row and bad data
                pass
                
    return total_cost

# Test it
if __name__ == "__main__":
        cost = portfolio_cost("Data/portfolio.csv")
        print(f"Total cost: ${cost:0.2f}")
