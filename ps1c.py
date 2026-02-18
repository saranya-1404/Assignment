# Constants
total_cost = 1000000
down_payment = total_cost * 0.25
annual_return = 0.04
semi_annual_raise = 0.07
months = 36
epsilon = 100   # accuracy within $100

# User input
starting_salary = float(input("Enter the starting salary: "))

# Step 1: Check if saving 100% salary is enough
current_savings = 0
annual_salary = starting_salary
monthly_salary = annual_salary / 12

for month in range(1, months + 1):
    current_savings += current_savings * (annual_return / 12)
    current_savings += monthly_salary
    if month % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    # Step 2: Bisection Search
    low = 0
    high = 10000
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        savings_rate = mid / 10000

        current_savings = 0
        annual_salary = starting_salary
        monthly_salary = annual_salary / 12

        # Calculate savings for 36 months
        for month in range(1, months + 1):
            current_savings += current_savings * (annual_return / 12)
            current_savings += monthly_salary * savings_rate
            if month % 6 == 0:
                annual_salary *= (1 + semi_annual_raise)
                monthly_salary = annual_salary / 12

        # Check result
        if abs(current_savings - down_payment) <= epsilon:
            print("Best savings rate:", round(savings_rate, 4))
            print("Steps in bisection search:", steps)
            break
        elif current_savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1
