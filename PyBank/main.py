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
avg_pl_changes = 0.0
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
   # print(f"header: {header}")
   
   
    for row in csv_reader:
        months.append(row[0])
        p_and_l.append(row[1])

        #Calculate the net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])
   

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
sum_of_diff = 0
index1 = 0
diff = 0
pl_changes2 = []
for x in p_and_l:
    if index1 < len(p_and_l)-1:
        diff = int(p_and_l[index1+1]) - int(p_and_l[index1]) 
        pl_changes2.append(diff)
        sum_of_diff += diff
    index1 += 1
avg_pl_changes =   int(sum_of_diff) / int(index1-1)
""" print("Avg = " + str(avg_pl_changes))
print("Total Months  " + str(index1)) """

#Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase_in_profits = max(pl_changes2)
#returns the index to locate month with greatest increase
find_month_index1 = pl_changes2.index(greatest_increase_in_profits)


#Calculate the greatest decrease in losses (date and amount) over the entire period
greatest_decrease_in_losses = min(pl_changes2)
#returns the index to locate month with greatest decrease
find_month_index2 = pl_changes2.index(greatest_decrease_in_losses)

#print(months[find_month_index2+1])
output_analysis = (
   f"Financial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {index1}\n"
   f"Total: ${total}\n"
   f"Average  Change: ${avg_pl_changes:.2f}\n"
   f"Greatest Increase in Profits: {months[find_month_index1+1]} (${str(max(pl_changes2))})\n"
   f"Greatest Decrease in Profits: {months[find_month_index2+1]} (${str(min(pl_changes2))})\n")
print(output_analysis)                   
budget_csv2 = os.path.join("Resources", "output_budget_data3.txt")
# Export the results to text file
with open(budget_csv2, "w") as txt_file:
    txt_file.write(output_analysis)

