import csv

customers = open('customers.csv', 'r')

outfile = open("customer_country.csv", "w")

csv_file = csv.reader(customers)

next(csv_file)  #skip a row

outfile.write("Full Name, Country\n")
for rec in csv_file:
    outfile.write(f"{rec[1]} {rec[2]}, {rec[3]}\n")

                  
outfile.close()