annual_salary = float(input("Enter your annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0
t = 0.04
additional_savings = 0
no_of_months_required = 0
r = 0.04
while current_savings < down_payment:
    monthly_return = current_savings * r / 12
    current_savings += (monthly_salary * portion_saved) + monthly_return
    no_of_months_required += 1
print("Number of months: " + str(no_of_months_required))



