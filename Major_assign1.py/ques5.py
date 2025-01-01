def basic_salary(hourly_rate, hours_worked_per_week):
    # Calculate basic salary for a month (4 weeks)
    return hourly_rate * hours_worked_per_week * 4

def overtime_salary(hourly_rate, hours_worked_per_week):
    # Calculate overtime salary for hours worked beyond 40 hours per week
    if hours_worked_per_week > 40:
        overtime_hours = hours_worked_per_week - 40
        return overtime_hours * hourly_rate * 1.5 * 4  # Overtime for 4 weeks
    return 0

def total_salary(hourly_rate, hours_worked_per_week):
    # Calculate total salary
    basic = basic_salary(hourly_rate, hours_worked_per_week)
    overtime = overtime_salary(hourly_rate, hours_worked_per_week)
    return basic + overtime

def tax_amount(basic_salary):
    # Calculate tax based on the basic salary
    if basic_salary < 60000:
        return basic_salary * 0.10  # 10% tax
    elif 60000 <= basic_salary <= 85000:
        return basic_salary * 0.15  # 15% tax
    else:
        return basic_salary * 0.20  # 20% tax

def gross_salary(basic_salary):
    # Calculate allowances (20% of basic salary)
    allowances = basic_salary * 0.20
    # Calculate tax
    tax = tax_amount(basic_salary)
    # Calculate gross salary
    return basic_salary + allowances - tax

def salary_bracket(gross_salary):
    # Categorize the gross salary into income brackets
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"

def employee_report():
    # List to hold employee details
    employees = []

    # Take input for three employees
    for i in range(3):
        name = input(f"Enter the name of employee {i+1}: ")
        hourly_rate = float(input(f"Enter the hourly rate for {name}: "))
        hours_worked_per_week = float(input(f"Enter the hours worked per week for {name}: "))
        
        # Calculate salaries and tax
        basic = basic_salary(hourly_rate, hours_worked_per_week)
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        
        # Store employee details in a dictionary
        employees.append({
            'name': name,
            'basic_salary': basic,
            'gross_salary': gross,
            'tax_amount': tax,
            'salary_bracket': bracket
        })

    # Print formatted report
    print("\nEmployee Salary Report")
    print("-" * 50)
    print(f"{'Name':<20} {'Basic Salary':<15} {'Gross Salary':<15} {'Tax Amount':<15} {'Salary Bracket'}") #<20,15 is written for number of spaces
    print("-" * 50)
    for emp in employees:
        print(f"{emp['name']:<20} {emp['basic_salary']:<15.2f} {emp['gross_salary']:<15.2f} {emp['tax_amount']:<15.2f} {emp['salary_bracket']}")
    print("-" * 50)

# Call the employee_report function
employee_report()