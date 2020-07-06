'''
This program takes in two parameters like a credit interest and credit principal, and calculates
values like monthly payment or overpayment which then is printed out on the monitor
credit principal is the original money on the credit, while the interest is a charge for borrowed money.
'''

import math
credit_principal = int(input("Enter the credit principal: "))

months_or_monthly_payment = input(
"""What do you want to calculate?
type "m" - for count of months,
type "p" - for monthly payments: """)

if months_or_monthly_payment == "m":
    monthly = int(input("Enter monthly payment: "))
    payment = math.ceil(credit_principal / monthly)
    if payment >= 2:
        print(f"It takes {payment} months to repay the credit")
    else:
        print(f"It takes {payment} month to repay the credit")

if months_or_monthly_payment == "p":
    counts = int(input("Enter count of months: "))
    each_month = math.ceil(credit_principal / counts)
    last_payment = credit_principal - (counts - 1) * each_month
    if each_month != last_payment:
        print(f"Your monthly payment = {each_month} with last month payment {last_payment}")
    else:
        print(f"Your monthly payment = {each_month}")