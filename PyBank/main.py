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


#'PyBank\Resources\budget_data.csv'
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print header
    header = next(csv_reader)
    print(f"header: {header}")
    budget_dict = {header[0]: header[1]}
    print("the dict with only header is " + str(budget_dict) )

    #for k, v in prices.items():
    #...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
   

    #  if arg1 == 1 and arg2 == 2
    # thisdict["year"] = 2018
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

#for each month in bugget_dict
print("budget dict after for loop--------------" )
print(budget_dict)


#Calculate the net total amount of "Profit/Losses" over the entire period
print(" total after "+ str(total))
print(" line count after "+ str(line_count))

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
for x in pl_changes:
    if x < 0:
        print (x)

jan = months[0]
janpl = p_and_l[0]
feb = months[1]
febpl = p_and_l[1]
pl1 = int(janpl) - int(febpl) 
print("diff in jan and feb " + str(pl1))

index1 = 0
diff = 0
pl_changes2 = []
for x in p_and_l:
    if index1 < len(p_and_l):
        diff = int(p_and_l[index1]) - int(p_and_l[index1+1])
    pl_changes2.append(diff)
    index1 += 1
print("index1  " + index1)
print("len(p_and_l)  " + len(p_and_l))
#Calculate the greatest increase in profits (date and amount) over the entire period
print( "max value  " + str(max(pl_changes2)))

#Calculate the greatest decrease in losses (date and amount) over the entire period
print( "min value  " + str(min(pl_changes2)))