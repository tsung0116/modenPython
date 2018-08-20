user_name = input("Enter your name:")
print("Hello, {name}".format(name=user_name))

principal = input("Enter Loan Amount:")
principal = float(principal)
interest = 12.99
periods = 4
n_years = 2

final_cost = principal * (1+interest/100.0/periods)**n_years

print(final_cost)
print("{cost:0.02f}".format(cost=final_cost))
print("Total Interest Paid: {interest:0.02f}".format(interest=final_cost-principal))
print("Monthly Payments: {payment:0.02f}".format(payment=final_cost/24))