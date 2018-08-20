principal = -1
count = 0

while principal < 0 and count < 3:
    try:
        principal = float(input("Enter Loan Amount:"))
    except ValueError:
        print("Invalid Loan Amount")
        count += 1

if count == 3:
    print("Input Invalid, Bye")
    exit()

interest = 12.99
periods = 4
n_years = 2

final_cost = principal * (1+interest/100.0/periods)**n_years

print(final_cost)
print("{cost:0.2f}".format(cost=final_cost))
print("Total Interest Paid: {interest:0.02f}".format(interest=final_cost-principal))
print("Monthly Payments: {payment:0.02f}".format(payment=final_cost/24))