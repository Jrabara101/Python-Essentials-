def calculate_payslip(name, hours_worked, rate_per_hour):
    """Calculates the payslip for an employee.

    Args:
        name: Employee's name.
        hours_worked: Number of hours worked.
        rate_per_hour: Rate per hour.

    Returns:
        A dictionary containing the payslip details.
    """

    gross_salary = hours_worked * rate_per_hour
    sss_contribution = 100
    philhealth = 100
    housing_loan = 100
    other_loan = 100  # Adjust as needed
    tax = round(gross_salary * 0.10, 2)  # 10% tax
    total_deductions = sss_contribution + philhealth + housing_loan + other_loan + tax
    net_salary = gross_salary - total_deductions

    payslip = {
        "Employee Name": name,
        "Rendered Hours": hours_worked,
        "Rate per Hour": f"PHP {rate_per_hour:.2f}",
        "Gross Salary": f"PHP {gross_salary:.2f}",
        "SSS": sss_contribution,
        "PhilHealth": philhealth,
        "Housing Loan": housing_loan,
        "Other Loan": other_loan,
        "Tax": f"PHP {tax:.2f}",
        "Total Deductions": f"PHP {total_deductions:.2f}",
        "Net Salary": f"PHP {net_salary:.2f}"
    }

    return payslip

# Example usage:
employee_name = "Johnrick Rabara"
hours_worked = 10
rate_per_hour = 500

payslip_data = calculate_payslip(employee_name, hours_worked, rate_per_hour)

# Print the payslip in a formatted way
for key, value in payslip_data.items():
    print(f"{key}: {value}")