import os
import csv

#dictionary to hold all the data
budget_dict = {}
#stores overall total 
total = 0
#'PyBank\Resources\budget_data.csv'
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_dict = {"Month": "Profit-Loss"}

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print header
    header = next(csv_reader)
    print(f"header: {header}")

    #for k, v in prices.items():
    #...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount

    for row in csv_reader:
        total = total + int(row[1])
        budget_dict = [row]

print(budget_dict[0])


#Calculate the net total amount of "Profit/Losses" over the entire period
print (total)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


#Calculate the greatest increase in profits (date and amount) over the entire period


#Calculate the greatest decrease in losses (date and amount) over the entire period
