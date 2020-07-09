'''
This program let one compute all different parameters of the credit. So far this program calculate the annuity payment
which are fixed during the whole credit term.
Asking the user which parameter it wanna use from calculating the count of periods, monthly payment or credit payment.
When choosing an option, the user need to fill inn the remaining values such as; credit principal, monthly payment,
credit interest, count of periods. And compute and output the value the user wanted
credit principal is the original money on the credit, while the interest is a charge for borrowed money.
'''
import math


months_or_monthly_payment = input(
"""What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal: """)


if months_or_monthly_payment == "n":
    credit_principal = int(input("Enter credit principal: "))
    monthly = int(input("Enter monthly payment: "))
    credit_interest = float(input("Enter credit interest: "))

    nominal_interest_rate = credit_interest / (12 * 100)
    count_of_periods = math.ceil(math.log(monthly / (monthly - nominal_interest_rate * credit_principal), 1 + nominal_interest_rate))
    month_converter = count_of_periods % 12
    year_converter = count_of_periods // 12


    if year_converter >= 2 and month_converter >= 2:
        print(f"It takes {year_converter} years and {month_converter} months to repay this credit")
    elif year_converter == 0:
            print(f"It takes {month_converter} months to repay this credit")
    else:
        print(f"It takes {year_converter} year and {month_converter} month to repay this credit")

if months_or_monthly_payment == "a":
    credit_principal = int(input("Enter credit principal: "))
    months = int(input("Enter count of periods: "))
    credit_interest = float(input("Enter credit interest: "))

    nominal_interest_rate = credit_interest / (12 * 100)
    annuity_payment = credit_principal * ((nominal_interest_rate * (1 + nominal_interest_rate) ** months) /
                                          (((1 + nominal_interest_rate) ** months) - 1))
    print(f"Your annuity payment = {math.ceil(annuity_payment)}!")

if months_or_monthly_payment == "p":
    monthly_payment = float(input("Enter monthly payment: "))
    months = int(input("Enter count of periods: "))
    credit_interest = float(input("Enter credit interest: "))

    nominal_interest_rate = credit_interest / (12 * 100)
    annuity_payment = monthly_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** months) /
                                          (((1 + nominal_interest_rate) ** months) - 1))

    print(f"Your credit principal = {annuity_payment:.0f}!")

