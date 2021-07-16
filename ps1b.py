annual_salary = float(input("Enter your starting annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal:"))
current_savings = 0
t = 0.04
additional_savings = 0
no_of_months_required = 0
r = 0.04
no_of_months_to_increment = 6
while current_savings < down_payment:
    if no_of_months_to_increment == 0:
        monthly_salary += semi_annual_raise * monthly_salary
        no_of_months_to_increment = 6
    monthly_return = (current_savings * r / 12)
    current_savings += (monthly_salary * portion_saved) + monthly_return
    no_of_months_required += 1
    no_of_months_to_increment -= 1
print("Number of months: " + str(no_of_months_required))



