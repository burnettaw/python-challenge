# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won


# The winner of the election based on popular vote.
import os
import csv

voter_id = []
county = []
candidate = []
unique_candidates = []
total_votes_cast = 0

# read the file and calculate total
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print header
    header = next(csv_reader)
   # print(f"header: {header}")
   
    #line_num = 0

    for row in csv_reader:
        """ months.append(row[0])
        p_and_l.append(row[1]) """
                
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        #Calculate the net total amount of votes
        total_votes_cast += 1


#Calculate complete list of candidates who recieved votes
current_candidate = ""
next_candidate = ""
index = 0
for x in candidate:
    current_candidate = x
    if index < len(candidate)-1:
        next_candidate = candidate[index + 1]
    elif current_candidate != next_candidate:
        unique_candidates[index] = candidate
        
    index += 1
print (unique_candidates)

"""

#Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase_in_profits = max(pl_changes2)
#returns the index to locate month with greatest increase
find_month_index1 = pl_changes2.index(greatest_increase_in_profits)


#Calculate the greatest decrease in losses (date and amount) over the entire period
greatest_decrease_in_losses = min(pl_changes2)
#returns the index to locate month with greatest decrease
find_month_index2 = pl_changes2.index(greatest_decrease_in_losses)
"""
#prints output to screen and file 
output_analysis = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"----------------------------\n" ) 
"""
  f"Total Months: {index1}\n"
   f"Total: ${total}\n"
   f"Average  Change: ${avg_pl_changes:.2f}\n"
   f"Greatest Increase in Profits: {months[find_month_index1+1]} (${str(max(pl_changes2))})\n"
   f"Greatest Decrease in Profits: {months[find_month_index2+1]} (${str(min(pl_changes2))})\n") 
"""
print(output_analysis)      
"""             
budget_csv2 = os.path.join("Resources", "output_budget_data3.txt")
# Export the results to text file
with open(budget_csv2, "w") as txt_file:
    txt_file.write(output_analysis) """

