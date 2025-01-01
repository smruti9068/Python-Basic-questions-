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

# Example usage:
hourly_rate = 20  # Example hourly rate
hours_worked_per_week = 45  # Example hours worked per week

total = total_salary(hourly_rate , hours_worked_per_week)
print(f'Total salary for the month: ${total:.2f}')