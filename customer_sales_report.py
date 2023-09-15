import csv
CustID = "250"
total = 0

sales = open('sales.csv', 'r')

csv_file = csv.reader(sales)

outfile = open("salesreport.csv", "w")

outfile.write("Customer ID", "Total")

next(csv_file)

for rec in csv_file:
    if CustID == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
    else:
        outfile.write(f"{CustID}, {total}")
        CustID == rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
outfile.write(f"{CustID}, {total}")

outfile.close()
