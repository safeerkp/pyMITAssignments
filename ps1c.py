annual_salary = float(input("Enter your starting annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = 0.0
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
semi_annual_raise = 0.07
current_savings = 0
t = 0.04
no_of_months_required = 36
r = 0.04
no_of_months_to_increment = 6
steps_in_search = 0
print("Best savings rate: " + str(portion_saved))
print("Steps in bisection search: " + str(steps_in_search))
