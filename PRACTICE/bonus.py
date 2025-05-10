num_employees =int(input())
emp_data=[]

for i in range(num_employees):
    name=input().strip()
    designation = input().strip()
    salary= int(input())
    month_count=int(input())
    overtime = {}
    
    for n in range(month_count):
        month=input().strip()
        hours=int(input())
        overtime[month]=hours
    emp_data.append([name,designation,salary,overtime])
    
threshold=int(input())
rate=int(input())
total_bonus=0

for emp in emp_data:
    total_hours= sum(emp[3].values())
    emp.append(total_hours >= threshold)

    if total_hours>=threshold:
        total_bonus+=total_hours*rate
    
for i in emp_data:
    print(i[0], i[4])
print (total_bonus)

