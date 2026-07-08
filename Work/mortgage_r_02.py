principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1  # track the number of months

while principal > 0:
    if month <= 12:
        actual_payment = payment + 1000  # pay an extra $1000 for the first 12 months
    else:
        actual_payment = payment  # regular payment after the first 12 months

    total_paid += actual_payment
    principal = principal * (1 + rate / 12) - actual_payment
    month += 1

print('Total paid', total_paid)
print('Months to pay off the mortgage:', month - 1)  # subtract 1 because month is incremented after the last payment

