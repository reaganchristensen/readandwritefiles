import csv

EmployeePay = open('EmployeePay.csv', 'r')

csv_file = csv.reader(EmployeePay)

next(csv_file)

for rec in csv_file:
    bonus = float(rec[4])
    salary = int(rec[3])

    print(f"first name: {rec[1]}")
    print(f"last name: {rec[2]}")
    print(f"salary: ${salary:10,.2f}")
    print(f"bonus: ${bonus * salary:10,.2f}")
    print(f"pay: ${(bonus * salary) + salary:10,.2f}")
    input()
