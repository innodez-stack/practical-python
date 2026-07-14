"""Modified pcost file using csv module"""
import csv
def portfolio_cost(filename):
    """Calculate total portfolio cost using csv module"""
    total_cost = 0.0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip the header row
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                total_cost += shares * price
            except (ValueError, IndexError):
                # Skip bad data
                pass
    return total_cost

if __name__ == "__main__":
    total_cost = portfolio_cost("Data/portfolio.csv")
    print(f"Total cost: ${total_cost:0.2f}")
