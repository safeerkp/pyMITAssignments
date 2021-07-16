
def get_no_of_months_required(annual_salary,portion_saved) : 
    monthly_salary = annual_salary / 12 
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    semi_annual_raise = 0.07
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

    return no_of_months_required

annual_salary = float(input("Enter your starting annual salary:"))
portion_saved = 1
no_of_months_required = get_no_of_months_required(annual_salary,portion_saved)
if(no_of_months_required > 36 ) :
    print("It is not possible to pay the down payment in three years.")
    exit()
count = 0
while True :
    count += 1
    print("no_of_months_required : "+str(no_of_months_required))
    print("portion_saved :"+str(portion_saved))
    if(no_of_months_required == 36 ) :
        break
    if(no_of_months_required < 36 ) :
        portion_saved = portion_saved - portion_saved / 2
    if(no_of_months_required > 36) :
        portion_saved = portion_saved + portion_saved / 2
    no_of_months_required = get_no_of_months_required(annual_salary,portion_saved)
    
print("Best savings rate: " + str(portion_saved))
print("Steps in bisection search: " + str(count)) 
    