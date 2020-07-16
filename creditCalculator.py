'''
This program let one compute all different parameters of the credit. This program calculate the annuity payment
 which are fixed during the whole credit term, and the differentiated payment where the part of reducing the credit
 prinsipal is constant. Also the interest repayment part of the credit calculator, it reduces under the credit term.
Asking the user which parameter it wanna use from calculating the count of periods, monthly payment or credit payment.
When choosing an option, the user need to fill inn the remaining values such as; credit principal, monthly payment,
credit interest, count of periods and interest. And compute and output the value the user wanted
credit principal is the original money on the credit, while the interest is a charge for borrowed money.
'''
import math
import argparse
import sys

# Initialize the parser
parser = argparse.ArgumentParser(description="Credit Calculator")

# Add the parameters or optional:
parser.add_argument("--type", help= " choose between 'annuity' or 'diff'(differentiated) payment")
parser.add_argument("--payment", help= "monthly payment", type=int)
parser.add_argument("--principal", help= "calculation of both types e.g the total loan", type=int)
parser.add_argument("--periods", help= "denotes the number of months/or years needed to repay", type=int)
parser.add_argument("--interest", help= "convert the interest rate into a float", type=float)

args = parser.parse_args()
arguments = len(sys.argv) - 1

if arguments != 4:
    print("Incorrect parameters")
elif args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type is None:
    print("Incorrect parameters")
elif args.type == 'diff' and args.payment != None:
    print('Incorrect Parameters')
elif (args.payment or args.principal or args.periods or args.interest) <= 0:
    print("Incorrect parameters")
elif arguments != 4:
    print("Incorrect parameters")
elif args.type == "diff":

    if args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")
    elif args.periods < 0:
        print("Incorrect parameters")
    elif args.payment is not None:
        print("Incorrect parameters")
    else:
        nominal_interest_rate = args.interest / (12 * 100)
        differentiated_payments = []

        for month in range(1, args.periods + 1):
            d = math.ceil((args.principal / args.periods) + nominal_interest_rate * (args.principal - args.principal * (month - 1) / args.periods))
            differentiated_payments.append(d)
            print(f"Month {month}: paid out {d}")

        overpayment = int(sum(differentiated_payments) - args.principal)
        print()
        print(f"Overpayment = {str(math.ceil(overpayment))}")

elif args.type == "annuity":
    if (args.principal is None or args.periods is None or args.interest is None) and args.payment is None:
        print("Incorrect parameters")
    else:
        if args.payment is not None and args.periods is not None and args.interest is not None:
            nominal_interest_rate = args.interest / (12 * 100)
            annuity_payment = args.payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** args.periods) /
                                              (((1 + nominal_interest_rate) ** args.periods) - 1))
            overpayment = args.payment * args.periods - annuity_payment
            print(f"Your credit principal = {str(math.floor(annuity_payment))}!")
            print(f"Overpayment = {str(math.ceil(overpayment))}")

        elif args.principal is not None and args.periods is not None and args.interest is not None:
            nominal_interest_rate = args.interest / (12 * 100)
            annuity_payment = args.principal * ((nominal_interest_rate * (1 + nominal_interest_rate) ** args.periods) /
                                                  (((1 + nominal_interest_rate) ** args.periods) - 1))
            overpayment = (math.ceil(annuity_payment) * args.periods) - args.principal
            print(f"Your annuity payment = {str(math.ceil(annuity_payment))}!")
            print(f"Overpayment = {str(math.ceil(overpayment))}")

        elif args.principal is not None and args.interest is not None and args.payment is not None:
            nominal_interest_rate = args.interest / (12 * 100)
            count_of_periods = math.ceil(math.log(args.payment / (args.payment - nominal_interest_rate * args.principal), 1 + nominal_interest_rate))
            month_converter = count_of_periods % 12
            year_converter = count_of_periods // 12
            overpayment = int((math.ceil(count_of_periods) * args.payment) - args.principal)

            if year_converter >= 2 and month_converter >= 2:
                print(f"You need {str(year_converter)} years and {str(month_converter)} months to repay this credit")
                print(f"Overpayment = {str(math.ceil(overpayment))}")

            elif year_converter == 0:
                    print(f"You need {str(month_converter)} months to repay this credit")
                    print(f"Overpayment = {str(math.ceil(overpayment))}")
            elif year_converter >= 1 and month_converter == 0:
                print(f"You need {str(year_converter)} years to repay this credit")
                print(f"Overpayment = {str(math.ceil(overpayment))}")
            else:
                print(f"You need {str(year_converter)} year and {str(month_converter)} month to repay this credit")
                print(f"Overpayment = {str(math.ceil(overpayment))}")
