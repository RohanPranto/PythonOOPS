# Input number of employees
num_employees = int(input())
employees = []

# Reading employee data
for _ in range(num_employees):
    emp = {}
    emp['name'] = input().strip()
    emp['designation'] = input().strip()
    emp['salary'] = int(input())
    emp['overtime'] = {}
    emp['status'] = False

    month_count = int(input())
    for _ in range(month_count):
        month = input().strip()
        hours = int(input())
        emp['overtime'][month] = hours

    employees.append(emp)

# Input threshold and rate per hour
threshold = int(input())
rate_per_hour = int(input())

# Check eligibility and calculate total bonus
total_bonus = 0
for emp in employees:
    total_hours = 0
    for hours in emp['overtime'].values():
        total_hours += hours

    if total_hours >= threshold:
        emp['status'] = True
        total_bonus += total_hours * rate_per_hour

# Print employee name and status
for emp in employees:
    print(emp['name'], emp['status'])

# Print total bonus
print(total_bonus)
