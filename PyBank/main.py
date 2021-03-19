#Calculate the net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#Calculate the greatest increase in profits (date and amount) over the entire period
#Calculate the greatest decrease in losses (date and amount) over the entire period

import os
import csv

#dictionary to hold all the data
budget_dict = {}
#stores overall total 
total = 0
current_month = 0
next_month = 0

#holds profit & loss changes
pl_changes = []
avg_pl_changes = []
months = []
p_and_l = []
greatest_increase_in_profits = 0.0
greatest_decrease_in_losses = 0.0

# read the file and calculate total
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print header
    header = next(csv_reader)
    print(f"header: {header}")
    budget_dict = {header[0]: header[1]}
 
    line_count = 1
    for row in csv_reader:
        months.append(row[0])
        p_and_l.append(row[1])
        total = total + int(row[1])
        current_month = row[1]
        if line_count > 0 and line_count < len(row)-1 :
            next_month =  row[1-1]
        pl_changes.append(int(current_month) - int(next_month)) 
       
        line_count += 1
    budget_dict[header[0]] = months
    budget_dict[header[1]] = p_and_l

#Calculate the net total amount of "Profit/Losses" over the entire period
print(" total after "+ str(total))
#print(" line count after "+ str(line_count))

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
index1 = 0
diff = 0
pl_changes2 = []
for x in p_and_l:
    if index1 < len(p_and_l)-1:
        diff = int(p_and_l[index1+1]) - int(p_and_l[index1]) 
    pl_changes2.append(diff)
    index1 += 1
print("index1  " + str(index1))
print("len(p_and_l)  " + str(len(p_and_l)))
#Calculate the greatest increase in profits (date and amount) over the entire period
print( "max value  " + str(max(pl_changes2)))

#Calculate the greatest decrease in losses (date and amount) over the entire period
print( "min value  " + str(min(pl_changes2)))
""" 
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])


    import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


    # Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    fieldnames = ["last_name", "first_name", "ssn", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)


"""
#_, filename = os.path.split(budget_csv)
csvpath = os.path.join("Resources","budget_analysis.csv")
with open(csvpath, 'x') as csvfile:
    fieldnames = ["Date", "Profit/Losses"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(budget_dict)

 
"""
#write the results to file
budget_csv2 = os.path.join("Resources", "output_budget_data.csv")
with open(budget_csv2, "x", newline=" " ) as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for row in csv_writer:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
"""