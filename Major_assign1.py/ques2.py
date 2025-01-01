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

# Example usage:
hourly_rate = 20  # Example hourly rate
hours_worked_per_week = 45  # Example hours worked per week

# Calculate total salary
total = total_salary(hourly_rate, hours_worked_per_week)

# Calculate basic salary
basic = basic_salary(hourly_rate, hours_worked_per_week)

# Calculate tax amount
tax = tax_amount(basic)

# Display results
print(f'Total salary for the month: ${total:.2f}')
print(f'Basic salary: ${basic:.2f}')
print(f'Tax amount deducted: ${tax:.2f}')