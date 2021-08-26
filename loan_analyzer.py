# coding: utf-8
# Athit Padmasuta
"""Required Module Imports"""
# Module for csv file handling
import csv
# Module for handling files from OS paths
from pathlib import Path

"""Part 1: Automate the Calculations."""
# List of Loan Costs
loan_costs = [500, 600, 200, 1000, 450]

# Used the len function to calculate the total number of loans in the list.
total_number_of_loans = len(loan_costs)
#Didplay the value.
print("The total number of loans is ", total_number_of_loans)

# Used the sum function to calculate the total value of all loans in the list.
total_value_of_loans = sum(loan_costs)
#Display the value.
print("The total value of loans is $", total_value_of_loans)

# Used the sum value of all loans divided by the total number of loans to calculate the average loan price.
average_loan_amount = total_value_of_loans / total_number_of_loans
# Display the value.
print("The average loan amount is $", average_loan_amount)

"""Part 2: Analyze Loan Data."""

# Given the following loan data, you will need to calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Used get() on the dictionary of additional information to extract theLoan Price, Future Value, and Remaining Months on the loan.
loan_price = loan.get("loan_price")
remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")
# Display the values.
print(loan_price)
print(remaining_months)
print(future_value)

# Used the formula for Present Value to calculate a "fair value" of the loan.
# Used a hardcoded minimum required return of 20% as the discount rate.
# Formula -> Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months.
present_value = future_value / (1 + 0.2/12) ** remaining_months

# Wrote a conditional statement to decide if the present value represents the loan's fair value.
# If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
# Else, if the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if present_value > loan_price:
    print("Loan is worth buying")
else:
    print("Loan is not worth buying")

"""Part 3: Perform Financial Calculations."""

# Given the following new_loan data, you will need to calculate the present value for the loan.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Defined a new function that will be used to calculate present value.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return present_value


# Used the function to calculate the present value of the new loan based on new_loan dictionary key.
# Used an annual_discount_rate variable set to 0.2 for this new loan calculation.
annual_discount_rate = 0.20
present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
#Display the value.
print(f"The present value of the loan is: {present_value}")


"""Part 4: Conditionally filter lists of loans."""
# Loans Dictionary
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Created an empty list called inexpensive_loans
inexpensive_loans = []
# Looped through loans and appended any loan that cost less than $500 to the 'inexpensive_loans' list.
for loan in loans:
    if loan["loan_price"] < 500:
        inexpensive_loans.append(loan)

# Print the inexpensive_loans list.
print(inexpensive_loans)

"""Part 5: Save the results."""

# Set the output header.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path.
output_path = Path("inexpensive_loans.csv")

# Used the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())